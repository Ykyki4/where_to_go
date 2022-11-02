from django.contrib import admin
from django.urls import path
from places import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('place/<int:place_id>/', views.get_place)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
