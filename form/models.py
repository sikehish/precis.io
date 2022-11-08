from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Resume(models.Model):
    title=models.CharField(max_length=30, blank=False)
    name= models.CharField(max_length=100)
    email= models.EmailField() 
    phone= models.CharField(max_length=12)
    website=models.URLField();
    profile=models.TextField()
    location=models.CharField(max_length=30)
    skills=ArrayField(
            models.CharField(max_length=20, blank=True),
        )
    employers=ArrayField(
            models.CharField(max_length=20, blank=True),
            size=3
        )
    titles=ArrayField(
            models.CharField(max_length=30, blank=True),
            size=3
        )
    job_start=ArrayField(
            models.CharField(max_length=10, blank=True),
            size=3
        )
    job_end=ArrayField(
            models.CharField(max_length=10, blank=True),
            size=3
        )
    degrees=ArrayField(
            models.CharField(max_length=30, blank=True),
            size=3
        )
    institutions=ArrayField(
            models.CharField(max_length=30, blank=True),
            size=3
        )
    edu_start=ArrayField(
            models.CharField(max_length=10, blank=True),
            size=3
        )
    edu_end=ArrayField(
            models.CharField(max_length=10, blank=True),
            size=3
        )

    uid=models.ForeignKey(User, default=None,  on_delete=models.CASCADE)
    createdat = models.DateTimeField(default= datetime.now, blank=True)