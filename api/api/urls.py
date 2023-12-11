from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from app.views import UserViewSet
router=routers.DefaultRouter()
router.register(r'user',UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls))
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

