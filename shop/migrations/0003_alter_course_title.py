# Generated by Django 4.2.5 on 2023-10-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
