from .active_record_sport_section import Sport_Section_Active_Record
from .models import Sport_Section


class Sport_Section_DM():
    def __init__(self, sport, title, description):
        self.sport = sport
        self.title = title
        self.description = description

    @staticmethod
    def findById(id):
        return Sport_Section_Active_Record.getById(id)

    @staticmethod
    def findAll():
        return Sport_Section_Active_Record.getAll()

    @staticmethod
    def findAllBySportId(id):
        return Sport_Section_Active_Record.getAllBySportId(id)
