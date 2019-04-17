from django.conf.urls import url
from api.views import (
    UpdateModelDetailAPIView, UpdateModelListAPIView
)


urlpatterns = [
    url(r'^$', UpdateModelListAPIView.as_view()), # List, Create
    # Take input only digits
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()),

]
