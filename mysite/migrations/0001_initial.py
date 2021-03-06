# Generated by Django 3.0.2 on 2020-05-05 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discription', models.CharField(choices=[('Bf', 'Bf'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Lunch-Dinner', 'Lunch-Dinner'), ('BF-Lunch-Dinner', 'BF-Lunch-Dinner')], max_length=256)),
                ('Dateed', models.DateField()),
                ('Amount', models.FloatField()),
                ('Status', models.BooleanField(default=True)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
