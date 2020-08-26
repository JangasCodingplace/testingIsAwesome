from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class CreateCourseAPITest(APITestCase):
    path = reverse('CreateCourseAPI')

    headers = {
        "Allow": "POST, OPTIONS",
        "Content-Type": "application/json",
        "Vary": "Accept"
    }

    def test_successfull_course_creation(self):
        data = {
            'title': 'Test'
        }
        response = self.client.post(
            path=self.path,
            data=data,
            headers=self.headers
        )
        expected_status_code = status.HTTP_201_CREATED
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], '')

    def test_failed_course_creation_by_title_not_unique(self):
        data = {
            'title': 'Test'
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
