# Generated by Django 4.2.5 on 2023-10-04 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_of_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_of_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]