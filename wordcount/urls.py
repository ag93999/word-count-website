from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name='home'),
    path('', views.about, name='about'),
    path('count/', views.count, name='count'),
]
