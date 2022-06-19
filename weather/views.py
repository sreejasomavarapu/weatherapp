from django.shortcuts import render
import requests
# Create your views here.
from . forms import WeatherForm

def home(request):
    city=''
    form =WeatherForm()
    if request.method=='POST':
        form =WeatherForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('name')
    
            url ='https://api.openweathermap.org/data/2.5/weather?q={}&appid=52020e0c85ec1bd3be2d55489e2245d8'
            #city ='Hyderabad'
            r=requests.get(url.format(city)).json()
            #print(r.text)
            context ={
                    'temperature' : r['main']['temp'],
                    'description' : r['weather'][0]['description'],
                    'icon' : r['weather'][0]['icon'],
                    'form':form
            }
            print(context)
            return render(request,'weather/home.html',context)
    else:
        return render(request,'weather/home.html',{'form':form})