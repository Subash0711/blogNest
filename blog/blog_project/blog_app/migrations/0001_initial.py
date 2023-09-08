# Generated by Django 5.1.1 on 2024-10-05 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogLists',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.TextField(blank=True, null=True)),
                ('blog_content', models.TextField(blank=True, null=True)),
                ('isUpdate', models.BooleanField(blank=True, default=False, null=True)),
                ('isDelete', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('userid', models.ForeignKey(blank=True, db_column='userid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.blogusers')),
            ],
            options={
                'db_table': 'blog_lists',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BlogUserComments',
            fields=[
                ('cmt_id', models.AutoField(primary_key=True, serialize=False)),
                ('cmt_content', models.TextField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('isUpdate', models.BooleanField(blank=True, default=False, null=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.bloglists')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.blogusers')),
            ],
            options={
                'db_table': 'blog_user_comments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BlogUsersLikes',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('isLike', models.BooleanField(blank=True, null=True)),
                ('like_blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.bloglists')),
                ('like_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.blogusers')),
            ],
            options={
                'db_table': 'blog_users_likes',
                'managed': True,
            },
        ),
    ]
