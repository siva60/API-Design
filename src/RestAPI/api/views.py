from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
import json
from api.mixings import CSRFExemptMixin
from updates.mixings import HttpResponseMixin
from api.forms import UpdateModelForm
from api.utils import is_json

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

        # First check if the json data is given or not.
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': "Invalid JSON data"})
            return self.render_to_response(error_data, status=404)

        # check if object with that valid id is present in db. The returned object contains the old data
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': "Data not found with that ID! Could not Update"})
            return self.render_to_response(error_data, status=404)

        # now old data is as below
        data = json.loads(obj.serialize())
        # Or Instead of directly using serializer, define the structure as below.
        # saved_data = {
        #     "user": obj.user,
        #     "content": obj.content
        # }

        # new passed data from user is:
        passed_data = json.loads(request.body)

        # Now update the old data with new data.
        for key, value in passed_data.items():
            data[key] = value

        # Now pass the updated data object to our model form
        form = UpdateModelForm(data, instance=obj)

        # Perform form validation
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({"message": "some data"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):

        # first check data with that valid id is present
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': "Data not found with that ID! Could not Update"})
            return self.render_to_response(error_data, status=404)

        # then perform delete operation, here obj.delete will have 2 items in it.
        deleted, item_deleted = obj.delete()
        print(deleted)
        if deleted == 1:
            json_data = json.dumps({"message": "Successfully deleted"})
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps({'message': "Could not Delete item! "})
        return self.render_to_response(error_data, status=400)


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

        # check if the json data is valid.
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': "Invalid JSON data"})
            return self.render_to_response(error_data, status=404)

        # then decode the json data to add to our model form.
        data = json.loads(request.body)
        form = UpdateModelForm(data)

        # Perform the form validation.
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)

        # if errors in the form return json data to browser as error
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        data = {"message": "Not Allowed"}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "Cannot delete entire data"})
        return self.render_to_response(json_data, status=403)
