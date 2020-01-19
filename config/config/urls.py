"""config URL Configuration

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
from diary.views import list, read, create, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', list, name='articles-list'),
    path('articles/<int:pk>/', read, name='articles-read'),
    path('articles/create/', create, name='articles-create'),
    path('articles/update/<int:pk>', update, name='articles-update'),
    path('articles/delete/<int:pk>', delete, name='articles-delete'),
]
