from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('token-auth/refresh', refresh_jwt_token),
    path('account/', include('account.urls')),
    path('ethics_app/', include('ethics_app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
