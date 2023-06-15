from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Student, Teacher, Subject
from .serializers import StudentSerializer, TeacherSerializer, SubjectSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'diary_app/index.html')




class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectListAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailAPIView(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer