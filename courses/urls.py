from django.urls import path
from courses import views


urlpatterns = [
    path('courses/', views.get_courses),
]