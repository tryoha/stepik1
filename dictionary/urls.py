from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index),
    path('words_list/', views.wordslist, name='words_list'),
    path('add_word/', views.add_word, name='add_word'),
]
