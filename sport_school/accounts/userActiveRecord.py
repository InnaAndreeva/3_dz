from django.contrib.auth.models import User


class User_Active_Record:
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def check_if_exists_by_username(username):
        return User.objects.filter(username=username).exists()

    @staticmethod
    def check_if_exists_by_email(email):
        return User.objects.filter(email=email).exists()

    # @staticmethod
    # def get_by_username(username):
    #     return User.objects.get(username=username)

    # @staticmethod
    # def get_by_email(email):
    #     return User.objects.filter(email=email)

    def create(self):
        u = User.objects.create_user(first_name=self.first_name, last_name=self.last_name,
                                     username=self.username, email=self.email, password=self.password)
        u.save()
        return u

    # def delete(self):
    #     user = User.objects.get(username=self.username)
    #     user.delete()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
