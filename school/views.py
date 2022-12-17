from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    # for student in students:
    #     print('ученик', student.name, student.group)
    #     for teacher in student.teachers.all():
    #         print('учитель', teacher.name, teacher.subject)

    context = {'object_list': students}

    return render(request, template, context)
