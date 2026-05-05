from django.urls import path
from . import views

urlpatterns = [
  path('add_sale/', views.add_sale, name='add_sale')
]