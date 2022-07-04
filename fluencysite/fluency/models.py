from unicodedata import category
from django.db import models

# Create your models here.
class VocabList(models.Model):
    categoryname = models.CharField(max_length=500)

    def __str__(self):
        return self.categoryname

class Item(models.Model):
    vocablist = models.ForeignKey(VocabList, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    delete = models.BooleanField()
    def __str__(self):
        return self.text
