# from django.shortcuts import render
from .serializers import StudentSerializer, TeacherSerializer, SimpleResponse
from students.models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from teachers.models import Teacher
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def student_views(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def teacher_views(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TeacherSerializer( data = request.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def student_views_detail(request, pk):
    try:
        students = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(students, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        students.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    



@api_view(['GET', 'PUT', 'DELETE'])
def teacher_views_detail(request, pk):
    try:
        teachers = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TeacherSerializer(teachers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        teachers.delete()
        return Response(status = status.HTTP_404_NOT_FOUND)



class SimpleResponseView(APIView):
    def get(self, request):
        data = {
            'message' : 'hello world'
        }
        serializer = SimpleResponse(data)
        return Response(serializer.data)

    



    
    
