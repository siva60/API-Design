from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from accounts.api.views import AuthView

urlpatterns = [
    url(r'^$', AuthView.as_view()),
    url(r'^auth/jwt/$', obtain_jwt_token),
    url(r'^auth/jwt/refresh/$', refresh_jwt_token),
]
