from django.http import JsonResponse
from django.shortcuts import render
from .models import Courses
# Create your views here.

def get_courses(request):
    courses = Courses.objects.all()
    return JsonResponse(courses, safe=False)

def get_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    return JsonResponse(course, safe=False)

def test(request):
    return {
        "name": "test"
    }