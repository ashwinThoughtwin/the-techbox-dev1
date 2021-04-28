from django.test import TestCase,Client
from  .views_api import TechToolListApi
from rest_framework import status
from django.urls import reverse
import json


class TestToolListApi(TestCase):
    def test__001_listoftools(self):
        client = Client()
        response = client.get(reverse('techtoollist_api'))
        print("hi")
        self.assertEquals(response.status_code,status.HTTP_200_OK)



