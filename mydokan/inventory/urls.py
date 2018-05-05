from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', home , name = 'home'),
    path('category/<name>', category_views, name = 'category_views'),
    path('product/<int:id>', single_page_views, name = 'single_page_views'),
    path('cart/<int:id>', add_cart_views, name = 'add_cart_views'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
