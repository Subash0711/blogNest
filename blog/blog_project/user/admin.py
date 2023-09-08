from django.contrib import admin
from user.models import (BlogUsers)

# Register your models here.

@admin.register(BlogUsers)
class Users(admin.ModelAdmin):
    list_display = ("id", "fullname", "emailid")