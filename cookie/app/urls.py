from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,),
    path('home/',views.home,name='home'),
    path('login/',views.login),
    path('singup/',views.singup),
    path('savedata/',views.savedata ,name='savedata'),
    path('register/',views.register,name='register'),
    path('dashbord/',views.dashbord,name='dashbord'),
    path('product/',views.product),
    path('about/',views.about),
    path('award/',views.award),
    path('contact/',views.contact),
    path('logout/',views.logout),
]

