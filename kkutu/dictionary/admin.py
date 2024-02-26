from django.contrib import admin
from dictionary.models import *

# Register your models here.
li = [Dictionary, Attack, OneTime, ThreeLetter, WordBattle]
for i in li:
    admin.site.register(i)