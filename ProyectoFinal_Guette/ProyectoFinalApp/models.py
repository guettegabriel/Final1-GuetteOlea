from django.db import models

# Create your models here.

class Sega(models.Model):

    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30) 
    año = models.DateField()

class GameBoy(models.Model):

    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30) 
    año = models.DateField()

class Nes(models.Model):

    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30) 
    año = models.DateField()


    

