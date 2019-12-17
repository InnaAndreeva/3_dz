from .models import Sport_Section


class Sport_Section_Active_Record():
    def __init__(self, sport, title, description):
        self.title = title
        self.description = description
        self.sport = sport

    @staticmethod
    def getById(id):
        return Sport_Section.objects.get(pk=id)

    @staticmethod
    def getAll():
        return Sport_Section.objects.all()

    @staticmethod
    def getAllBySportId(id):
        return Sport_Section.objects.filter(sport=id)