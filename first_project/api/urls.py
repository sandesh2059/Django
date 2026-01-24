from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.student_views),
    path('teachers/', views.teacher_views),
    path('student/<int:pk>', views.student_views_detail),
    path('teacher/<int:pk>', views.teacher_views_detail),
    path('response/', views.SimpleResponseView.as_view()),
]