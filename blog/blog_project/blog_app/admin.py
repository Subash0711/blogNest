from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.BlogLists)
class BlogList(admin.ModelAdmin):
    list_display = ("blog_id", "blog_title","isUpdate", "isDelete","created_at")


@admin.register(models.BlogUserComments)
class UserComments(admin.ModelAdmin):
    list_display = ['cmt_id','blog__blog_id','user__emailid']




@admin.register(models.BlogUsersLikes)
class BlogsLikes(admin.ModelAdmin):
    list_display=["like_blog__blog_id","like_blog__blog_title","total_likes"]

    def total_likes(self,obj):
        return models.BlogUsersLikes.objects.filter(like_blog=obj.like_blog).count()
    total_likes.short_description = "Total Likes"