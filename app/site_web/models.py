from django.db import models


class ImageGalerie(models.Model):

    titre = models.CharField(max_length=200)

    alt = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='static/img/galerie')

    def __str__(self):
        return self.titre
