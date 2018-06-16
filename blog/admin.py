from django.contrib import admin
from .models import Category, Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'end_time', 'category', 'author']


# 在127.0.0.1:8000/admin页面中增加对应名称的模型
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)




