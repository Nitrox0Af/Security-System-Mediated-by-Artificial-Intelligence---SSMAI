from django.db import models
 
class Quest(models.Model):
    str_1= models.CharField(max_length=255, null=False)
    str_2= models.CharField(max_length=255, null=False)
    str_3= models.CharField(max_length=255, null=False)
    str_4= models.CharField(max_length=255, null=False)
    str_5= models.CharField(max_length=255, null=False)
# Create your models here.
