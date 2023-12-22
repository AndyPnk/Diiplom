
import sqlite3
import hashlib


def auth(log, pas):
    con = sqlite3.connect('hack.db')
    curs = con.cursor()
    h_log = hashlib.sha256(str(log).encode('utf - 8')).hexdigest()
    h_pas = hashlib.sha256(str(pas).encode('utf - 8')).hexdigest()
    curs.execute(
        f"SELECT * from uslog WHERE Login = '{h_log}' AND Password = '{h_pas}'")
    row = curs.fetchone()
    if row:
        return True
    else:
        return False