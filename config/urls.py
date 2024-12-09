from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('catalog/', include('catalog.urls', namespace='catalogs')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
