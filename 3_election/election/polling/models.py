from django.db import models


# Create your models here.

class Candidate(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Voter(models.Model):
    voted_for=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    adhaar_num=models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    