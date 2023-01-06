from django.db import models

# Create your models here.

#Model Created

class Teacher(models.Model):
	Firstname = models.CharField(max_length=50)
	Lastname = models.CharField(max_length=50)
	Email = models.EmailField(max_length=50)
	Contacr = models.CharField(max_length=50)

#this function is user for converting object to 
def __str__(self) -> str:
	return self.Firstname
