# Generated by Django 4.1.8 on 2023-04-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_report', '0002_alter_disaster_report_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster_report',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media/disaster_images/'),
        ),
    ]
