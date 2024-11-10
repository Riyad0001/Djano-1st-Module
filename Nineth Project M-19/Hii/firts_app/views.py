from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

def home(request):
    response= render(request,'home.html')
    response.set_cookie('name','rohim')
    response.set_cookie('name','riyad',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'cookies.html',{'name':name})

def delet_cookie(request):
    response= render(request,'del.html')
    response.delete_cookie('name')
    return response

def set_season(request):
    data={
        'name':'Riyad',
        'age':'12',
        'Language':'Bangla'
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request,'home.html')

def get_season(request):
    if 'name' in request.session:
        name=request.session.get('name')
        age=request.session.get('age')
        Language=request.session.get('Language')
        request.session.modified=True
        return render(request,'get_session.html',{'name':name,'age':age,'Language':Language})
    else:
        return HttpResponse("Your session is expired.Please Login Again")

def delete_session(request):
    request.session.flush()
    return render(request,'del_s.html')


