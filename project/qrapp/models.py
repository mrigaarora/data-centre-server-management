from django.db import models

# Create your models here.
class Table(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Rack=models.CharField(max_length=100)
   
