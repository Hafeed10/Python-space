from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the Django admin interface
    path("", include(("space1.urls"), namespace="space1")),  # Includes URLs from the app 'pathc2'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
