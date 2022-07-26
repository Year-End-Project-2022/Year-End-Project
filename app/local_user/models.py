from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Competence(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class LocalUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)
    pseudo_discord = models.CharField(max_length=100, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='static/img/user', blank=True, null=True)
    date_fst_adhesion = models.DateField(blank=True, null=True)
    date_last_adhesion = models.DateField(blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    competences = models.JSONField(default={})
    credit = models.IntegerField(default=0)
