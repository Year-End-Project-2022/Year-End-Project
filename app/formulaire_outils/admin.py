from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Categories, Groupe, Media, Outils


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

admin.site.register(Categories, CategoriesAdmin)

class OutilsAdmin(ImportExportModelAdmin):
    resource_class = OutilsResource

admin.site.register(Outils, OutilsAdmin)

class MediaAdmin(ImportExportModelAdmin):
    resource_class = MediaResource

admin.site.register(Media, MediaAdmin)

class GroupeAdmin(ImportExportModelAdmin):
    resource_class = GroupeResource

admin.site.register(Groupe, GroupeAdmin)