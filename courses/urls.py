from django.urls import path
from courses import views


urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/<int:course_id>/', views.get_course),
    path('', views.test)
]