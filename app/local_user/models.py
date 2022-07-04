from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class LocalUser(AbstractUser):
    date_naissance = models.DateField(blank=True, null=True)
    pseudo_discord = models.CharField(max_length=100, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
