from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Sega(models.Model):

    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30) 
    año = models.DateField()
    descripcion = models.CharField(max_length=300, default="Descripción")

class GameBoy(models.Model):

    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30) 
    año = models.DateField()

class Nes(models.Model):

    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30) 
    año = models.DateField()


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Sega, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment[:60]