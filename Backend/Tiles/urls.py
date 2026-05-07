from django.urls import path
from . import views

urlpatterns = [
  path('add_tile/', views.add_tile_design, name='add_tile'),
  path('get_tile/', views.get_tile_design, name='get_tiles')
]