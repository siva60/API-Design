from rest_framework import serializers

from status.models import Status

##########################
# This module Turns our actual models into JSON data. This process is Serialization.
# Serializers also validate the data.
############################


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image',
        ]

    def validate_content(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("Input too long")
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or Image is missing")
        return data

