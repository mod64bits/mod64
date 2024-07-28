from django.contrib import admin
from django.urls import path, include
from apps.produtos import urls as produtos_urls

urlpatterns = [
    path('produtos/', include(produtos_urls)),
    path('admin/', admin.site.urls),
]
