from django.contrib import admin
from status.models import Status as StatusModel
from status.forms import StatusForm
# Register your models here.


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']

    class Meta:
        model = StatusModel


admin.site.register(StatusModel, StatusAdmin)
