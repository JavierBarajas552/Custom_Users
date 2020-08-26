from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    displayname = models.CharField(max_length=80, blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
