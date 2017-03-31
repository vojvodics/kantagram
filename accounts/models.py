from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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


class Komentar(models.Model):
    akcija = models.ForeignKey(Akcija)
    autor = models.ForeignKey(User)
    tekst = models.TextField()
    datum_kreiranja = models.DateTimeField(default=timezone.now)
    lajkovi = models.IntegerField(default=0)

    def __str__(self):
        return self.tekst

class LajkZaKomentar(models.Model):
    pass

class LajkZaAkciju(models.Model):
    pass