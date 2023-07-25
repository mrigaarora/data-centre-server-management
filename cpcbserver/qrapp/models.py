from django.db import models

# Create your models here.
class Rack(models.Model):
    Rack=models.CharField(max_length=100)

class Company(models.Model):
    company=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.company

class Server(models.Model):
    rack_no = models.IntegerField()
    server_make = models.ForeignKey(Company, on_delete=models.CASCADE)
    server_model = models.CharField(max_length=100)
    server_serial_no = models.CharField(max_length=100)
    ownership = models.CharField(max_length=100)
    warranty_amc_status = models.CharField(max_length=100)
    vms = models.BooleanField()
    num_of_vms = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    public_ip = models.GenericIPAddressField(null=True, blank=True)
    applications_running = models.TextField()
    specification = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Server {self.server_serial_no} - {self.server_make} {self.server_model}"
