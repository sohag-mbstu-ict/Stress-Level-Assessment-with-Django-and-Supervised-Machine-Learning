from django.shortcuts import render
from django.http import HttpResponse
import joblib
import datetime
from . models import Destination
# Create your views here.

def index(request):
    dest=Destination.objects.all()
    return render(request,'index.html',{'dest':dest})

def DTL(request):
    in_="Sohag Hossain"
    today_date = datetime.datetime.now().date()
    #https://stackoverflow.com/questions/53383602/what-is-block-content-and-endblock-content-for-in-django
    return render(request,'home.html',{'date':today_date})

def test(request):
    return render(request,'test.html')

def RESULT(request):
    #filename=open("static/Stress_Detection_model.sav")
    loaded_model = joblib.load("static/Stress_Detection_model.sav")

    snoring=request.POST.get('snoring')
    respiration=request.POST.get('respiration')
    temperature=request.POST.get('temperature')
    limb=request.POST.get('limb')
    blood=request.POST.get('blood')
    eye=request.POST.get('eye')
    sleep=request.POST.get('sleep')
    heart=request.POST.get('heart')

    print("snoring : ",snoring)
    newData = [[float(snoring),float(respiration),float(temperature),float(limb),float(blood),float(eye),float(sleep),float(heart)]]
    result=loaded_model.predict(newData)
    
    print("result  :   ",result)
    return render(request,'result.html', {"result2":int(result)})
