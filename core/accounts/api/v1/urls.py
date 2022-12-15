from django.urls import path , include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name='api-v1'


urlpatterns = [
    path('register/',views.RegestrationsApiView.as_view(),name='registerapiview'),
    path('token/login/',views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.RevortToken.as_view(),name='token-logout'),

    #JWT
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('profile/',views.UserProfile.as_view(),name='user-profile'),

    path('sendmail/',views.SendEmail.as_view(),name='send_email'),

    path('active/token/<str:token>/',views.ActivationsApiView.as_view(),name='token_activate'),
    path("activation/resend/",views.ResendVerfications.as_view(),name="activation-resend"),
]
