from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Competence(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)


class UserCompetence(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()


class LocalUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)
    pseudo_discord = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    img = models.URLField(
        default="https://st4.depositphotos.com/1012074/20946/v/450/depositphotos_209469984-stock-illustration-flat-isolated-vector-illustration-icon.jpg")
    competences = models.ManyToManyField(UserCompetence)
    credit = models.IntegerField(default=0)
