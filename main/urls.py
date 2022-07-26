from django.urls import path
from . import views

# urls for app main
urlpatterns = [
    path('', views.homepage, name='home')
]