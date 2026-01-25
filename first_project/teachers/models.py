from django.db import models


class Teacher(models.Model):
    
    t_id = models.CharField(max_length = 5)
    name = models.CharField(max_length = 30)


    def __str__(self):
        return self.name
# Create your models here.
