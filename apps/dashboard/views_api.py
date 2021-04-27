from .serializers import ToolSerializers,AssignToolSerializers
from .models import TechTool,ToolsIssue
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TechToolListApi(APIView):
    def get(self, request, format=None):
        techtools = TechTool.objects.all()
        serializer = ToolSerializers(techtools, many=True)
        return Response(serializer.data)

    def post(self, request, formar=None):
        serializer = ToolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechToolDetailApi(APIView):

    def get_object(self, pk):
        try:
            return TechTool.objects.get(pk=pk)
        except TechTool.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        techtool = self.get_object(pk)
        serializer = ToolSerializers(techtool)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        techtool = self.get_object(pk)
        serializer = ToolSerializers(techtool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        techtool = self.get_object(pk)
        techtool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignToolApi(APIView):

    def get(self, request):
        assignlist = ToolsIssue.objects.all()
        serializer = AssignToolSerializers(assignlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignToolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




