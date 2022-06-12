from django.db import models
from django.db.models import Model


class PrayTimeTable(Model):
    monthNum = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pray_times')

