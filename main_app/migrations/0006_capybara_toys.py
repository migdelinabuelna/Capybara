# Generated by Django 4.1.7 on 2023-04-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_capybara_toys'),
    ]

    operations = [
        migrations.AddField(
            model_name='capybara',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
