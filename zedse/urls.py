from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='arab'),
    path('begin/', views.begin, name='beginer'),
    path('frnds/', views.frnds, name='friends')

]

