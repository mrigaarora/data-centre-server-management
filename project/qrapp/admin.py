from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin

class ViewAdmin(ImportExportModelAdmin):
    pass

class TablesAdmin(admin.ModelAdmin):
    list_display =['id', 'Rack']

# Register your models here
admin.site.register(Table, TablesAdmin)