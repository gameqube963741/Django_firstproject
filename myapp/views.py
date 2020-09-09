from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random  # 加入 random 套件


# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django!")

def hello2(request,username):
    return HttpResponse("Hello " + username)
   
def hello3(request,username):
    now=datetime.now()
    return render(request,"hello3.html",locals())
   
def hello4(request,username):
    now=datetime.now()
    return render(request,"hello4.html",locals())
   
def dice(request):
    no1=random.randint(1,6)   # 1~6
    no2=random.randint(1,6)   # 1~6
    no3=random.randint(1,6)   # 1~6
    # 使用 locals()傳遞所有的區域變數 
    return render(request,"dice.html",locals())   

def show(request):
    person1={"name":"Edward","phone":"0977-177-998","age":29}
    person2={"name":"Mike","phone":"02-25099933","age":21}
    person3={"name":"Howhow","phone":"0911-886-885","age":31}
    persons=[person1,person2,person3]
    return render(request,"show.html",locals())

def djget(request):
    name = request.GET['name']
    city = request.GET['city']
    return render(request,"djget.html",locals())

def djpost(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username=='admin' and password=='0000':
            return HttpResponse('歡迎到此一遊！')
        else:
            return HttpResponse('帳號或密碼錯誤！')
    else:
        return render(request,"djpost.html",locals())



