from django.urls import path
from posts import views


urlpatterns = [
    path('list/', views.list_posts, name='posts_list'),
    path('new/', views.new_post, name='new_post'),
]
