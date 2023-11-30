from django.test import Client, TestCase

from books.models import Book


class BookEndpointsTest(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
    
    def test_create(self):
        data = {
            
        }
        