from django.shortcuts import render
import json
from django.views.generic import View

from django.http import JsonResponse, HttpResponse
from updates.models import Update
from updates.mixings import JSONResponseMixin

from django.core.serializers import serialize


def json_example_view(request):
    """

    GET -- retrieve data
    :param request:
    :return:
    """
    data = {
        "count": 1000,
        "content": "Some Content"
    }

    json_data = json.dumps(data)
    return JsonResponse(data)


# Using Class based View
class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some Content"
        }
        return JsonResponse(data)


class JsonCBV2(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some Content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=2)
        json_data = obj.serialize()
        # data = serialize("json", [obj, ], fields=('user', 'content',))
        # json_data = data
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        # qs = Update.objects.all()
        json_data = Update.objects.all().serialize()
        # data = serialize("json", qs, fields=('user', 'content',))
        # print(data)
        # json_data = data
        return HttpResponse(json_data, content_type='application/json')
