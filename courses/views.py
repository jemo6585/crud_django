from django.http import JsonResponse
from django.shortcuts import render
from .models import Course
# Create your views here.

def get_courses(request):
    courses = Course.objects.all()
    return JsonResponse(courses, safe=False)