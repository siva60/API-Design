1. Create
2. Retrieve --- List
3. Update
4. Delete

1. POST
2. GET
3. PUT( or Patch)
4. DELETE


urls:
http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/updates/examples/
http://127.0.0.1:8000/updates/cbv/
http://127.0.0.1:8000/updates/cbv2/
http://127.0.0.1:8000/updates/serialize/
http://127.0.0.1:8000/updates/serialize-detail/

http://127.0.0.1:8000/api/
http://127.0.0.1:8000/api/<id>

#########################################
Obtaining JSON Response:

1. import json, HttpResponse


   Then dump the data using json.dumps
   
   return HttpRespnse(data)
   
2. Using JsonResponse
    from django.http import JsonResponse, HttpResponse
    
    return HttpResponse(data)


##############################################

Using Class Based Views:
1. from django.views.generic import View

** concept of mixings. 
It allows us to extend the class based view with new code

##########################################33

Serializing:
1. Gives the serialized data
siva@siva-5548:~/Projects60/API-Design/src/RestAPI$ python manage.py dumpdata --format json --indent 4

2. To get the specific data:
(venv) siva@siva-5548:~/Projects60/API-Design/src/RestAPI$ python manage.py dumpdata admin.logentry --format json --indent 4

TO initiate serialization:
from django.core.serializers import serialize

Basic Example in view.py:


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content',))
        print(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')







    
