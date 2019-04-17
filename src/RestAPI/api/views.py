from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
import json
from api.mixings import CSRFExemptMixin
from updates.mixings import HttpResponseMixin
from api.forms import UpdateModelForm


# # Data is already serialized in models.py so no need JSONResponse
# Creating, updating, retrieving, deleting, model (1)


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    Retrieve, Update, delete --> object
    """
    is_json = True

    # get_object method applied to all other methods that need to retrieve data based on id.
    def get_object(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': "Data not found with that ID! Could not Update"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    # This method is implemented in ModelListView.
    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "Not Allowed! Use the API Update endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': "Data not found with that ID! Could not Update"})
            return self.render_to_response(error_data, status=404)
        print(request.body)
        # print(dir(request))
        # print(request.POST)
        # print(request.data)
        new_data = json.loads(request.body)
        print(new_data['content'])
        json_data = json.dumps({"message": "some data"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': "Data not found with that ID! Could not Update"})
            return self.render_to_response(error_data, status=404)
        json_data = json.dumps({"message": "Cannot delete entire data"})
        return self.render_to_response(json_data, status=403)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    List View
    Create View
    """
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        # check the form validation first, then save and serialize the data
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "Not Allowed"}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "Cannot delete entire data"})
        return self.render_to_response(json_data, status=403)
