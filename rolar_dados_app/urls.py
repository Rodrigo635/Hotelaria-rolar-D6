from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roll_dice/', views.roll_dice, name='roll_dice'),
]
