from django.contrib import admin
from .models import Categories, Groupe, Media, Outils


class OutilsAdmin(admin.ModelAdmin):
    list_display = ('nom_func',
                    'nombre',
                    'nombre_hs',
                    'groupe'
                    )

    list_filter = ('categories',
                   'groupe',
                   'taille',
                   'marque',
                   )

    search_fields = ('nom',
                     'type',
                     'taille',
                     'categories__title',
                     'nombre',
                     'nombre_hs',
                     'groupe__nom',
                     'commentaire',
                     )


admin.site.register(Outils, OutilsAdmin)
admin.site.register(Categories)
admin.site.register(Media)
admin.site.register(Groupe)
