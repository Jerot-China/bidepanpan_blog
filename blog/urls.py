from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # (?P<pk>[0-9]+)是命名捕获组，其作用是从用户访问的 URL 里把括号内匹配的字符串捕获并作为关键字参数传给其对应的视图函数 detail
    url(r'^post/pk=(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]
