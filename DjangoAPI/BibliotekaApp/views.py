from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BibliotekaApp.models import Knjige, Clan
from BibliotekaApp.serializers import KnjigeSerializers, ClanSerializers


@csrf_exempt
def knjigeApi(request, id=0):
    if request.method == 'GET':
        knjige = Knjige.objects.all()
        knjige_serializer = KnjigeSerializers(knjige, many=True)
        return JsonResponse(knjige_serializer.data, safe=False)
    elif request.method == 'POST':
        knjige_data = JSONParser().parse(request)
        knjige_serializer = KnjigeSerializers(data=knjige_data)
        if knjige_serializer.is_valid():
            knjige_serializer.save()
            return JsonResponse("Dodano uspesno", safe=False)
        return JsonResponse("Neuspesno", safe=False)

    elif request.method == 'PUT':
        knjige_data = JSONParser().parse(request)
        knjige = Knjige.objects.get(KnjigaId=knjige_data['KnjigaId'])
        knjige_serializer = KnjigeSerializers(knjige, data=knjige_data)
        if knjige_serializer.is_valid():
            knjige_serializer.save()
            return JsonResponse("Dodano uspesno", safe=False)
        return JsonResponse("Neuspesno", safe=False)

    elif request.method == 'DELETE':
        knjige = Knjige.objects.get(KnjigaId=id)
        knjige.delete()
        return JsonResponse("Izbrisano uspesno", safe=False)


@csrf_exempt
def clanApi(request, id=0):
    if request.method == 'GET':
        clanovi = Clan.objects.all()
        clanovi_serializer = ClanSerializers(clanovi, many=True)
        return JsonResponse(clanovi_serializer.data, safe=False)
    elif request.method == 'POST':
        clanovi_data = JSONParser().parse(request)
        clanovi_serializer = ClanSerializers(data=clanovi_data)
        if clanovi_serializer.is_valid():
            clanovi_serializer.save()
            return JsonResponse("Dodano uspesno", safe=False)
        return JsonResponse("Neuspesno", safe=False)

    elif request.method == 'PUT':
        clanovi_data = JSONParser().parse(request)
        clanovi = Clan.objects.get(ClanId=clanovi_data['ClanId'])
        clanovi_serializer = ClanSerializers(clanovi, data=clanovi_data)
        if clanovi_serializer.is_valid():
            clanovi_serializer.save()
            return JsonResponse("Dodano uspesno", safe=False)
        return JsonResponse("Neuspesno", safe=False)

    elif request.method == 'DELETE':
        clanovi = Clan.objects.get(ClanId=id)
        clanovi.delete()
        return JsonResponse("Izbrisano uspesno", safe=False)
