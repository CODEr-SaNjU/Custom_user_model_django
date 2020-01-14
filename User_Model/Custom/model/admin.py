from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import InfoCreationForm, InfoChangeForm
from .models import Info



class InfoAdmin(UserAdmin):
    add_form = InfoCreationForm
    form = InfoChangeForm
    model = Info

    list_display = ("email",'username','is_staff','is_active','is_superuser','is_admin')
    list_filter = ('email','is_staff','is_active')
    fieldsets = (
        (None, {
            "fields": (
                'email','password','username'
            ),
        }),
        ('Permissions',{'fields':('is_staff','is_active','is_superuser')}),
    )
    add_fieldsets = (
        (None ,{
            'classes':('wide',),
            'fields':('username','email','password1','password2','is_staff','is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Info,InfoAdmin)
admin.site.unregister(Group)
