from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm
from .models import Profile,InstagramPost
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    current_user = request.user.profile
    images = InstagramPost.objects.all()
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

    }
    return render(request, 'index.html',params)

# def register(request):
#     if request.method == 'GET':
#         form  = RegisterForm()
#         context = {'form': form}
#         return render(request, 'django_registration/registration_form.html', context)
#     if request.method == 'POST':
#         form  = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#         return redirect('index')
#     else:
#         print('Form is not valid')
#         messages.error(request, 'Error Processing Your Request')
#     context = {'form': form}
#     return render(request, 'django_registration/registration_form.html', context)

