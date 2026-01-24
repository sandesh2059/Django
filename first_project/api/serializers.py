from rest_framework import serializers
from students.models import Student
from teachers.models import Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SimpleResponse(serializers.Serializer):
    message = serializers.CharField()

    class Meta:
        fields = ['message']