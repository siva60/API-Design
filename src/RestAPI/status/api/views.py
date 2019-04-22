# TWO ENDPOINTS FOR ALL REQUESTS

from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from status.models import Status
from rest_framework.authentication import SessionAuthentication

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from status.api.serializers import StatusSerializer
import json


# from django.views.generic import View         # This is regular generic API View


# this method just returns a boolean value and checks if the entered value is actual json.
def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


# [PUT, RETRIEVE, DELETE]
class StatusAPIDetailView(mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ensures logged in
    serializer_class = StatusSerializer
    queryset = Status.object.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=serializer.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None


# [POST, RETRIEVE]
class StatusAPIView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ensures logged in
    serializer_class = StatusSerializer
    passed_id = None  # passed id on that instance itself.

    def get_queryset(self):
        request = self.request
        # print(request.user)
        qs = Status.object.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # this method maintain the user session. When posted data this keeps track of user.
    # gives permission error
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

