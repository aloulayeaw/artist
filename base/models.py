from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title
    
class PaymentForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Nom")
    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    email = models.EmailField(unique=True, verbose_name="Email")
    telephone = models.CharField(max_length=45, blank=True, null=True)
    adresse = models.TextField(verbose_name="Adresse")
    
    def __str__(self):
        return self.name
    

class OrderCounterModel(models.Model):
    last_command_number = models.IntegerField(default=0)

