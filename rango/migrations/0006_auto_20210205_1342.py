# Generated by Django 2.2.17 on 2021-02-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
