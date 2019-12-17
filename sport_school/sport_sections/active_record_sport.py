from .models import Sport


class Sport_Active_Record():
    def __init__(self, title, description):
        self.title = title
        self.description = description

    @staticmethod
    def getById(id):
        return Sport.objects.get(pk=id)

    @staticmethod
    def getAll():
        return Sport.objects.all()

