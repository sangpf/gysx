# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['invId', 'title', 'summary', 'client', 'responsibility',
                    'comment', 'type', 'status', 'cTime', 'bTime', 'eTime']

admin.site.register(Project,ProjectAdmin)

