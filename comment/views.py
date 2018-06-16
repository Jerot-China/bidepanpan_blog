from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from blog.models import Post
from .forms import CommentForm


# Create your views here.
def post_comment(request, post_pk):
    # 先获取被评论的文章，post_pk是id，post为获取的文章名称
    post = get_object_or_404(Post, pk=post_pk)

    # 判断请求为post类型
    if request.method == 'POST':
        # 提交的数据在request.post中
        # 我们利用这些数据构造了CommentForm实例
        form = CommentForm(request.POST)
        # 当调用 xxx.is_valid()方法时，django自动帮我们检查表单数据是否符合规则
        if form.is_valid():
            # 调用表单的save方法将数据存储进数据库
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = post
            comment.save()
            # 重定向至post的详情页，redirect函数接受模型时，会调用这个模型的 get_absolute_url方法
            return redirect(post)
        else:
            # 检测到语句不合法
            # 因此传了三个模板变量给detail.html
            # 一个文章 一个是评论列表 一个是表单
            # 然后使用 comment.set_all()方法
            # 作用是获取post下的全部评论
            comment_list = comment.set_all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)




