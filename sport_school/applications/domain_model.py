from .active_record import Application_Active_Record
from sport_sections.domain_model_sport_section import Sport_Section_DM

import datetime

class Application_DM():
    def __init__(self, user, sport_section_id, birth_date, district, gender):
        self.user = user
        self.sport_section = sport_section_id
        self.birth_date = birth_date
        self.district = district
        self.gender = gender
        self.errors = []

    # def is_valid(self):
    #     # if (len(self.district) > 0) and (len(self.gender) == 1) and (3 < int(self.age) < 100):
    #     if (len(self.district) > 0) and (len(self.gender) == 1) and (5 < (datetime.date.today() - datetime.datetime(birth_date)) < 60):
    #         return True
    #     else:
    #         return False
    #         
    def is_valid(self):
        if len(self.district) == 0:
            self.errors.append('Enter your district')
            return False
        elif len(self.gender) == 0:
            self.errors.append('Choose gender')
            return False
        elif 5 > (datetime.datetime.today().year - self.birth_date.year):
            self.errors.append('Too young')
            return False
        elif (datetime.datetime.today().year - self.birth_date.year) > 60:
            self.errors.append('Too old')
            return False
        else:
            return True



    def has_errors(self):
        if len(self.errors):
            return True
        else:
            return False

    @staticmethod
    def create(user, sport_section_id, birth_date, district, gender):
        app = Application_DM(user, sport_section_id, birth_date, district, gender)
        app.errors.clear()
        if app.is_valid():
            sport_section = Sport_Section_DM.findById(sport_section_id)
            a = Application_Active_Record(user=app.user, sport_section=sport_section,
                                          birth_date=app.birth_date, district=app.district, gender=app.gender)
            a.create()
        else:
            app.errors.append('Check your input please')
        return app
