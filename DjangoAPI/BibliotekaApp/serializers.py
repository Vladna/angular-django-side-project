from rest_framework import serializers
from BibliotekaApp.models import Knjige, Clan


class KnjigeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Knjige
        fields = ('KnjigaId',
                  'KnjigaIme',
                  'KnjigaAutor',
                  'KnjigaStanje',
                  'KnjigaDatumIzdavanja',
                  'KnjigaDatumVracanja',
                  'KnjiguIznajmio')


class ClanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clan
        fields = ('ClanId',
                  'ClanIme',
                  'ClanPrezime',
                  'ClanGodinaRodjenja',
                  'ClanStatus',
                  'ClanDatumUclanjenja',
                  'IznajmljenaKnjigaId')
