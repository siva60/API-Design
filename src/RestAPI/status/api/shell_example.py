# Serializing using Shell:

import json
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from status.models import Status
from status.api.serializers import StatusSerializer

'''
serializing a single object.
'''
qs = Status.object.first()
serializer = StatusSerializer(qs)
print(serializer.data)   # gives ordered dict data from our model
json_data = JSONRenderer().render(serializer.data)
print(json_data)     # gives byte format of JSON. or Called JSON

# To convert back to Python data:
json.loads(json_data)       # will give list or dict data in python

# When we have streaming data:

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)       # will give  list or dict data in python.


'''
Serializing a queryset
'''
qs = Status.object.first()
serializer = StatusSerializer(qs, many=True)
print(serializer.data)   # gives ordered dict data from our model
json_data = JSONRenderer().render(serializer.data)
print(json_data)     # gives byte format of JSON. or Called JSON

# To convert back to Python data:
json.loads(json_data)       # will give list or dict data in python

# When we have streaming data:

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)       # will give  list or dict data in python.


'''
Create Object
'''
data = {'user': 1}
serializer = StatusSerializer(data)
serializer.is_valid()
serializer.save()


'''
Update Object
'''

obj = Status.object.first()
data = {'content': 'so updating method with new conte nt'}
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()


'''
Delete Object
'''
obj = Status.object.last()
obj.delete()


