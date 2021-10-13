# from rest_framework.test import RequestsClient, CoreAPIClient
#
# client = RequestsClient()
# response = client.get('http://127.0.0.1:8000/user/')
# assert response.status_code == 200


# Fetch the API schema
# client = CoreAPIClient()
# schema = client.get('http://127.0.0.1:8000/schema/')

# Create a new user
# params = {'name': 'Regina', 'age': 89, 'address': 'Lake View'}
# client.action(schema, ['users', 'create'], params)

# Ensure that the organisation exists in the listing
# data = client.action(schema, ['users', 'list'])
# assert(len(data) == 1)
# assert(data == [{'name': 'Regina', 'age': 89, 'address': 'Lake View'}])

from rest_framework import status
from rest_framework.test import APITestCase

from leaderboard.models import User


class UserTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create and read a new user object.
        """
        url = "http://127.0.0.1:8000/user/"
        data = {'name': 'Regina', 'age': 89, 'address': 'Lake View'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Regina')
        self.assertEqual(User.objects.get().points, 0)
        self.assertEqual(User.objects.get().age, 89)
        self.assertEqual(User.objects.get().address, 'Lake View')

    def test_update_account(self):
        """
        Ensure we can update a new user object.
        """

        url = "http://127.0.0.1:8000/user/"
        data = {'name': 'Regina', 'age': 89, 'address': 'Lake View'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().age, 89)

        url = "http://127.0.0.1:8000/user/%s/" % User.objects.get().pk
        data = {'name': 'Regina', 'age': 99, 'address': 'Lake View'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().age, 99)
