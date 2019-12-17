from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from sport_sections.models import Sport_Section
# Create your models here.


class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sport_section = models.ForeignKey(Sport_Section, on_delete=models.CASCADE)
    # age = models.IntegerField()
    birth_date = models.DateField(default=datetime.now)
    district = models.CharField(max_length=200)
    gender = models.CharField(max_length=2)

    def __str__(self):
        return self.user.username + self.sport_section.title
