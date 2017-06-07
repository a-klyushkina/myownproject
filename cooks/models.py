from django.db import models

# Create your models here.
class cookprofile(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.CharField(max_length=2)
    birth = models.DateField(auto_now_add=False)
    since = models.DateTimeField(auto_now=True)
    adress = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return "{}".format(self.name)