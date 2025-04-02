from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/',CreateUserView.as_view(), name='register'),
    path('api/token/',TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh',TokenRefreshView.as_view(), name='token-refresh'),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
