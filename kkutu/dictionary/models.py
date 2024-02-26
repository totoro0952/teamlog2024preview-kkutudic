from django.db import models
from typing import Any

# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.word
    
class Attack(models.Model):
    word = models.CharField(max_length=200, null=True)
    next = models.IntegerField(null=True)

    def __str__(self):
        return self.word
    
class OneTime(models.Model):
    word = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.word
    
class ThreeLetter(models.Model):
    word = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.word
    
class WordBattle(models.Model):
    word = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.word