from django.urls import path
from userauth.views import register_view,CustomAuthToken

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/register', register_view, name='register'),
    # path('api/login', CustomAuthToken.as_view(), name='login')
]