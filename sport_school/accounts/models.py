from django.db import models
from django.contrib.auth.models import User

from sport_sections.models import Sport_Section
# Create your models here.


class User_Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_pupil = models.BooleanField(default=False)
    phone = models.CharField(max_length=200)
    sport_interests = models.TextField(blank=True)

    def __str__(self):
        return self.user.username



