from django.db import models

# Create your models here.
class quest(models.Model):

    ques = models.CharField(max_length=1000,null=False,blank=False)