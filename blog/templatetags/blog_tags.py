from ..models import Post
from ..models import Category
from django import template

# 实例化template.Library
register = template.Library()


# 通过装饰器将函数get_recent_posts装饰为register.simple_tag
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


# dates返回一个传递参数的列表，并且是Python的date对象
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
