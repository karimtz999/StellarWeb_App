from django.urls import path
from . import views

urlpatterns = [
    # Define your blog URL patterns here
    path('', views.blog_home, name='blog_home'),  # Example URL pattern
]
