from flask import Flask, render_template, request, url_for, redirect
#from flask_mysqldb import MySQL
app = Flask(__name__)

'''

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'slots'

mysql = MySQL(app)
'''
bays = ['A','B','C','D','E','F','G','H','I']
s= ['1','2','3','4','5','6','7','8','9']
slots =[]
for i in range(len(bays)):
    for j in range(len(s)):
        slots.append(bays[i] + s[j])
print(slots)
@app.route('/')
def hello():
    
    '''curr= mysql.connection.cursor()
    booked = curr.execute("SELECT * FROM slots")
    booked = list(curr.fetchall())
    for i in range(len(booked)):
        booked[i] = booked[i][0]'''
    booked = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'F6']
    
    return render_template('landing.html', slots=slots, booked = booked, l= len(booked))

@app.route('/update', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        slot = details['fname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO slots(SlNo, slot, vno, brand) VALUES (10, %s)", [firstNam])
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/updation', methods=['POST'])
def updation():
        details = request.form
        slot = details['slot']
        vno = details['vno']
        brand = details['brand']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO slots(slot, vno, brand) VALUES (%s, %s, %s)", [slot, vno, brand])
        mysql.connection.commit()
        cur.close()
        return redirect('/')


@app.route('/deletion', methods=['POST'])
def update():
        details = request.form
        slot = details['deslot']
    #    length = details['length']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM slots WHERE slot = %s", [slot])
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
