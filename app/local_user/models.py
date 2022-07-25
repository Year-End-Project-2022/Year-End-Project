from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class LocalUser(AbstractUser):
    date_naissance = models.DateField(blank=True, null=True)
    pseudo_discord = models.CharField(max_length=100, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='static/img/user', blank=True, null=True)
    date_fst_adhesion = models.DateField(blank=True, null=True, help_text="date de 1er adhésion de l'utilisateur")
    date_last_adhesion = models.DateField(blank=True, null=True, help_text="date de dernière adhésion de l'utilisateur")
