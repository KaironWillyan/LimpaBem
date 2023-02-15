from django.db import models

# Create your models here.

class Functionary(models.Model):
    class Meta:
        abstract = True
        
    firstName = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    lastName = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    
    serviceTime = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    
    sallary = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    

class Manager(models.Model):
    
    objects = models.Manager()