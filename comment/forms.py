from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # 指定表单的数据模型时comment
        model = Comment
        # fields 为传输的参数
        fields = ['name', 'email', 'url', 'text']
