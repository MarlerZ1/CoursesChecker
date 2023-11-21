import operator

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from students.models import Work
from teachers.forms import WorkEvaluationForm, WorkFeedbackForm
from teachers.models import Task, Feedback
from users.models import Group, User


# Create your views here.
def groupList(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, 'teachers/groupList.html', context)


def group(request, group_id):
    group = Group.objects.get(id=group_id)
    students = User.objects.filter(group=group)

    students = sorted(students, key=operator.attrgetter('last_name', 'first_name'))

    tasks = Task.objects.all()
    tasks = sorted(tasks, key=operator.attrgetter('number'))

    works = {}
    for student in students:
        works[student] = Work.objects.filter(student=student)
        works_s = []
        for task in tasks:
            added = False
            for work in works[student]:
                if work.task == task:
                    works_s.append(work)
                    added = True
            
            if not added:
                works_s.append(None)
        works[student] = works_s

    context = {
        'studentList': students,
        'taskList': tasks,
        'group': group,
        'works': works,
    }
    return render(request, 'teachers/group.html', context)


def work_check(request, work_id):
    work = Work.objects.filter(id=work_id).last()
    feedbackPast = Feedback.objects.filter(work=work).last()

    if request.POST:
        workFeedbackForm = WorkFeedbackForm(data=request.POST, instance=feedbackPast)
        workEvaluationForm = WorkEvaluationForm(data=request.POST, instance=work)

        if workFeedbackForm.is_valid() and workEvaluationForm.is_valid():
            workEvaluationForm.save()

            workFeedbackForm.save()
            feedback = Feedback.objects.last()
            feedback.work = work
            feedback.work.isEvaluate = False
            feedback.work.save()
            feedback.save()

        return HttpResponseRedirect(reverse('teachers:group', kwargs={'group_id': work.student.group.id}))
    else:
        workEvaluationForm = WorkEvaluationForm(instance=work)
        workFeedbackForm = WorkFeedbackForm(instance=feedbackPast)

        context = {
            'work': work,
            'workEvaluationForm': workEvaluationForm,
            'workFeedbackForm': workFeedbackForm,
        }
        return render(request, "teachers/workCheck.html", context)
