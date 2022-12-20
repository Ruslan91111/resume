from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from . import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('movies.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls

# router = SimpleRouter()
# router.register(r'movie', MovieViewSet)
# urlpatterns += router.urls