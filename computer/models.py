from django.db import models

class details(models.Model):
    name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    subject=models.TextField
    message=models.TextField
    
    
    

# Create your models here.
