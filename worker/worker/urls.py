"""
URL configuration for worker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('show/',views.show,name='show'),
     path('save/',views.save,name='save'),
     path('cse/',views.cse,name='cse'),
     path('main/',views.main,name='main'),
     path('history/',views.history,name='history'),
     path('login/',views.login,name='login'),
     path('signup/',views.Signup,name='signup'),
     path('query/',views.query,name='query'),
      path('view/',views.view,name='view'),
      path('delete/<id>',views.delete,name='delete'),
     path('Logout/',views.Logout,name='logout'),
     path('CIVIL/',views.CIVIL,name='CIVIL'),
]
