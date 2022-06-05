from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Profile,InstagramPost
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    current_user = request.user.profile
    images = InstagramPost.objects.all()
    profiles = Profile.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,
        'profiles': profiles,
    }
    return render(request, 'index.html',params)


