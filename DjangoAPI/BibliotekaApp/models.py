from django.db import models


class Knjige(models.Model):
    KnjigaId = models.AutoField(primary_key=True)
    KnjigaIme = models.CharField(max_length=500)
    KnjigaAutor = models.CharField(max_length=500)
    KnjigaStanje = models.BooleanField(default=False)
    KnjigaDatumIzdavanja = models.DateField()
    KnjigaDatumVracanja = models.DateField()
    KnjiguIznajmio = models.IntegerField()


class Clan(models.Model):
    ClanId = models.AutoField(primary_key=True)
    ClanIme = models.CharField(max_length=500)
    ClanPrezime = models.CharField(max_length=500)
    ClanGodinaRodjenja = models.DateField()
    ClanStatus = models.CharField(max_length=500)
    ClanDatumUclanjenja = models.CharField(max_length=500)
    IznajmljenaKnjigaId = models.IntegerField()
