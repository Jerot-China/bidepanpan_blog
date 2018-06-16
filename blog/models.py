from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=200)
    # 文章正文
    body = models.TextField()
    # 开始结束时间分别用DataTime
    create_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # 文章摘要，当有参数 blank=True 就可以输入空值了
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类和标题
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    # 作者 django.contrib.auto是django的内置应用，采用一对多的关系
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        # blog:detail 是因为在urls中配置的name='detail'派上了用场，意思是blog下的detail函数
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
