from django.urls import path
from . import views

urlpatterns = [
  path('dash/', views.get_recommendations, name='get_recommendations'),
  path('debt/', views.debt, name='debt'),
  path('inventory-alerts/', views.inventory_alerts, name='inventory_alerts'),
  path('today/', views.Today, name='today'),
  path('sales-comparison/', views.sales_comparison, name='sales_comparison'),
]