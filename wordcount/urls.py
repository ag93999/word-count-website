from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # ex: admin/
    path('admin/', admin.site.urls),
    # ex: home/
    path('home/', views.homepage, name='home'),
    path('', views.about, name='about'),
    # ex: count/
    path('count/', views.count, name='count'),
]
