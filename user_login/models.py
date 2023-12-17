from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=10, choices=USER_ROLES, default='student')
