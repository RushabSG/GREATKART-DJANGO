from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'username', 'last_login', 'is_active')
    list_display_links = ('email','first_name')
    readonly_fields = ("last_login", "date_joined")
    fieldsets = ()
    list_filter = ()
    filter_horizontal = ()

admin.site.register(Account, AccountAdmin)
