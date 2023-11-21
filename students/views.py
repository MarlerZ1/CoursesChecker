from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from students.forms import WorkEditForm
from students.models import Work
from teachers.models import Feedback, Task


# Create your views here.

def work_list(request):
    works = Work.objects.filter(student=request.user)

    context = {
        'works': works,
        'user': request.user
    }
    return render(request, 'students/workList.html', context)


def work_editor(request, work_id=None):
    work = Work.objects.filter(id=work_id).last()
    if request.method == 'POST':
        form = WorkEditForm(data=request.POST, instance=work)
        # form = WorkEditForm(data=request.POST or None, instance=request.user)
        # form.data.update(student=request.user)

        if form.is_valid():
            form.save()
            if not work_id:
                work = Work.objects.last()
            else:
                work = Work.objects.filter(id=work_id).last()
            work.student = request.user
            work.isEvaluate = True
            print(Work.objects.last().isEvaluate)
            work.save()
            print(Work.objects.last().isEvaluate)
            if Work.objects.filter(student=request.user).filter(task=work.task).count() > 1:
                work.delete()
                messages.warning(request, 'НЕЛЬЗЯ ДОБАВИТЬ ДВА ОДИНАКОВЫХ ОТВЕТА')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            return HttpResponseRedirect(reverse('students:workList'))
    else:
        form = WorkEditForm(instance=work)
    feedback = Feedback.objects.filter(work=work).last()

    context = {
        'form': form,
        'work': work,
        'user': request.user,
        'feedback': feedback,
        'defaultDescribe': Task.objects.first().description,
    }
    return render(request, 'students/workEditor.html', context)


def description_async(request):
    task_id = request.GET['id']
    task = Task.objects.get(id=task_id)

    return JsonResponse({'description': task.description})
