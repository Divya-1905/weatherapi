from ast import Param
from msilib.schema import AppId
from multiprocessing import context
from pydoc import describe
from re import search
from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.
def signup(request):    
    if request.method =='POST':
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        appid='23e36f6f810f3dfe837247868f001879'
        data = request.POST.get('city')
        print(request.POST)
        PARAMS = {'q':data,'appid':appid,'units':'metric'}
        res = requests.get(url=URL,params=PARAMS).json()
        print(res)
        description = res['weather'][0]['description']
        daily = res['sys']['sunrise']
        pressure= res['main']['pressure']
        humidity = res['main']['humidity']
        name = res['name']
        context = {'description':description,'daily':daily,'presure':pressure,'humidity':humidity,'city':name}
        return render(request,'weatherapi/index.html',context)  
    return render(request,'weatherapi/index.html')