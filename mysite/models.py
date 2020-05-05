from django.db import models
from django.conf import settings




class MainData(models.Model):
  UserID = models.TextField()
  Discription =  models.CharField(max_length=256, choices=[('Bf', 'Bf'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Lunch-Dinner', 'Lunch-Dinner'),('BF-Lunch-Dinner', 'BF-Lunch-Dinner')])
  Dateed = models.DateField()
  day = models.TextField(default="0")
  month = models.TextField(default='mar2020')
  Amount = models.FloatField()
  Status = models.TextField(default='not paid')

class MonthWise(models.Model):
  userid = models.TextField()
  month = models.TextField(default='mar2020')
  total = models.FloatField(default = 0)
  status = models.TextField(default='not paid')