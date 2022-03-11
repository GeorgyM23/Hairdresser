from django.urls import path
from . import views

urlpatterns = [
    path('', views.writing_home, name="writing_home"),
    path('/last', views.last, name="last"),
]