# Generated by Django 4.1.2 on 2023-07-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0003_alter_server_server_make'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='vm_information_file',
            field=models.FileField(blank=True, null=True, upload_to='server_vms/'),
        ),
    ]
