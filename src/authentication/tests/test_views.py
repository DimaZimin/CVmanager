from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self) -> None:
        pass


