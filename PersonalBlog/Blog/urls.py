from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_post/', views.newPost, name = "new_post" )
]