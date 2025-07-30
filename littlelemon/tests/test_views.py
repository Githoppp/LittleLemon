from django.test import TestCase
from restaurant.views import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(Title="Pizza", Price=12.00, Inventory=10)
        self.item2 = Menu.objects.create(Title="Pasta", Price=10.00, Inventory=5)
        self.item3 = Menu.objects.create(Title="Salad", Price=8.50, Inventory=20)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))  # Had to name the url in the app folder of urls.py as menu-list
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
