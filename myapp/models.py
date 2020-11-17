from django.db import models

# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField(max_length=4)
    def __str__(self):
        return "fname="+self.fname+", lname="+self.lname+", age="+self.age