from django import forms

from students.models import Work
from teachers.models import Task
from users.models import User


class WorkEditForm(forms.ModelForm):

    code = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'code',
        'id': 'code',
        'placeholder': 'Введите код',
    }))

    task = forms.ModelChoiceField(queryset=Task.objects.order_by('number'), initial=Task.objects.first(), widget=forms.Select(attrs={
        'class': 'task',
    }))

    # grade = forms.IntegerField()
    # isEvaluate = forms.BooleanField()
    # returnNumber = forms.IntegerField()

    class Meta:
        model = Work
        # fields = ['student', 'task', 'grade', 'isEvaluate', 'code', 'returnNumber']
        fields = [ 'task', 'code']