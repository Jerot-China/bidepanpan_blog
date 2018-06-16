from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    # auto_now_add的作用是，当插入一条数据进数据库时自动将当前时间填入这个字段中
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.post')

    def __str__(self):
        return self.text[:20]

