import sqlite3
from cryptography.fernet import Fernet
import json
from hello.rsa_create import key_pare
from hello.sign_f import sign
key = Fernet.generate_key().decode('utf - 8')



def registr_vik(user_type, pib, h_log, h_pas, Number ):
    data = {
        "PIB": pib,
        "kfd": key,
        "Number":Number

    }
    con = sqlite3.connect('hack.db')
    curs = con.cursor()

    js_obj = json.dumps(data, indent=4)
    with open(f'{h_log}.json', 'w') as f:
        f.write(js_obj)
    entities = [pib, h_log, h_pas, Number, user_type]
    curs.execute("INSERT INTO uslog(PIB,Login,Password,Num,User) VALUES(?,?,?,?,?)", entities)
    con.commit()
    priv_pem,pub_pem = key_pare()
    with open(f'{h_log}_priv.pem', 'wb') as f:
        f.write(priv_pem)
    with open(f'{h_log}_pub.pem', 'wb') as f:
        f.write(pub_pem)
    sign(h_log)
    return True







