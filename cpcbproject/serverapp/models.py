from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedManyToManyField,ChainedForeignKey
import os



# Create your models here.
class Rack(models.Model):
    Rack=models.CharField(max_length=100)
    def __str__(self):
        return self.Rack

class Company(models.Model):
    company=models.CharField(max_length=100)
    racks = models.ManyToManyField(Rack,related_name='companies')
    
    def __str__(self):
        return self.company
    
   
class OwnershipChoice(models.Model):
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name
    
def validate_excel_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xlsx', '.xls', '.xlsm']
    if ext.lower() not in valid_extensions:
        raise ValidationError("Only Excel files with extensions .xlsx, .xls, or .xlsm are allowed.")
    
class Server(models.Model):
    rack_no = models.ForeignKey(Rack, on_delete=models.CASCADE)
    server_make = models.ForeignKey(Company, on_delete=models.CASCADE)
    server_model = models.CharField(max_length=100, unique=True)
    server_serial_no = models.CharField(max_length=100, unique=True)
    ownership = models.ForeignKey(OwnershipChoice, on_delete=models.CASCADE)
    warranty_amc_status = models.CharField(max_length=100)
    vms = models.BooleanField(default=False)
    num_of_vms = models.IntegerField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(unique=True)
    public_ip = models.GenericIPAddressField(null=True, blank=True, unique=True)
    applications_installed = models.TextField()
    portals_running = models.TextField(null=True, blank=True)
    specification = models.TextField(null=True, blank=True)
    vm_information_file = models.FileField(
        upload_to='server_vms/',
        null=True,
        blank=True,
        validators=[validate_excel_file_extension]
    )

    def __str__(self):
        return f"Server {self.server_serial_no} - {self.rack_no} {self.server_make} {self.server_model}"
    
    def save(self, *args, **kwargs):
        # Set num_of_vms to None if vms is False
        if not self.vms:
            self.num_of_vms = None

        super().save(*args, **kwargs)

    def clean(self):
        # Ensure num_of_vms is None if vms is False
        if not self.vms and self.num_of_vms is not None:
            raise ValidationError("Number of VMs should only be specified when VMs is selected.")
        if self.vms and not self.vm_information_file:
            raise ValidationError("Please upload the Excel file with VM information.")