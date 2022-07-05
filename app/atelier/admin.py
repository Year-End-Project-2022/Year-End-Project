from django.contrib import admin
from .models import Atelier, Niveau, Publique, Seance, Theme, Session


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

class SessionAdmin(admin.StackedInline):
    model = Session
    extra = 1
    


@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    inlines = [SessionAdmin]
    list_display = ('titre','nb_incrit','atelier','liste_des_dates')
    list_filter = ('atelier__titre',)
    search_fields = ('titre','atelier__titre',)
    
    def liste_des_dates(self, obj):
        return ", ".join([str(x) for x in SessionAdmin.model.objects.filter(seance=obj).values_list('date', flat=True)])



@admin.register(Atelier)
class AtelierAdmin(admin.ModelAdmin):
    list_display = ('admin_photo',
                    'titre',
                    'theme',
                    'publique',
                    'niveau',
                    "nb_seance_distance",
                    "nb_seance_physique",
                    "nb_presonne_interesse",
                    "publier",)

    list_filter = ('theme',
                   'publique',
                   'niveau',
                   'annimateur_possible',
                   'publier',)

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