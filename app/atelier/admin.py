from django.contrib import admin
from .models import Atelier, Niveau, Publique, Seance, Theme


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

@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    list_display = ('atelier',)
    list_filter = ('atelier__titre',)
    search_fields = ('atelier__titre', 'dates__date',)
    
@admin.register(Atelier)
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