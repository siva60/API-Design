from django.db import models
from django.conf import settings


# image name and storage
def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)


# creating custom queryset to make our method more chainable.
# https://simpleisbetterthancomplex.com/tips/2016/08/16/django-tip-11-custom-manager-with-chainable-querysets.html

class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


# This model similar to instagram status, post, update
class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # allow users to update as well.
    timestamp = models.DateTimeField(auto_now_add=True)

    object = StatusManager()

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = 'Status post'
        # verbose_name_plural = 'Status posts'
