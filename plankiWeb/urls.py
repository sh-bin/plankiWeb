from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url for admin panel
    path('admin/', admin.site.urls),

    # url for home page
    path('', include('plankiHomePage.urls')),
]

if settings.DEBUG:
    # For 'Debug Toolbar'
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
