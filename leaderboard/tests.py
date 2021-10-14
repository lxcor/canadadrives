from rest_framework import status
from rest_framework.test import APITestCase

from leaderboard.models import User


class UserTests(APITestCase):

    def setUp(self):
        """
        Create a new user object to be tested
        """
        self.user = User.objects.create(name="Samantha", age=55, address="Boston")
        self.pk = self.user.pk

    def test_list_users(self):
        """
        Ensures the existing users can be listed
        """
        url = "http://0.0.0.0:8000/users/"
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)

    def test_retrieve_user(self):
        """
        Ensures the existing user can be retrieved
        """
        url = "http://0.0.0.0:8000/users/%s/" % self.user.pk
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Samantha')
        self.assertEqual(User.objects.get().age, 55)
        self.assertEqual(User.objects.get().address, 'Boston')
        self.assertEqual(User.objects.get().points, 0)

    def test_delete_user(self):
        """
        Ensure an existing user can be deleted.
        """
        url = "http://0.0.0.0:8000/users/%s/" % self.user.pk
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_create_user(self):
        """
        Ensures a new user can be created.
        """
        url = "http://0.0.0.0:8000/users/"
        data = {'name': 'Regina', 'age': 89, 'address': 'Lake View'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().name, 'Regina')
        self.assertEqual(User.objects.last().age, 89)
        self.assertEqual(User.objects.last().address, 'Lake View')
        self.assertEqual(User.objects.last().points, 0)

    def test_increment_and_decrement_user_points(self):
        """
        Ensures the points of an user can be incremented and decremented by one.
        """
        url = "http://0.0.0.0:8000/users/%s/increment_points/" % self.user.pk
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().points, 1)

        url = "http://0.0.0.0:8000/users/%s/decrement_points/" % self.user.pk
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().points, 0)

