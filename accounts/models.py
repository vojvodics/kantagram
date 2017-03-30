from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)
    photo = models.URLField(default="http://www.aspirehire.co.uk/aspirehire-co-uk/_img/profile.svg")

    def __str__(self):
        return self.user.username


class Akcija (models.Model):
    title = models.CharField(max_length=300)
    admin = models.ForeignKey(User)
    description = models.TextField()
    photo = models.URLField(blank=False)
    location = models.CharField(max_length=500)
    state = models.CharField(max_length=200)
    long_desc = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    votes = models.IntegerField(default=0)

    successful = models.BooleanField(default=False)
    update_image = models.URLField(blank=True)
    report = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Prijava(models.Model):
    korisnik = models.ForeignKey(User)
    akcija = models.ForeignKey(Akcija)
