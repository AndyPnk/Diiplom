from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.http import FileResponse
import hello.session
import hashlib
import hello.auth
import hello.db
import sqlite3


def Index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f"IP адреса клієнта: {ip}")
    return render(request, 'index.html')
    


def Reg(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f"Домен: {request.META.get('USERDOMAIN')}\nМобіл. пристрій: {request.META.get('HTTP_SEC_CH_UA_MOBILE')}\nПк. пристрій: {request.META.get('HTTP_SEC_CH_UA_PLATFORM')}")
    print(f"IP адреса клієнта: {ip}")
    return render(request, 'SignUp.html')

def LogIn(request):
    return render(request, "LogIn.html")

def Get_user(request):
    login = request.POST.get("login")
    passw = request.POST.get("pass")
    h_log = hashlib.sha256(str(login).encode('utf - 8')).hexdigest()
    
    hello.session.Add_user(request, h_log)
    resp = hello.auth.auth(login, passw)
    print(resp)
    if resp == True:
        return render(request, 'face_id_auth.html')
    else:
        return render(request, 'LogIn.html')
    

def addFile1(request):
    hello.session.Check_session(request)
    h_log = request.session.get('user')
    print(h_log)
    file_path = f'{h_log}.json'
    with open(file_path, 'rb') as file:
        f = file.read()
        response = FileResponse(f)
        response['Content-Disposition'] = f'attachment; filename={h_log}".json"'
        return response
    #dat = db.conect(request)
    #request.session['user'] = login
    #return render(request, "kab.html", {'date': dat})

def Kab(request):
    hello.session.Check_session(request)
    hello.db.User_Type(request)
    user = request.session.get('type')
    print(user[0])
    if user[0] == 'client':
        return render(request, 'customer.html')
    else:
        data = hello.db.Get_dashboard(request)
        return render(request, 'dashboard.html', {'data': data})
#
def User_oper(request):
    hello.session.Check_session(request)
    h_log = request.session.get('user')
    return render(request, 'user.html')

def Table_oper(request):
    hello.session.Check_session(request)
    h_log = request.session.get('user')
    return render(request, 'table.html')

def Ad_post(request):
    hello.session.Check_session(request)
    h_log = request.session.get('user')
    con = sqlite3.connect('hack.db')
    curs = con.cursor()
    entities = ['Паливо', request.POST.get('type'), 'Критичний', request.POST.get('start'),request.POST.get('end'),request.POST.get('cost'), request.POST.get('num'), h_log]
    curs.execute("INSERT INTO log(Name,TypeCar,TypeStorage,StartPoint,EndPoint,Cost,NumCar, Login) VALUES(?,?,?,?,?, ?, ?,?)", entities)
    con.commit()
    return render(request,'customer.html')




    
    

    
        
    