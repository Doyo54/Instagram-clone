from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404
from .forms import PostForm,UpdateUserProfileForm,CommentForm
from .models import Profile,InstagramPost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
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
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    loops = {
        'images': images,
        'form': form,
        'users': users,
        'profiles': profiles,
    }
    return render(request, 'index.html',loops)


def search_profile(request):
    if 'search' in request.GET and request.GET['search']:
        name = request.GET.get("search")
        results = Profile.search_profile(name)
        message = f'name'
        loops = {
            'results': results,
            'message': message
        }
        return render(request, 'search_results.html', loops)
    else:
        message = "You haven't searched for any User"
    return render(request, 'search_results.html', {'message': message})

def profile(request, username):
        user_prof = InstagramPost.get_Profile(username)
        if request.user == user_prof:
           return redirect('update_profile', username=request.user.username)
      
        return render(request, 'user_profile.html', {'user_prof': user_prof,})

def update_profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
  
    return render(request, 'profile.html', {'prof_form': prof_form,'images': images,})


def post_comment(request, id):
    image = get_object_or_404(InstagramPost, pk=id)
  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, 'comment.html', { 'image': image,'form': form,})





