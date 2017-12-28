from django.urls import reverse
from rabbits_rest.models import Rabbit
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class RabbitTestEmptyDB(APITestCase):
    def setUp(self):
        Rabbit.objects.all().delete()

    def test_add(self):
        url = reverse('rabbit-list')
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rabbit.objects.count(), 1)
        self.assertEqual(Rabbit.objects.get().Nickname, 'Bunny BunBun')

    def test_get_list(self):
        url = reverse('rabbit-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
        self.assertEqual(Rabbit.objects.count(), 0)

    def test_get_detail(self):
        url = reverse('rabbit-detail', args=[2])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update(self):
        url = reverse('rabbit-detail', args=[2])
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RabbitTestSingleEntryDB(APITestCase):
    def setUp(self):
        Rabbit.objects.all().delete()
        instance = Rabbit(Nickname="Mr Debugles")
        instance.save()

    def test_add(self):
        url = reverse('rabbit-list')
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rabbit.objects.count(), 2)
        self.assertEqual(Rabbit.objects.get(id=1).Nickname, 'Mr Debugles')
        self.assertEqual(Rabbit.objects.get(id=2).Nickname, 'Bunny BunBun')

    def test_get_list(self):
        url = reverse('rabbit-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['Nickname'], 'Mr Debugles')
        self.assertEqual(Rabbit.objects.count(), 1)

    def test_get_detail_non_existent(self):
        url = reverse('rabbit-detail', args=[2])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_non_existent(self):
        url = reverse('rabbit-detail', args=[2])
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_detail_existent(self):
        url = reverse('rabbit-detail', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Nickname'], 'Mr Debugles')

    def test_update_existent(self):
        url = reverse('rabbit-detail', args=[1])
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Rabbit.objects.get().Nickname, 'Bunny BunBun')


class RabbitTestMultipleEntryDB(APITestCase):
    def setUp(self):
        Rabbit.objects.all().delete()
        self.name_list = ['Bugels', 'BugyDeBug', 'Buger', 'Bugerite', 'BugBugy']
        for name in self.name_list:
            instance = Rabbit(Nickname=name)
            instance.save()

    def test_add(self):
        url = reverse('rabbit-list')
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rabbit.objects.count(), len(self.name_list) + 1)
        for i, name in enumerate(self.name_list):
            self.assertEqual(Rabbit.objects.get(id=i + 1).Nickname, name)
        self.assertEqual(Rabbit.objects.get(id=len(self.name_list) + 1).Nickname, 'Bunny BunBun')

    def test_get_list(self):
        url = reverse('rabbit-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for i, name in enumerate(self.name_list):
            self.assertEqual(response.data[i]['Nickname'], name)
        self.assertEqual(Rabbit.objects.count(), len(self.name_list))

    def test_get_detail_non_existent(self):
        url = reverse('rabbit-detail', args=[len(self.name_list) + 1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_non_existent(self):
        url = reverse('rabbit-detail', args=[len(self.name_list) + 1])
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_detail_existent(self):
        url = reverse('rabbit-detail', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Nickname'], self.name_list[0])

    def test_update_existent(self):
        url = reverse('rabbit-detail', args=[1])
        data = {'Nickname': 'Bunny BunBun'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Rabbit.objects.get(id=1).Nickname, 'Bunny BunBun')
