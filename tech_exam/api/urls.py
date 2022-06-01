from django.urls import path
from . import views


urlpatterns = [
    path('',views.get_stocks),
    path('add_stock/',views.add_stock),
    path('place_order/',views.place_order),
    path('show_orders/',views.show_orders),
    path('total_investment/',views.total_invested),
]