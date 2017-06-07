from django.db import models
from django.contrib.auth.models import User

class waiterprofile(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.CharField(max_length=2)
    birth = models.DateField(auto_now_add=False)
    since = models.DateTimeField(auto_now_add=True)
    adress = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return "{}".format(self.name)

class Order(models.Model):
    waiter = models.ForeignKey(User)
    cook = models.CharField(max_length=50)
    table = models.CharField(max_length=2)
    text = models.TextField(max_length=300)
    remark = models.TextField(max_length=100)
    status = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)