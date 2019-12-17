from .active_record_sport import Sport_Active_Record

class Sport_DM():
    def __init__(self, title, description):
        self.title = title
        self.description = description

    @staticmethod
    def findAll():
        return Sport_Active_Record.getAll()



