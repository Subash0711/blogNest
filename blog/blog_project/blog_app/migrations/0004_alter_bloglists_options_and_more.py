# Generated by Django 4.2.2 on 2023-09-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_bloguserslikes_alter_blogusercomments_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloglists',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='blogusercomments',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='bloguserslikes',
            options={'managed': True},
        ),
    ]
