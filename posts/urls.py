from django.urls import path
from posts import views


urlpatterns = [
    path('list/', views.list_posts),
]
