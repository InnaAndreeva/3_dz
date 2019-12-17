from .models import User_Data


class User_Data_Active_Record:
    def __init__(self, user, phone, sport_interests):
        self.phone = phone
        self.sport_interests = sport_interests
        self.is_pupil = False
        self.user = user

    @staticmethod
    def getById(id):
        u_d = User_Data.objects.get(pk=id)
        return u_d

    def create(self):
        u_d = User_Data.objects.create(user=self.user, phone=self.phone,
                                       sport_interests=self.sport_interests, is_pupil=self.is_pupil)
        u_d.save()
        return u_d

    def getUserInfo(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.username}'

    # @staticmethod
    # def changePhone(user, new_phone):
    #     u_d = User_Data.objects.filter(user=self.user)
    #     u_d.phone = new_phone
    #     u_d.save()
