from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class LocalUser(AbstractUser):
    pass

class Competance(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    value = models.IntegerField()