from django.urls import path
from . import views

urlpatterns = [
  path('dash/', views.get_recommendations, name='get_recommendations')
]