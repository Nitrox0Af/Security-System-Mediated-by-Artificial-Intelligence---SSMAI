from django.db import models
 
class resultado(models.Model):
    res= models.IntegerField()
    def __str__(self):
        return self.res
# Create your models here.
