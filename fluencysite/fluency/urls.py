from django.urls import path
from . import views


urlpatterns =[
path('<str:categoryname>', views.index, name='index'),
path('', views.home, name='home'),
path('flashcard/', views.flashcard, name='flashcard'),
]