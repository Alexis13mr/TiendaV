from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class item(models.Model):
    nomb = models.CharField(max_length=30)
    descrip=models.CharField(max_length=200)
    talla=models.CharField(max_length=3)
    valor=models.IntegerField()
    cant=models.IntegerField()
    tipo = models.CharField(max_length=30)
    imagen=models.ImageField(upload_to="productos",null=True)

