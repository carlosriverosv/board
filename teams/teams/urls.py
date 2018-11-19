"""teams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_view
from django.urls import path, include
from accounts import views as acc_vi


urlpatterns = [
    path('', acc_vi.home, name='home'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),
    path('signup/', acc_vi.signup, name='signup'),
]
