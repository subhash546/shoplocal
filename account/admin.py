from django.contrib import admin
from .models import Account

from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'last_login',
        'date_joined'
    )
    list_display_links=('email','username',)
    ordering = ('email',)
    

    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
    )

    add_fieldsets = (
    
    )
    filter_horizontal=()
    list_filter=()

# Register your models here.
admin.site.register(Account,UserModel)

