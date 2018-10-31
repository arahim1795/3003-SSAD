from django.conf.urls import url
from . import views

urlpatterns = [
    # /CMO/
    url(r'^$',views.index, name = 'index'),

    # /CMO//12/
    url(r'^(?P<operator_id>[0-9]+)/$',views.detail,name='detail'),
]