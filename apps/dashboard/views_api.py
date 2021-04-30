from rest_framework.exceptions import ValidationError

from .serializers import ToolSerializers, AssignToolSerializers
from .models import TechTool, ToolsIssue
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

class TechToolListApi(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        techtools = TechTool.objects.all()
        serializer = ToolSerializers(techtools, many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self, request, formar=None):
        serializer = ToolSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechToolDetailApi(APIView):
    permission_classes = (permissions.IsAuthenticated,)
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        techtool = self.get_object(pk)
        techtool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignToolListApi(generics.ListAPIView):
    queryset = ToolsIssue.objects.all()
    serializer_class = AssignToolSerializers


class AssignToolCreateApi(generics.CreateAPIView):
    queryset = ToolsIssue.objects.all()
    serializer_class = AssignToolSerializers
