import random
import urllib.request
import time
BaseURL= "***thingspeak URL***"

while True:
    PatientID=random.randint(2,4)
    heartbeat=random.uniform(60,100)
    temp=random.uniform(97,105)
    humid=random.uniform(30,70)
    CO=random.uniform(10,40)
    CO2=random.uniform(300,1000)
    print("Sending data to Thingspeak....... ")
    print("Patient ID      :- %d" % (PatientID),end="\n")
    print("Heartbeat level :- %2.2f" % (heartbeat),end="\n")
    print("Temperature     :- %2.2f" % (temp),end="\n")
    print("Humidity        :- %2.2f" %(humid),end="\n")
    print("CO Level        :- %2.2f" %(CO),end="\n")
    print("CO2 Level       :- %2.2f" %(CO2),end="\n")
    conn=urllib.request.urlopen(BaseURL+"&field1=%d" %(PatientID) +"&field2=%2.2f" %(heartbeat) + "&field3=%2.2f" %(temp) + "&field4=%2.2f" %(humid) + "&field5=%2.2f" %(CO) + "&field6=%2.2f" %(CO2))
    print(conn.read)
    conn.close
    print("\t data sent successfully")
    time.sleep(20)
