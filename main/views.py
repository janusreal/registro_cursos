from django.shortcuts import render, HttpResponse
from main.services import *

# Create your views here.

def test(req):
    c = crear_curso('','','')
    return HttpResponse('ok')

    crear_estudiante('12121','',)