from django.conf.urls import url
from django.urls import include
from updates.views import (
    json_example_view,
    JsonCBV,
    JsonCBV2,
    SerializedListView,
    SerializedDetailView,
)


urlpatterns = [
    url(r'^$', json_example_view),
    url(r'example/', json_example_view),
    url(r'cbv/', JsonCBV.as_view()),
    url(r'cbv2/', JsonCBV2.as_view()),
    url(r'serialize/', SerializedListView.as_view()),
    url(r'serialize-detail/', SerializedDetailView.as_view())
]
