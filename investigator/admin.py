from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'wxAccounts', 'wxName','account','passWord','role','name','img','gender','identity',
                    'bankCard','station','telephone','isValid']

admin.site.register(User, UserAdmin)

