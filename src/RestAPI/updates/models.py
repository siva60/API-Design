from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json
# Create your models here.


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


# custom queryset manager
class UpdateQueryset(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     for obj in qs:
    #         struct = json.loads(obj.serialize())
    #         final_array.append(struct)
    #     return json.dumps(final_array)

    def serialize(self):
        list_values = list(self.values("user", "content", "image", "id"))
        print("values: ",list_values)
        return json.dumps(list_values)


# serializing the entire queryset
class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQueryset(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    # serializing the individual instance.
    # def serialize(self):
    #     json_data = serialize("json", [self], fields=('user', 'content', 'image'))
    #     # convert to python dictionary
    #     stuct = json.loads(json_data)  # list of dictioanry
    #     print(stuct)
    #     # again convert back to json data to give http response
    #     data = json.dumps(stuct[0]['fields'])
    #     return data

    def serialize(self):
        # try:
        #     image = self.image.url
        # except:
        image = ""

        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user.id,
            "image": image
        }
        print(data)
        data =json.dumps(data)
        print(data)
        return data

