from django import forms
from .models import InstagramPost,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = InstagramPost
        fields = ('image', 'description')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio']

