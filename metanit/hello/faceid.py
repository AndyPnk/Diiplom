import pyAesCrypt
import cv2
import os
import sqlite3

def face_id(h_log, key):
    im_2 = open(f'hello/media/{h_log}.jpg', 'rb')
    b_photo = im_2.read()
    with open(f'{h_log}.jpg', 'wb') as f:
        f.write(b_photo)
    im_2.close()
    pyAesCrypt.encryptFile(
        f'{h_log}.jpg',
        f'{h_log}.jpg.rtx',
        key,
        bufferSize=128 * 1024
    )
    
    with open(f'{h_log}.jpg.rtx', 'rb') as f:
         enc_ph = f.read()
         con = sqlite3.connect('hack.db')
         curs = con.cursor()
         curs.execute("UPDATE uslog SET FOTO = ? WHERE Login = ?", (enc_ph, h_log))
         con.commit()
    
    os.remove(f'hello/media/{h_log}.jpg')
    os.remove(f'{h_log}.jpg.rtx')
    os.remove(f'{h_log}.jpg')
