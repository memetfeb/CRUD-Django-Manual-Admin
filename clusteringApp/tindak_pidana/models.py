from django.db import models
from django.utils.translation import gettext_lazy as _

class Kategori(models.Model):
    nama_TP = models.CharField(max_length=30)
    pasal_TP = models.CharField(max_length=30)
    kategori_TP = models.CharField(max_length=3)
