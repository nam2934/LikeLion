from django import forms
from .models import Post
from .models import Tag
ㅑ
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

