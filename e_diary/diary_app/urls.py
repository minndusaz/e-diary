from . import views
from django.urls import path
from .views import StudentListAPIView, StudentDetailAPIView, TeacherListAPIView, TeacherDetailAPIView, SubjectListAPIView, SubjectDetailAPIView, ParentListAPIView, ParentDetailAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('teachers/', TeacherListAPIView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),
    path('subjects/', SubjectListAPIView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailAPIView.as_view(), name='subject-detail'),
    path('parents/', ParentListAPIView.as_view(), name='parent-list'),
    path('parents/<int:pk>/', ParentDetailAPIView.as_view(), name='parent-detail'),
]
