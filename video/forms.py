from django import forms
from video.models import Post

class CreatePostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields = ['title','video','image','tanctipus','hely','datum','tancos']
