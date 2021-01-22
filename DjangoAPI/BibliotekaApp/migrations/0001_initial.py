# Generated by Django 3.1.5 on 2021-01-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('ClanId', models.AutoField(primary_key=True, serialize=False)),
                ('ClanIme', models.CharField(max_length=500)),
                ('ClanPrezime', models.CharField(max_length=500)),
                ('ClanGodinaRodjenja', models.DateField()),
                ('ClanStatus', models.CharField(max_length=500)),
                ('ClanDatumUclanjenja', models.CharField(max_length=500)),
                ('IznajmljenaKnjigaId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Knjige',
            fields=[
                ('KnjigaId', models.AutoField(primary_key=True, serialize=False)),
                ('KnjigaIme', models.CharField(max_length=500)),
                ('KnjigaAutor', models.CharField(max_length=500)),
                ('KnjigaStanje', models.BooleanField(default=False)),
                ('KnjigaDatumIzdavanja', models.DateField()),
                ('KnjigaDatumVracanja', models.DateField()),
                ('KnjiguIznajmio', models.IntegerField()),
            ],
        ),
    ]