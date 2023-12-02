from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Book

User = get_user_model()

class BookAPITestCase(TestCase):
    def setUp(self):
        self.guest_client = APIClient()
        self.user = User.objects.create_user(
            username='Dordzhi',
            email='dordzhi@mail.ru',
            password='dordzhi'
        )
        self.authorized_client = APIClient()
        self.authorized_client.force_authenticate(user=self.user)

        self.data = {
            'title': 'Шерлок Холмс',
            'author': 'Артур Конан Дойл',
            'publication_year': 1887,
            'isbn': '9785906928429'
        }
    
    def test_book_creation(self):
        self.assertTrue(self.user.is_authenticated)
        incomplete_data = {
            'title': 'Шерлок Холмс 2',
            'publication_year': 1889,
            'isbn': '9785906928430'
        }
        response = self.guest_client.post(
            '/api/books/', self.data, format='json'
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

        response1 = self.authorized_client.post(
            '/api/books/', self.data, format='json'
        )
        self.assertEqual(response1.status_code, HTTPStatus.CREATED)
        self.assertTrue(
            Book.objects.filter(
                title='Шерлок Холмс',
                author='Артур Конан Дойл'
            ).exists()
        )

        response2 = self.authorized_client.post(
            '/api/books/', incomplete_data, format='json'
        )
        self.assertEqual(response2.status_code, HTTPStatus.BAD_REQUEST)
    
    def test_get_list_book(self):
        response = self.guest_client.get('/api/books/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
