from django.urls import path
from . import views
from .views import add_movie

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/add_review/', views.add_review, name='add_review'),
    path('add_movie/', add_movie, name='add_movie'),
    path('update_movie/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),


]


