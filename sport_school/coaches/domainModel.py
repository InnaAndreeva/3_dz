from .activeRecord import Coach_Active_Record


class Coach_DM:
    def __init__(self, sport_section, first_name, last_name, photo, description, phone, email, hire_date):
        self.sport_section = sport_section
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo
        self.description = description
        self.phone = phone
        self.email = email
        self.is_staff = True
        self.hire_date = hire_date

    @staticmethod
    def findAll():
        return Coach_Active_Record.getAll()

    
