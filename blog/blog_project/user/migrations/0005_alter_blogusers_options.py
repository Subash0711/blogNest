# Generated by Django 4.2.2 on 2023-09-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_blogusers_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogusers',
            options={'managed': True},
        ),
    ]
