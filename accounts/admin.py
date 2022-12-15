from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('name', 'last_name', 'username', 'email', 'date_joined', 'is_active')
    list_display_links = ('username', 'email')
    readonly_fields = ('date_joined', 'last_login', 'password')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)