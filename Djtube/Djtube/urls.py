from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('', include('users.urls'), name='users'),
    path('', include('social.apps.django_app.urls'), name='social'),
    path('posts/', include('posts.urls'), name='posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
