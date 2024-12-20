# Generated by Django 5.1.1 on 2024-10-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(max_length=50)),
                ('emailid', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'blog_users',
                'managed': True,
            },
        ),
    ]
