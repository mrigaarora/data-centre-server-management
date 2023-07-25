from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin



class RacksAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =['id', 'Rack']

class CompanyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['company']

class ServerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = [field.name for field in Server._meta.get_fields()]
    search_fields = ('server_serial_no', 'server_make', 'server_model', 'rack_no')
    list_filter = ('server_make', 'rack_no')



# Register your models here
admin.site.register(Rack, RacksAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Server,ServerAdmin)