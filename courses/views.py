from django.http import JsonResponse
from django.shortcuts import render
from .models import Courses
#decorators
from django.views.decorators.csrf import csrf_exempt
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
        "id": course.course_id,
        "name": course.course_name,
        "description": course.course_description,
    }
    return JsonResponse(course_data, safe=False)

def test(request):
    return JsonResponse({
        "name": "test"
    })
@csrf_exempt
def add_or_delete_course(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course_description = request.POST.get("course_description")
        course = Courses(course_name=course_name, course_description=course_description)
        course.save()
        return JsonResponse({
            'course_id': course.course_id,
            'course_name': course.course_name,
            'course_description': course.course_description,
            
            "message": "Course added successfully"
            
        }, safe=False)
    elif request.method == "DELETE":
        course_id = request.POST.get("course_id")
        try:
            course = Courses.objects.get(course_id=course_id)
        
            course.delete()
            return JsonResponse({
            "message": "Course deleted successfully"
            }, safe=False)
        except:
            return JsonResponse({
            "message": "Course not found"
            }, safe=False)
    else:
        return JsonResponse({
            "message": "Invalid request"
        }, safe=False)

    
def delete_course(request, id):
    course = Courses.objects.get(course_id=id)
    course.delete()
    return JsonResponse({
        "message": "Course deleted successfully"
    }, safe=False)
    