from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

# Namespace and URL
app_name = 'account'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
