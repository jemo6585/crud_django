from django.http import JsonResponse
from django.shortcuts import render
from .models import Course
# Create your views here.

def get_courses(request):
    courses = Course.objects.all()
    return JsonResponse(courses, safe=False)

def get_course(request, course_id):
    course = Course.objects.get(id=course_id)
    return JsonResponse(course, safe=False)