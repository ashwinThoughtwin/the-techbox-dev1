import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from apps.dashboard.models import TechTool, Employee, ToolsIssue
from apps.dashboard.serializers import ToolSerializers


class ToolListCreateAPIViewTestCase(APITestCase):
    url = reverse("techtoollist_api")

    def setUp(self):
        self.username = "chandu"
        self.email = "chandu@gmail.com"
        self.password = "gbbnmbmbmnvb"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test03_list_tools(self):
        response = self.client.get(self.url)
        cot=TechTool.objects.count()
        self.assertTrue(len(json.loads(response.content)) >= cot)
        print(cot)

    def test01_create_tool(self):
        response = self.client.post(self.url, {"name": "mousse", "status": False})
        self.assertEqual(201, response.status_code)

    def test02_create_tool_Failed(self):
        response = self.client.post(self.url, {"status": False})
        self.assertEqual(response.status_code, 400)




class ToolDetailAPIViewTestCase(APITestCase):

    def setUp(self):
        self.tool = TechTool.objects.create(name='DvD', status=False)
        self.url = reverse("tooldetail_api", kwargs={"pk": self.tool.pk})
        self.url2 = reverse("tooldetail_api", kwargs={"pk": 5})

        self.username = "chandu"
        self.email = "chandu@gmail.com"
        self.password = "gbbnmbmbmnvb"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test04_tool_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    # def test05_tool_detail_Failed(self):
    #     response = self.client.get(self.url2)
    #     self.assertEqual(404, response.status_code)

    def test05_tool_update(self):
        response1 = self.client.put(self.url, {"name": "phone", 'status': True})
        response = json.loads(response1.content)
        tool = TechTool.objects.get(id=self.tool.id)
        # self.assertEqual(response.get("name"), tool.name)
        self.assertEqual(response1.status_code,200)

    def test05_tool_update_fail(self):
        response1 = self.client.put(self.url, {"names": "phone", 'status': True})

        self.assertEqual(response1.status_code, 400)

    def test06_tool__delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
        print("for tool delete",response.status_code)

    # def test06_tool__delete_fail(self):
    #     response = self.client.delete(self.url2)
    #     self.assertEqual(404, response.status_code)
    #     print("for tool delete",response.status_code)
    #





class AssignListCreateAPIViewTestCase(APITestCase):
    url = reverse("assign_create_api")

    def setUp(self):
        self.emp = Employee.objects.create(name="demo", designation='Team Leader', address='demo', mobile=97654323,
                                           email="emdfg@gmail.com", date_of_birth="1997-03-08")
        self.tool = TechTool.objects.create(name='DvD', status=False)

    def test07_create_assign(self):
        response = self.client.post(self.url, {
            "id": 144,
            "borrowTime": "2021-04-29T19:44:32.729760+05:30",
            "submitDate": "2021-04-29T20:44:00+05:30",
            "timeOut": True,
            "empName": self.emp.id,
            "techTool": self.tool.id
        })
        self.assertEqual(201, response.status_code)
        print("for assign success ",response.status_code)


    def test08_create_assign_Failed(self):
        response = self.client.post(self.url, {"timeOut": True})
        self.assertEqual(response.status_code, 400)
        print("for assign fails",response.status_code)

