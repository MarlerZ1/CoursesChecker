
from django import template

register = template.Library()

@register.filter()
def get_student_works(works, student):
    return works[student]