##########################
#This code was created for fun
#currently is running on my Raspberry pi 3 b+
##########################
#!/usr/bin/env python

import os
import time
#time.sleep(10)
import datetime
import MySQLdb
import socket
import psutil
import urllib.request
import sys


global c
global db
global directory

directory = "/home/jan/Plocha/log"
try:
    os.mkdir(directory)
except:
    pass



def Watch():
    timer = (datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"))
    date = (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d"))
    return(timer, date)

def Logger(text, var):
    timer, date = (Watch())
    log=open("%s/log-%s.txt" %(directory, date), "a+")
    log.write("%s - %s - %s\n" % (date, timer, text))
    log.close()
    if var == 1:
        log=open("%s/log_error-%s.txt" %(directory, date), "a+")
        log.write("%s - %s - %s\n" % (date, timer, text))
        log.close()
    else:
        pass
    #return

def CPU():
    try:
        cpu_temp = os.popen('vcgencmd measure_temp').readline()
        cpu_temp = cpu_temp.replace("temp=","").replace("'C\n","")
        cpu_use = psutil.cpu_percent()
    except:
        Logger("read CPU NOK",1)
    else:
        Logger("read CPU OK",0)
        return(cpu_temp, cpu_use)

def Connection():
    world = '8.8.8.8'
    router = '192.168.0.1'
    #timeout = 2
    resp_world = os.system("ping -c 1 -w 1 " + world + " > /dev/null 2>&1")
    if resp_world == 0:
        #socket.settimeout(3)
        #socket.create_connection(("www.google.com", 80))
        #urllib.request.urlopen(url, timeout = timeout )
        net_status = "Connected"
        router_status = "Connected"
        mode = 1
        Logger("net and router connection OK",0)
    else:
        net_status = "Disconnected"
        mode = 2
        resp_router = os.system("ping -c 1 -w 1 " + router + " > /dev/null 2>&1")
        if resp_router == 0:
            mode = 3
            router_status = "Connected"
            Logger("net connection NOK ; router connection OK",1)
        else:
            mode = 4
            router_status = "Disconnected"
            Logger("net connection NOK ; router connection NOK",1)
        #os.system('sh /home/jan/Dokumenty/wifi_reconnect.sh')
        #time.sleep(6)
    return(net_status, router_status, mode)

def connect_db():
    try:
        db = MySQLdb.connect("localhost","xxx","xxx","xxx_SERVER")
        c= db.cursor()
    except:
        Logger("Connect to db NOK",1)
        status = False

    else:
        Logger("Connect to db OK",0)
        status = True

    return(status, c, db)

def insert_to_db():
    try:
        timer, date = (Watch())
        net_status, router_status, mode = (Connection())
        cpu_temp, cpu_use= (CPU())
        #print(str(cpu_temp) + " - " + date + " - " + timer + " - " + str(cpu_use) + " - " + net_status + " - " + router_status + " - " + str(mode))
        sql =  "INSERT INTO SERVER_TAB (CPU_Temp, CPU_Date, CPU_Time, CPU_Use, NET_Status, ROUTER_Status, W_Mode) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    except:
        Logger("insert do db NOK",1)
        return
    else:
        Logger("insert to db OK",0)
    try:
        c.execute(sql,( float(cpu_temp) , str(date), str(timer), float(cpu_use), str(net_status), str(router_status), int(mode)))
        db.commit()
    except:
        db.rollback()
        #db.close()
        Logger("execute sql NOK",1)
    else:
        Logger("execute sql OK",0)
    return

def read_from_db():
    try:
        #c.execute("SELECT * FROM TAB_CPU WHERE ID = (SELCET MAX(ID) FROM TAB_CPU)")
        c.execute("SELECT * FROM SERVER_TAB ORDER BY ID DESC LIMIT 1")
        result = c.fetchall()
        if result[0][0] >=43200 :  #43 200-> den ; 302 400-> tyden ; 1 296 000-> 30 dnu  ;; 2sek interval
            sql = "TRUNCATE TABLE SERVER_TAB"
            c.execute(sql)
        #if result is not None:
         #x   print ('CPU temperature: ' , result[0][1], '| time: ' , result[0][3], ' | date: ' , result[0][2], '| CPU use: ' , result[0][4], '| NET status: ' , result[0][5],
           #        'Router status: ' , result[0][6], ' | mode: ', result[0][7])
    except:
        Logger("read from db NOK",1)
    else:
        Logger("read from db OK",0)
    return

def main():
    while 1:
        Logger("while start NOW -----------------------",0)
        insert_to_db()
        #read_from_db()
        time.sleep(2)
        Logger("while end NOW -------------------------\n",0)

if __name__ == '__main__':

    Logger("####################### first run ##################",0)
    status, c, db = (connect_db())
    while status == False:
        status = (connect_db())

    try:
        main()
    except KeyboardInterrupt:
        Logger("End of script #############################\n\n",1)
    else:
        Logger("Main byl spusten\n",1)
        pass
