from django.http import HttpResponse
from django.shortcuts import render
import hashlib
import json
import base64
import hello.registr
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import hello.session
from hello.faceid import face_id
from hello.face_id_auth import face_auth
from django.http import JsonResponse


def Info_reg_Client(request):
    user_type = 'client'
    pib = request.POST.get('PIB')
    Login = request.POST.get('Login')
    Number = request.POST.get('Num')
    Password = request.POST.get('Passw')
    
    h_log = hashlib.sha256(str(Login).encode('utf - 8')).hexdigest()
    h_pas = hashlib.sha256(str(Password).encode('utf - 8')).hexdigest()
    hello.session.Add_user(request,h_log)
    if (hello.registr.registr_vik(user_type, pib, h_log, h_pas, Number)==True):
        return render(request, 'faceid.html')
    
def Info_reg_Operation(request):
    user_type = 'operation'
    pib = request.POST.get('PIB')
    Login = request.POST.get('Login')
    Number = request.POST.get('Num')
    Password = request.POST.get('Passw')
    
    h_log = hashlib.sha256(str(Login).encode('utf - 8')).hexdigest()
    h_pas = hashlib.sha256(str(Password).encode('utf - 8')).hexdigest()

    hello.session.Add_user(request,h_log)
    if (hello.registr.registr_vik(user_type, pib, h_log, h_pas, Number)==True):
        return render(request, 'faceid.html')

    #return HttpResponse(f'Користувач: {user_type}\nПІБ: {pib}\nLogin: {Login}\n Password: {Password}')
   
def Get_photo(request):
    h_log = request.session.get('user')
   
    data = json.loads(request.body)
    img_data = data.get('image', '')
    img_data = img_data.split(',')[1]
    image_data = base64.b64decode(img_data)
    photo = ContentFile(image_data, name='uploaded_photo.png')
    default_storage.save(f'{h_log}.jpg', ContentFile(photo.read()))
    return JsonResponse({'success': True}, status=200)
def Get_photo_auth(request):
    h_log = request.session.get('user')
    print(h_log)
    data = json.loads(request.body)
    img_data = data.get('image', '')
    img_data = img_data.split(',')[1]
    image_data = base64.b64decode(img_data)
    photo = ContentFile(image_data, name='uploaded_photo.png')
    default_storage.save(f'{h_log}.jpg', ContentFile(photo.read()))
    # resp = face_auth(h_log)
    resp = True
    if resp:
        return JsonResponse({'success': True}, status=200)
    else:
        return JsonResponse({'success': False, 'error_message': 'Some error occurred'}, status=400)
def Add_key(request):
    h_log = request.session.get('user')
    
    with open(f'{h_log}.json') as f:
        data = json.load(f)
        key = data['kfd']
        face_id(h_log, key)

    return render(request, 'getkey.html')

    #foto = request.FILES['photo']

