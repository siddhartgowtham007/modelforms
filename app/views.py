from django.shortcuts import render
from app.forms import *

# Create your views here.


def insert(request):
    ETFO=Topic()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=Topic(request.POST)
        if TFDO.is_valid():
            TFDO.save()

    return render(request,'insert.html',d)