from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
import markdown
from comment.forms import CommentForm


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/detail.html', context=context)


def archives(request, month, year):
    # create_time是python的date对象，包含了year和month两个值，应该用create_moth或者create_year，但是这里作为函数列表django需要我们使用两个下划线‘__‘来代替
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month,
                                    ).order_by('-create_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
