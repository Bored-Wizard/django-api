from rest_framework import serializers
from . import models

class NoteSerializer(serializers.Modelserializer):
    class Meta:
        model = models.Note
        fields = "__all__"