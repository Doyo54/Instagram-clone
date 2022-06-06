from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from .forms import PostForm,UpdateUserProfileForm
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
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,
        'profiles': profiles,
    }
    return render(request, 'index.html',params)


def search_profile(request):
    if 'search' in request.GET and request.GET['search']:
        name = request.GET.get("search")
        results = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search_results.html', params)
    else:
        message = "You haven't searched for any User"
    return render(request, 'search_results.html', {'message': message})

def profile(request, username):
        user_prof = InstagramPost.get_Profile(username)
        if request.user == user_prof:
           return redirect('update_profile', username=request.user.username)
      
    
        params = {
        'user_prof': user_prof,
       
         }

        return render(request, 'user_profile.html', params)







