from django.conf.urls import url
from django.urls import path

from . import views

# Namespace and URL
app_name = 'event'
urlpatterns = [
    url(r'gen', views.createRandomEvent, name='gen'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DisplayView.as_view(), name='display'),
    path('new', views.EventNew.as_view(), name='new'),
    path('<int:pk>/edit', views.EventUpdate.as_view(), name='edit'),
    path('<int:pk>/resolve', views.EventDelete.as_view(), name='delete'),
]
