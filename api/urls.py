from django.urls import path
from . import views

urlpatterns = [
    # Define your API URL patterns here
    path('', views.api_home, name='api_home'),  # Example URL pattern
] 