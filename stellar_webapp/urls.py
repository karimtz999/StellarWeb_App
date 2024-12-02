from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Main app
    path('accounts/', include('accounts.urls')),  # User authentication
    path('api/', include('api.urls')),  # API routes
    path('blog/', include('blog.urls')),  # Optional
]
