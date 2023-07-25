# Generated by Django 4.1.2 on 2023-06-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0006_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='Company',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='server',
            name='specification',
            field=models.TextField(blank=True, null=True),
        ),
    ]