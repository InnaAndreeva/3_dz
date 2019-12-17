from django.test import TestCase
from django.test import Client
# Create your tests here.
from django.contrib.auth.models import User

from .models import User_Data


class TestCalls(TestCase):

    # OK
    def test_register_with_min_phone_length(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test1',
                     'last_name': 'test1',
                     'username': 'test1',
                     'email': 'test1@test.ru',
                     'phone': '1234567',
                     'password': '123123123',
                     'password2': '123123123',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)


        self.client.login(username='test1', password='123123123')
        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

    # OK
    def test_register_with_max_phone_length(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test2',
                     'last_name': 'test2',
                     'username': 'test2',
                     'email': 'test2@test.ru',
                     'phone': '11111111111',
                     'password': '123123123',
                     'password2': '123123123',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)


        self.client.login(username='test1', password='123123123')
        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

    # In a range
    def test_register_with_in_range_phone_1(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test3',
                     'last_name': 'test3',
                     'username': 'test3',
                     'email': 'test3@test.ru',
                     'phone': '12345678',
                     'password': '123123123',
                     'password2': '123123123',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)

    # In a range
    def test_register_with_in_range_phone_2(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test4',
                     'last_name': 'test4',
                     'username': 'test4',
                     'email': 'test4@test.ru',
                     'phone': '1234567890',
                     'password': 'Person123',
                     'password2': 'Person123',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)

    # Small phone number
    def test_register_with_small_phone(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test5',
                     'last_name': 'test5',
                     'username': 'test5',
                     'email': 'test5@test.ru',
                     'phone': '111111',
                     'password': '123123123',
                     'password2': '123123123',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), user_count)

    # Large phone number
    def test_register_with_large_phone(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test6',
                     'last_name': 'test6',
                     'username': 'test6',
                     'email': 'test6@test.ru',
                     'phone': '111111111111',
                     'password': '123123123',
                     'password2': '123123123',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), user_count)

    # Test password length
    # OK
    def test_register_with_min_password(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test7',
                     'last_name': 'test7',
                     'username': 'test7',
                     'email': 'test7@test.ru',
                     'phone': '1234567',
                     'password': '123456',
                     'password2': '123456',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)

        # OK
    def test_register_with_max_password(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test7',
                     'last_name': 'test7',
                     'username': 'test7',
                     'email': 'test7@test.ru',
                     'phone': '1234567',
                     'password': '123456789012',
                     'password2': '123456789012',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)

    # With short password
    def test_register_with_short_password(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test7',
                     'last_name': 'test7',
                     'username': 'test7',
                     'email': 'test7@test.ru',
                     'phone': '1234567',
                     'password': '12345',
                     'password2': '12345',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), user_count)

    # With large password
    def test_register_with_large_password(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test7',
                     'last_name': 'test7',
                     'username': 'test7',
                     'email': 'test7@test.ru',
                     'phone': '1234567',
                     'password': '1234567890123',
                     'password2': '1234567890123',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), user_count)

    def test_register_with_password_in_range_1(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test7',
                     'last_name': 'test7',
                     'username': 'test7',
                     'email': 'test7@test.ru',
                     'phone': '1234567',
                     'password': '1234567',
                     'password2': '1234567',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)


    def test_register_with_password_in_range_2(self):
        user_count = User.objects.count()
        form_data = {'first_name': 'test7',
                     'last_name': 'test7',
                     'username': 'test7',
                     'email': 'test7@test.ru',
                     'phone': '1234567',
                     'password': '12345678901',
                     'password2': '12345678901',
                     'sport_interests': 'bla bla bla'
                     }
        response = self.client.post("/accounts/register",
                                    form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)








