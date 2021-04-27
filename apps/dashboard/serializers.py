from rest_framework import serializers
from .models import TechTool, ToolsIssue


class ToolSerializers(serializers.ModelSerializer):
    class Meta:
        model = TechTool
        fields = ("__all__")


class AssignToolSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToolsIssue
        fields = ('id', 'borrowTime', 'submitDate', 'timeOut', 'empName', 'techTool')
