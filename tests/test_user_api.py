from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class RegistrationAPITest(APITestCase):
    path = reverse('UserRegistrationAPI')

    headers = {
        "Allow": "POST, OPTIONS",
        "Content-Type": "application/json",
        "Vary": "Accept"
    }

    def test_successfull_user_registration(self):
        data = {
            'email': 'test@gmail.com',
            'password': 'passw0rd1'
        }
        response = self.client.post(
            path=self.path,
            data=data,
            headers=self.headers
        )
        expected_status_code = status.HTTP_201_CREATED
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['first_name'], '')
        self.assertEqual(response.data['last_name'], '')

    def test_successfull_user_registration_with_names(self):
        data = {
            'email': 'test@gmail.com',
            'password': 'passw0rd1',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(
            path=self.path,
            data=data,
            headers=self.headers
        )
        expected_status_code = status.HTTP_201_CREATED
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])

    def test_failed_registration_by_email_not_unique(self):
        data = {
            'email': 'unique@gmail.com',
            'password': 'passw0rd1'
        }
        self.client.post(
            path=self.path,
            data=data,
            headers=self.headers
        )
        response = self.client.post(
            path=self.path,
            data=data,
            headers=self.headers
        )
        expected_status_code = status.HTTP_400_BAD_REQUEST
        self.assertEqual(response.status_code, expected_status_code)
