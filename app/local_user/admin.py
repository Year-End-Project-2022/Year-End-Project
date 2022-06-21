from django.contrib import admin

from .models import LocalUser

# Register your models here.

class LocalUserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'email',
                    'first_name',
                    'last_name',
                    'is_staff'
                    )
    
    list_filter = ('is_staff',
                   'is_superuser',
                   'is_active',
                   'groups'
                   )

    search_fields = ('username',
                     'email',
                     'first_name',
                     'last_name'
                     )

admin.site.register(LocalUser, LocalUserAdmin)