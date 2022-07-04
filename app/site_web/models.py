from django.db import models
from django.utils.html import format_html


class ImageGalerie(models.Model):

    titre = models.CharField(max_length=200)

    alt = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='static/img/galerie')

    def __str__(self):
        return self.titre

    def admin_photo(self):
        return format_html('<img src="{}" width="100" height="100" />'
                           .format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
