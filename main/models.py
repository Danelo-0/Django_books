from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    fio = models.CharField('ФИО', max_length=250)
    dateBirth = models.DateField("Дата рождения", auto_now=False, auto_now_add=False)
    dateDeath = models.DateField("Дата смерти", auto_now=False, auto_now_add=False)
    lid = models.TextField("Описание")

    def __str__(self):
        return self.fio


class Language(models.Model):
    language = models.CharField('Язык перевода', max_length=150)

    def __str__(self):
        return self.language


class Print(models.Model):
    title = models.CharField('Название издательства', max_length=250)
    city = models.CharField('Город издательства', max_length=250)
    date = models.PositiveIntegerField("Дата основания")
    lid = models.TextField("Описание")

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField('Жанр', max_length=250)

    def __str__(self):
        return self.genre


class Book(models.Model):
    title = models.CharField('Название', max_length=250)
    author = models.ManyToManyField(Author)
    description = models.TextField("Описание")
    publishing_house = models.ForeignKey(Print, on_delete=models.CASCADE)
    date = models.PositiveIntegerField("Год выпуска")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language)
    isbn = models.BigIntegerField("ISBN", unique=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    familia = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField('Город', max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    lid = models.TextField("Описание")
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.familia
