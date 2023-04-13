from django.db import models

# Create your models here.

class Courses(models.Model):
    course_id = models.IntegerField(primary_key=True, auto_created=True)
    course_name = models.CharField(max_length=200)
    course_description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)