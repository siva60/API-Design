from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from status.api.views import (
    StatusAPIView,
    StatusAPIDetailView,
)


urlpatterns = [
    # r'^(?P<id>.*)/delete/$' takes any input entered, replace .* with \d+ to take only digit input
    url(r'auth/jwt/$', obtain_jwt_token),
    url(r'auth/jwt/refresh/$', refresh_jwt_token),
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
]


# status/  -> List
# status/create/  -> create
# status/<id>/ -> detail
# status/<id>/update/  -> update
# status/<id>/delete/  -> delete


# http://127.0.0.1:8000/status/20/

# http://127.0.0.1:8000/status/

# http://127.0.0.1:8000/status/?q=method
