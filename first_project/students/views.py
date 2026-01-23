from django.shortcuts import render
from rest_framework import response
from django.http import HttpResponse, JsonResponse

def student_view(request):
    students = {
        'id' : '10',
        'name' : 'sandesh'
    }
    return JsonResponse(students)


# Create your views here.
