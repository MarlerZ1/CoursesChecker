from django import forms

from students.models import Work
from teachers.models import Feedback


class WorkEvaluationForm(forms.ModelForm):
    grade = forms.IntegerField(max_value=5, min_value=2)

    class Meta:
        model = Work
        fields = ['grade']


class WorkFeedbackForm(forms.ModelForm):
    proposedSolution = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'code',
        'class': 'code',
        'placeholder': 'Введите предлагаемое решение',
        'onkeyup': 'resizeTextarea(this)'
    }))

    mistakeDescription = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'code',
        'class': 'code',
        'placeholder': 'Введите найденные ошибки',
        'onkeyup': 'resizeTextarea(this)'
    }))

    class Meta:
        model = Feedback
        fields = ['proposedSolution', 'mistakeDescription']
