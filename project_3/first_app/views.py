from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={'Author':'Riyad','age':14,'lst':['ryaan','is','pro','Fucker'],'val':'','datetime':datetime.datetime.now(),'courses':
    [{'name':'C',
    'price':300,
    'author':'Riyad'},
    {'name':'Python',
    'price':400,
    'author':'Fuead'},
    {'name':'C++',
    'price':500,
    'author':'Munni'}
    ]}
    return render(request,'home.html',d)
