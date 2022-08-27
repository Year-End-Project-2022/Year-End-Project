from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponseRedirect
from .models import Categories, Groupe, Media, Outils
from django.contrib.contenttypes.models import ContentType
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, get_object_or_404
 

class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories

class MediaResource(resources.ModelResource):
    class Meta:
        model = Media
        
class OutilsResource(resources.ModelResource):
    class Meta:
        model = Outils

class GroupeResource(resources.ModelResource):
    class Meta:
        model = Groupe

class CategoriesAdmin(ImportExportModelAdmin):
    resource_class = CategoriesResource



class OutilsAdmin(ImportExportModelAdmin):
    resource_class = OutilsResource
    actions = ['pdf_export']
    @admin.action(description='Exporter les outils selectionnés en PDF')
    def pdf_export(modelAdmin, request, queryset):
        selected = queryset.values_list('id', flat=True)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect('/export/%s/' % (
            ','.join(str(id) for id in selected),
        ))



class MediaAdmin(ImportExportModelAdmin):
    resource_class = MediaResource



class GroupeAdmin(ImportExportModelAdmin):
    resource_class = GroupeResource


class OutilsAdmin(ImportExportModelAdmin):
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
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Groupe, GroupeAdmin)

