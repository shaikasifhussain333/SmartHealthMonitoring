import requests
import json
from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='*******'
app.config['MYSQL_DB']='********'

mysql=MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        details=request.form
        fname=details["fname"]
        lname=details['lname']
        email=details['email']
        mobile_no=details['mobile']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO appointments (FirstName, LastName, Email, Mobile) VALUES (%s, %s, %s, %s)", (fname,lname,email,mobile_no))
        mysql.connection.commit()
        cur.close()
    return render_template('index.html')

@app.route('/home', methods=['GET','POST'])
def home():
    return redirect('/')


@app.route('/upload')
def upload():
    cur=mysql.connection.cursor()
    r=requests.get('***get data from thingspeak URL****')
    data=r.json()
    id=data['feeds'][0]['field1']
    heartbeat=data['feeds'][0]['field2']
    temp=data['feeds'][0]['field3']
    humid=data['feeds'][0]['field4']
    CO=data['feeds'][0]['field5']
    CO2=data['feeds'][0]['field6']
    cur.execute("UPDATE Patients SET Heartbeat= %s, Temperature= %s , Humidity= %s , CO_level= %s , CO2_level= %s WHERE Patient_ID= %s",(heartbeat,temp,humid,CO,CO2,id))
    #cur.execute(sql,val)
    #cur.execute("INSERT INTO Patients(Patient_ID,Heartbeat,Temperature,Humidity,CO_level,CO2_level) VALUES(%s,%s,%s,%s,%s,%s)",(id,heartbeat,temp,humid,CO,CO2))
    mysql.connection.commit()
    cur.close()
    return render_template('upload.html',data=data)

@app.route('/database')
def database():
    cur=mysql.connection.cursor()
    resultValue= cur.execute("SELECT * FROM Patients")
    if resultValue>0:
        userDetails = cur.fetchall()
        #print(userDetails)
    #result=cur.execute("SELECT * FROM appointments")
    if resultValue>0:
        appdetails = cur.fetchall()
        return render_template('database.html',userDetails=userDetails,appdetails=appdetails)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/chart")
def chart():
    cur=mysql.connection.cursor()
    resultValue= cur.execute("SELECT * FROM Patients")
    if resultValue>0:
        data = cur.fetchall()
    return render_template('chart.html',data=data)

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/doctor',methods=['GET','POST'])
def doctor():
    if request.method=='POST':
        return redirect('/database')
    return render_template('doctor.html')

@app.route('/plots')
def plots():
    return redirect('/database')

if __name__=="__main__":
 app.run(debug=True)
