# Generated by Django 4.1.7 on 2023-04-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding date'),
        ),
    ]