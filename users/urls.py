from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path(
        'profile/<str:username>/',
        views.UserProfile.as_view(),
        name='profile'
    ),
    path('update_profile/', views.update_profile, name='update_profile'),
]
