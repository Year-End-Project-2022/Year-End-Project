from django.contrib import admin
from .models import ImageGalerie


class ImageGalerieAdmin(admin.ModelAdmin):
    list_display = ('admin_photo',
                    'titre',
                    'alt'
                    )

    search_fields = ('titre',
                     'alt'
                     )

    readonly_fields = ('admin_photo',)


admin.site.register(ImageGalerie, ImageGalerieAdmin)
