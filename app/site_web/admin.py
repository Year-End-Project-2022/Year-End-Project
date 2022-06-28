from django.contrib import admin
from .models import ImageGalerie, Atelier, Niveau
from .models import PersonneDispo, Publique, Theme

# Register your models here.


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


@admin.register(Publique)
class PubliqueAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


@admin.register(PersonneDispo)
class PersonneDispoAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class ImageGalerieAdmin(admin.ModelAdmin):
    list_display = ('admin_photo',
                    'titre',
                    'alt'
                    )

    search_fields = ('titre',
                     'alt'
                     )

    readonly_fields = ('admin_photo',)


class AtelierAdmin(admin.ModelAdmin):
    list_display = ('admin_photo',
                    'titre',
                    'theme',
                    'publique',
                    'niveau',
                    "nb_seance_distance",
                    "nb_seance_physique",
                    )

    list_filter = ('theme',
                   'publique',
                   'niveau',
                   'annimateur_possible'
                   )

    search_fields = ('titre',
                     'theme__titre',
                     'publique__titre',
                     'niveau__titre',
                     "nb_seance_distance",
                     "nb_seance_physique",
                     'annimateur_possible__nom',
                     "objectif",
                     'point_abordes',
                     )
    readonly_fields = ('admin_photo',)


admin.site.register(ImageGalerie, ImageGalerieAdmin)

admin.site.register(Atelier, AtelierAdmin)
