from django.urls import path
from courses import views
from django.contrib import admin

urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/<int:course_id>/', views.get_course),
    path('', views.test),
    path('admin/', admin.site.urls),
]