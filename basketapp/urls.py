from django.urls import re_path
from basketapp import views as basketapp
from .apps import BasketappConfig

app_name = 'basketapp'

urlpatterns = [
    re_path(r"^$", basketapp.basket, name="view"),
    re_path(r"^add/(?P<pk>\d+)/$", basketapp.add, name="add"),
    re_path(r"^remove/(?P<pk>\d+)/$", basketapp.delete, name="remove"),
    re_path(r"^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$", basketapp.edit, name="edit"),
]

