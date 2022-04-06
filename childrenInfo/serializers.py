from dataclasses import fields
from rest_framework import serializers
from .models import ChildrenInfoModel

class ChildrenInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildrenInfoModel
        fields = ('name','age','gender','school')