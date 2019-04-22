# ONE ENDPOINT FOR ALL REQUESTS.

from rest_framework.views import APIView
from rest_framework import generics, mixins
from status.models import Status
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


# One Endpoint for all CRUD operations.
class StatusAPIView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    passed_id = None         # passed id on that instance itself.

    def get_queryset(self):
        qs = Status.object.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passes_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passes_id or None
        self.passed_id = passed_id    # this make sure if passes id is None it will take the default.

        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passes_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passes_id or None
        self.passed_id = passed_id  # this make sure if passes id is None it will take the default.

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passes_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passes_id or None
        self.passed_id = passed_id  # this make sure if passes id is None it will take the default.

        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passes_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passes_id or None
        self.passed_id = passed_id  # this make sure if passes id is None it will take the default.

        return self.destroy(request, *args, **kwargs)




# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request):
#         qs = Status.object.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         qs = Status.object.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#
# # StatusAPIView is more advanced View than above class. It derives the
# # properties from rest_framework generics ListAPIView.
# # get_queryset method narrows down our search based on filter. If the qs filtered is none,
# # it returns the first query giving all results.
# # http://127.0.0.1:8000/status/?q=method. This searches the content that contain 'method' string.
#
# # post method is based on mixing.CreateModelMixin can also handle post requests.
#
# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     # [Create, GET]
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.object.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# # StatusCreateAPI View allows us to post the data deriving inbuilt CreateAPIView from generics.
# class StatusCreateAPIView(generics.CreateAPIView):
#     # [create]
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.object.all()
#     serializer_class = StatusSerializer
#
#
# # StatusDetailAPI View allows us to narrow down our search based on pk or id.
#
# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     # [Retrieve based on id, Update, delete]
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.object.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'        # the string 'id' must match with the parameter in url.py
#
#     '''
#     # Or Instead of Using the lookup_field above custom function is used.
#     def get_object(self, *args, **kwargs):
#         kwargs = self.kwargs
#         kw_id = kwargs.get('id')
#         return Status.object.get(id=kw_id)
#     '''
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# # StatusUpdateAPI View allows us update the item based on the 'id' entered in url.
# class StatusUpdateAPIView(generics.UpdateAPIView):
#     # [update]
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.object.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'        # the string 'id' must match with the parameter in url.py
#
#
# # StatusDeleteAPI view allows us to delete the data based on the 'id'
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     # [delete]
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.object.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'        # the string 'id' must match with the parameter in url.py
#

