"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import re_path,include
from django.contrib.auth import views as view
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('django_registration.backends.one_step.urls'), name='register'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/login', view.LoginView.as_view(template_name='registration/login.html'), name ='login'), 
    re_path(r'^logout/$', view.LogoutView.as_view(next_page='login')), 
    re_path(r'',include('app.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
