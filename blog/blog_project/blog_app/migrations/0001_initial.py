# Generated by Django 4.2.2 on 2023-08-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogLists',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.TextField(blank=True, null=True)),
                ('blog_content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'blog_lists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BlogUserComments',
            fields=[
                ('cmt_id', models.AutoField(primary_key=True, serialize=False)),
                ('cmt_content', models.TextField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_comments',
                'managed': False,
            },
        ),
    ]
