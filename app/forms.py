from django import forms
from .models import InstagramPost

class PostForm(forms.ModelForm):
    class Meta:
        model = InstagramPost
        fields = ('image', 'description')

