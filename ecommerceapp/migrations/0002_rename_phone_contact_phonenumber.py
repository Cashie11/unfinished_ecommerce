# Generated by Django 4.2.2 on 2023-06-28 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='phonenumber',
        ),
    ]
