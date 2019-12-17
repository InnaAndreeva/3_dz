from .userActiveRecord import User_Active_Record
from .userDataActiveRecord import User_Data_Active_Record


class User_DM:
    def __init__(self, first_name, last_name, username, email, phone, password, password2, sport_interests):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.password2 = password2
        self.sport_interests = sport_interests
        self.errors = []

    # def is_valid(self):
    #     if (self.password == self.password2) and (len(self.first_name) > 0) and (len(self.last_name) > 0) and (len(self.phone) > 0):
    #         return True
    #     else:
    #         return False
    #         
    def is_valid(self):
        if self.password != self.password2:
            self.errors.append('Passwords not match')
            return False
        elif (len(self.password) < 6):
            self.errors.append('Short Password')
            return False
        elif (len(self.password) > 12):
            self.errors.append('Large Password')
            return False
        elif (len(self.first_name) == 0) or (len(self.last_name) == 0):
            self.errors.append('Enter first name and last name')
            return False
        elif len(self.phone) < 7:
            self.errors.append('Enter phone number')
            return False
        elif len(self.phone) > 11:
            self.errors.append('Not correct phone number')
            return False
        else:
            return True



    def is_user_exists(self):
        if User_Active_Record.check_if_exists_by_email(self.email) or User_Active_Record.check_if_exists_by_username(self.username):
            return True
        else:
            return False

    def has_errors(self):
        if len(self.errors):
            return True
        else:
            return False

    def get_errors(self):
        return self.errors

    @staticmethod
    def create_user(first_name, last_name, username, email, phone, password, password2, sport_interests):
        user_dm = User_DM(
            first_name, last_name, username, email, phone, password, password2, sport_interests)
        # Clean up old errors
        user_dm.errors.clear()
        if user_dm.is_valid():
            if not user_dm.is_user_exists():
                user_ar = User_Active_Record(
                    user_dm.first_name, user_dm.last_name, user_dm.username, user_dm.email, user_dm.password)
                user = user_ar.create()
                user_data_ar = User_Data_Active_Record(
                    user, phone, sport_interests)
                user_data_ar.create()
            else:
                user_dm.errors.append('Username or email are taken')

        else:
            user_dm.errors.append('Check input please')
        return user_dm
            
