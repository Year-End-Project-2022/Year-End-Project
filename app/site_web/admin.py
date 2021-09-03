from django.contrib import admin
from .models import ImageGalerie, Atelier, Niveau, PersonneDispo, Publique, Theme

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


admin.site.register(ImageGalerie)

admin.site.register(Atelier)
