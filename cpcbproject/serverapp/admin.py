from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from . forms import ServerForm



class RacksAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =['id', 'Rack']

class CompanyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','company','display_racks']

    def display_racks(self, obj):
        return ', '.join([rack.Rack for rack in obj.racks.all()])

    display_racks.short_description = 'Racks'

class ServerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    form = ServerForm
    list_display = (
        'id',
        'rack_no',
        'server_make',
        'server_model',
        'server_serial_no',
        'ownership',
        'warranty_amc_status',
        'vms',
        'num_of_vms',
        'vm_information_file',
        'ip_address',
        'public_ip',
        'portals_running',
        'specification',
    )
   
    list_filter = ('server_make', 'rack_no')

class OwnershipChoiceAdmin(admin.ModelAdmin):
    list_display = ('id','display_name')

admin.site.register(Rack, RacksAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Server,ServerAdmin)
admin.site.register(OwnershipChoice,OwnershipChoiceAdmin)

