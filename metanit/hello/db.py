import sqlite3


def Get_dashboard(request):
    conn = sqlite3.connect('hack.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM log')
    row = cursor.fetchall()
    list = []

    for i in row:
        cursor.execute("SELECT * FROM log WHERE id=?", (i))
        date = cursor.fetchone()
        db = {
            'Name': date[1],
            'TypeCar': date[2],
            'TypeStorage':date[3],
            'StartPoint':date[4],
            'EndPoint':date[5],
            'Cost':date[6],
            'NumCar':date[7],
        } 
        list.append(db)
    #cursor.close()
    #conn.close()
    return list
def User_Type(request):
    h_log =  request.session.get('user')
    
    conn = sqlite3.connect('hack.db')
    cursor = conn.cursor()
    cursor.execute("SELECT User FROM uslog WHERE Login=?", (str(h_log),))
    date = cursor.fetchall()
    request.session['type'] = date[0]
    #cursor.close()
    #conn.close()
    
    