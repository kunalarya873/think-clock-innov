from django.db import models

class ImpedanceData(models.Model):
    test_id = models.IntegerField()
    type = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    ambient_temperature = models.FloatField()
    re = models.CharField(max_length=100)
    rct = models.CharField(max_length=100)
    capacity = models.FloatField()
