from django.contrib import admin
from django.contrib.auth.models import Group
from userauth.models import userAccount
# Register your models here.
admin.site.unregister(Group)

class AccountAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'phone', 'is_staff']
admin.site.register(userAccount, AccountAdmin)