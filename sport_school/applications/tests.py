from django.test import TestCase

from django.contrib.auth.models import User
from .models import Application
from sport_sections.models import Sport_Section, Sport
from accounts.models import User_Data
# Create your tests here.


class TestCalls(TestCase):
    # Test creation application with min age
    def test_creation_app_with_min_age(self):
        user = User.objects.create_user(
            first_name='test1', last_name='test1', username='test1', email='test1@mail.ru', password='123123123')
        user_data = User_Data.objects.create(
            user=user, is_pupil=False, phone='45454545', sport_interests='bla bla')
        self.client.login(username='test1', password='123123123')
        response = self.client.post(
            '/accounts/login', {'username': 'test1', 'password': '123123123'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

        app_count = Application.objects.count()
        user = User.objects.get(username='test1')
        # Create data for application
        sport = Sport.objects.create(
            title='tennis', description='active sport')
        sport_section1 = Sport_Section.objects.create(
            sport=sport, title='table tennis', description='active sport')
        sport_section2 = Sport_Section.objects.create(
            sport=sport, title='big tennis', description='active sport')

        form_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'email': user.email,
                     'phone': user.user_data.phone,
                     'sport_section': sport_section1.id,
                     'birth_date': '2014-12-12',
                     'district': 'My District',
                     'gender': 'Ж'
                     }
        response = self.client.post("/application/send_application",
                                    form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Application.objects.count(), app_count + 1)
        self.assertIsNotNone(Application.objects.filter(user=user))

    # Test creation application with max age
    def test_creation_app_with_max_age(self):
        user = User.objects.create_user(
            first_name='test1', last_name='test1', username='test1', email='test1@mail.ru', password='123123123')
        user_data = User_Data.objects.create(
            user=user, is_pupil=False, phone='45454545', sport_interests='bla bla')
        # self.client.login(username='test1', password='123123123')
        response = self.client.post(
            '/accounts/login', {'username': 'test1', 'password': '123123123'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

        app_count = Application.objects.count()
        user = User.objects.get(username='test1')
        # Create data for application
        sport = Sport.objects.create(
            title='tennis', description='active sport')
        sport_section1 = Sport_Section.objects.create(
            sport=sport, title='table tennis', description='active sport')
        sport_section2 = Sport_Section.objects.create(
            sport=sport, title='big tennis', description='active sport')

        form_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'email': user.email,
                     'phone': user_data.phone,
                     'sport_section': sport_section1.id,
                     'birth_date': '1959-12-12',
                     'district': 'My District',
                     'gender': 'Ж'
                     }
        response = self.client.post("/application/send_application",
                                    form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Application.objects.count(), app_count + 1)
        self.assertIsNotNone(Application.objects.filter(user=user))

    # Test creation application with age in range
    def test_creation_app_with_age_in_range_1(self):
        user = User.objects.create_user(
            first_name='test1', last_name='test1', username='test1', email='test1@mail.ru', password='123123123')
        user_data = User_Data.objects.create(
            user=user, is_pupil=False, phone='45454545', sport_interests='bla bla')
        # self.client.login(username='test1', password='123123123')
        response = self.client.post(
            '/accounts/login', {'username': 'test1', 'password': '123123123'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

        app_count = Application.objects.count()
        user = User.objects.get(username='test1')
        # Create data for application
        sport = Sport.objects.create(
            title='tennis', description='active sport')
        sport_section1 = Sport_Section.objects.create(
            sport=sport, title='table tennis', description='active sport')
        sport_section2 = Sport_Section.objects.create(
            sport=sport, title='big tennis', description='active sport')

        form_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'email': user.email,
                     'phone': user_data.phone,
                     'sport_section': sport_section1.id,
                     'birth_date': '1971-08-12',
                     'district': 'My District',
                     'gender': 'Ж'
                     }
        response = self.client.post("/application/send_application",
                                    form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Application.objects.count(), app_count + 1)
        self.assertIsNotNone(Application.objects.filter(user=user))
    # Test creation application with age in range
    def test_creation_app_with_age_in_range_2(self):
        user = User.objects.create_user(
            first_name='test1', last_name='test1', username='test1', email='test1@mail.ru', password='123123123')
        user_data = User_Data.objects.create(
            user=user, is_pupil=False, phone='45454545', sport_interests='bla bla')
        # self.client.login(username='test1', password='123123123')
        response = self.client.post(
            '/accounts/login', {'username': 'test1', 'password': '123123123'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

        app_count = Application.objects.count()
        user = User.objects.get(username='test1')
        # Create data for application
        sport = Sport.objects.create(
            title='tennis', description='active sport')
        sport_section1 = Sport_Section.objects.create(
            sport=sport, title='table tennis', description='active sport')
        sport_section2 = Sport_Section.objects.create(
            sport=sport, title='big tennis', description='active sport')

        form_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'email': user.email,
                     'phone': user_data.phone,
                     'sport_section': sport_section1.id,
                     'birth_date': '2012-11-07',
                     'district': 'My District',
                     'gender': 'Ж'
                     }
        response = self.client.post("/application/send_application",
                                    form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Application.objects.count(), app_count + 1)
        self.assertIsNotNone(Application.objects.filter(user=user))
    # Test creation application with under min age
    def test_creation_app_with_small_age(self):
        user = User.objects.create_user(
            first_name='test1', last_name='test1', username='test1', email='test1@mail.ru', password='123123123')
        user_data = User_Data.objects.create(
            user=user, is_pupil=False, phone='45454545', sport_interests='bla bla')
        # self.client.login(username='test1', password='123123123')
        response = self.client.post(
            '/accounts/login', {'username': 'test1', 'password': '123123123'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

        app_count = Application.objects.count()
        user = User.objects.get(username='test1')
        # Create data for application
        sport = Sport.objects.create(
            title='tennis', description='active sport')
        sport_section1 = Sport_Section.objects.create(
            sport=sport, title='table tennis', description='active sport')
        sport_section2 = Sport_Section.objects.create(
            sport=sport, title='big tennis', description='active sport')

        form_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'email': user.email,
                     'phone': user_data.phone,
                     'sport_section': sport_section1.id,
                     'birth_date': '2015-01-01',
                     'district': 'My District',
                     'gender': 'Ж'
                     }
        response = self.client.post("/application/send_application",
                                    form_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Application.objects.count(), app_count)
        self.assertFalse(Application.objects.filter(user=user).exists())
    # Test creation application with large age
    def test_creation_app_with_old_age(self):
        user = User.objects.create_user(
            first_name='test1', last_name='test1', username='test1', email='test1@mail.ru', password='123123123')
        user_data = User_Data.objects.create(
            user=user, is_pupil=False, phone='45454545', sport_interests='bla bla')
        # self.client.login(username='test1', password='123123123')
        response = self.client.post(
            '/accounts/login', {'username': 'test1', 'password': '123123123'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

        app_count = Application.objects.count()
        user = User.objects.get(username='test1')
        # Create data for application
        sport = Sport.objects.create(
            title='tennis', description='active sport')
        sport_section1 = Sport_Section.objects.create(
            sport=sport, title='table tennis', description='active sport')
        sport_section2 = Sport_Section.objects.create(
            sport=sport, title='big tennis', description='active sport')

        form_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'email': user.email,
                     'phone': user_data.phone,
                     'sport_section': sport_section1.id,
                     'birth_date': '1958-01-01',
                     'district': 'My District',
                     'gender': 'Ж'
                     }
        response = self.client.post("/application/send_application",
                                    form_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Application.objects.count(), app_count)
        self.assertFalse(Application.objects.filter(user=user).exists())
