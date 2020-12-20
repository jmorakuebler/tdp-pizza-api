from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from users import views


app_name = 'users'

urlpatterns = [
    path('drf-token/', views.CreateDRFTokenView.as_view(), name='drf-token'),
    path(
        'jwt-token/', jwt_views.TokenObtainPairView.as_view(), name='jwt-token'
    ),
    path(
        'jwt-token/refresh/', jwt_views.TokenRefreshView.as_view(),
        name='jwt-token-refresh'
    ),
]
