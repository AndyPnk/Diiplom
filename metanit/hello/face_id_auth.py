import cv2
# import dlib
import pyAesCrypt
import os 
import json
import sqlite3
from scipy.spatial import distance
def face_auth(h_log):
    con = sqlite3.connect('hack.db')
    curs = con.cursor()
    uid = h_log
    f = open(f'{uid}.json')
    data = json.load(f)
    passw = data['kfd']
    sql_fetchone_photo = f"""SELECT FOTO from uslog where Login == '{h_log}'"""
    curs.execute(sql_fetchone_photo)
    photo = curs.fetchone()[0]
    if photo is not None:
        with open(f'{uid}.jpg.rtx', 'wb') as f:
            f.write(photo)
    else:
        print(f"Зображення для користувача {h_log} не знайдено.")
    pyAesCrypt.decryptFile(
        f'{uid}.jpg.rtx',
        f'{uid}1.jpg',
        passw,
        bufferSize=128 * 1024
    )
    sp = dlib.shape_predictor('hello/shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('hello/dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()
    im_1 = cv2.imread(f'hello/media/{h_log}.jpg')
    face_1 = detector(im_1, 1)
    shape = sp(im_1, face_1[0])
    face_descriptor_1 = facerec.compute_face_descriptor(im_1, shape)
    im_2 = cv2.imread(f'{uid}1.jpg')
    face_2 = detector(im_2, 1)
    shape = sp(im_2, face_2[0])
    face_descriptor_2 = facerec.compute_face_descriptor(im_2, shape)
    result = distance.euclidean(face_descriptor_1, face_descriptor_2)
    if result < 0.55:
        os.remove(f"{uid}1.jpg")
        os.remove(f"hello/media/{uid}.jpg") 
        return True
    else:
        os.remove(f'{uid}1.jpg')
        os.remove(f'hello/media/{uid}.jpg')
        return False
        
