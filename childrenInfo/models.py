from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ("M","Male"),
    ("F", "Female"),
    ("C", "Common"))

class ChildrenInfoModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    school = models.CharField(max_length=100)