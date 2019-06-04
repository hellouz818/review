"""reviewproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import diaryapp.views
import userapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userapp.views.base, name = "base"),

    path('main/', diaryapp.views.main, name = "main"),
    path('new/', diaryapp.views.new, name = "new"),
    path('postcreate/', diaryapp.views.postcreate, name = "postcreate"),
    path('show/<int:post_id>', diaryapp.views.show, name='show'),
    path('edit/', diaryapp.views.edit, name='edit'),
    path('postupdate/<int:post_id>', diaryapp.views.postupdate, name='postupdate'),
    path('postdelete/<int:post_id>', diaryapp.views.postdelete, name='postdelete'),



    path('home/', userapp.views.home, name = "home"),
    path('signup/', userapp.views.signup, name="signup"),
    path('login/', userapp.views.login, name="login"),
    path('logout/', userapp.views.logout, name="logout"),
    

]
