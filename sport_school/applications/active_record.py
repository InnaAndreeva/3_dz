from .models import Application


class Application_Active_Record():
    def __init__(self, user, sport_section, birth_date, district, gender):
        self.user = user
        self.sport_section = sport_section
        self.birth_date = birth_date
        self.district = district
        self.gender = gender

    def create(self):
        application = Application.objects.create(
            user=self.user, sport_section=self.sport_section, birth_date=self.birth_date, district=self.district, gender=self.gender)
        application.save()
        return application

    @staticmethod
    def getById(id):
        return Application.objects.get(pk=id)
