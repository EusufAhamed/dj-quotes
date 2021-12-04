from django.urls import path
from quotes_app import views

urlpatterns = [
    path('', views.quotes_view, name='quotes_view'),
]