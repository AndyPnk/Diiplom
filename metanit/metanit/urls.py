from django.contrib import admin
from django.urls import path
from hello import views
from hello import models

urlpatterns = [

    path('', views.Index),
    path('register', views.Reg),
    path('LogIn', views.LogIn),
    path('get_user', views.Get_user),
    path('userTypeClient', models.Info_reg_Client),
    path('userTypeOperation', models.Info_reg_Operation),
    path('upload_photo', models.Get_photo),
    path('upload_photo_auth', models.Get_photo_auth),
    path('getkey', models.Add_key),
    path('addFile1',views.addFile1),
    path('kab', views.Kab),
    path('user_opr', views.User_oper),
    path('table_opr', views.Table_oper),
    path('add_post', views.Ad_post)
]



