from django.shortcuts import render
from django.http import HttpResponse
from .models import places
from .models import peoples
#


# Create your views here.
def func(request):
    #return HttpResponse("Hello World")
    obj = places.objects.all()
    p_obj=peoples.objects.all()
    return render(request,'index.html',{'data':obj,'p_data':p_obj})

#def passingval(request):
   # name='Fathih'
   # return render(request,'passval.html',{'sm':name})
#def getentry(request):
   #return render(request,'getval.html')
#def addition(request):
    #x=int(request.GET['n1'])
    #y=int(request.GET['n2'])
    #result=x+y
    #return render(request,'result.html',{'result':result})
#def index(request):
    #return render(request,'index.html')