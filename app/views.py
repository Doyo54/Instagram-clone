from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'django_registration/registration_form.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
        return redirect('index')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
    context = {'form': form}
    return render(request, 'django_registration/registration_form.html', context)

