from django.http import JsonResponse
from django.shortcuts import render
from .models import Courses
# Create your views here.

def get_courses(request):
    courses = Courses.objects.all()
    all_courses = [];
    for course in courses:
        all_courses.append({
            "id": course.course_id,
            "name": course.course_name,
            "description": course.course_description,
        })
    return JsonResponse(all_courses, safe=False)

def get_course(request, course_id):
    course = Courses.objects.get(course_id=course_id)
    course_data = {
        "id": course.course_name,
        "name": course.course_name,
        "description": course.course_description,
    }
    return JsonResponse(course_data, safe=False)

def test(request):
    return JsonResponse({
        "name": "test"
    })