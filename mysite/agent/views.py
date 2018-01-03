from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    print('agent/view')
    return render(request,'agent/index.html')



def all(request):
    return HttpResponse("mine request ")

