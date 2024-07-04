from django.db import models
from pass_the_pass.resourses import STATUS, LEVEL, SEASONS, new


class User(models.Model):
    """ Model containing user data """
    email = models.EmailField(primary_key=True, unique=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Coord(models.Model):
    """Model containing coordinates"""
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):
    """Model containing level difficulty"""
    season = models.CharField(max_length=50, choices=SEASONS)
    difficulty = models.CharField(max_length=50, choices=LEVEL)


class Image(models.Model):
    """Model containing image data """
    data = models.ImageField()
    title = models.CharField(max_length=100)


class Camping(models.Model):
    """Model for working with a database """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coord, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS, default=new)


class CampingImage(models.Model):
    """Model for linking an image to a pereval"""
    camping = models.ForeignKey('Camping', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
