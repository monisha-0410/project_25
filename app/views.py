from django.shortcuts import render
from app.models import *
# Create your views here.
def display_country(request):
    QLCO=Country.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_country.html',d)


def display_capital(request):
    QLcO=Capital.objects.all()
    d={'QLcO':QLcO}
    return render(request,'display_capital.html',d)


def insert_country(request):
    id=int(input('enter the country_id:'))
    n=input('Enter the country name:')
    p=int(input('Enter the population:'))
    nco=Country.objects.get_or_create(Country_id=id,Country_Name=n,population=p)[0]
    nco.save()
    QLCO=Country.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_country.html',d)

def insert_capital(request):
    id=int(input('enter the capital_id:'))
    c=int(input('enter the country_id:'))
    n=input('Enter the Capital name:')
    DO=Country.objects.get(Country_id=c)
    NCO=Capital.objects.get_or_create(Capital_Id=id,capital_name=n,Country_id=DO)[0]
    NCO.save()
    QLcO=Capital.objects.all()
    d={'QLcO':QLcO}
    return render(request,'display_capital.html',d)
