# Generated by Django 3.0.2 on 2020-05-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20200505_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindata',
            name='Status',
            field=models.TextField(default='not paid'),
        ),
    ]