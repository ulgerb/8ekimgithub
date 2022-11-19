from django.db import models

# Create your models here.

class Constraction(models.Model):
    title = models.CharField(("Proje Adı"),max_length=100 )
    detay = models.TextField(("Proje Detayları"))
    proje_user = models.CharField(("Proje Sorumlusu"), max_length=50)
    maliyet = models.IntegerField(("Maliyet"))
    image = models.FileField(("Proje resmi"), upload_to='', max_length=100)
    
    def __str__(self) -> str:
        return self.title