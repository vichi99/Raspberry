#!/usr/bin/python
import socket
import RPi.GPIO as GPIO
import os
import sys
import time
#import serial
print("try")
BUFFER_SIZE = 4
#GPIO.cleanup()
#Client-pro odesilani.Je zadana cilova IP adresa
TCP_IP = '0.0.0.0'
TCP_PORT = 8881


#Server-pro prijem. Je zadana Raspberry IP adresa
TCP_IPS = '0.0.0.0'
TCP_PORTS = 8882
q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
q.bind((TCP_IPS, TCP_PORTS))


MESSAGE = "1"
print("try2")

GPIO.setmode(GPIO.BCM)

filename1 = "/sys/class/gpio/gpio55"
filename2 = "/sys/class/gpio/gpio56"
filename3 = "/sys/class/gpio/gpio57"
filename4 = "/sys/class/gpio/gpio58"
filename5 = "/sys/class/gpio/gpio59"
filename6 = "/sys/class/gpio/gpio60"
filename7 = "/sys/class/gpio/gpio61"
filename8 = "/sys/class/gpio/gpio62"

try:
    with open("/sys/class/gpio/export", mode='w') as f:
        f.write("55")
    print("export")
except: pass
try:
    with open("/sys/class/gpio/gpio55/direction", mode='w') as f:
        f.write("out")
    print("direction")
except: pass

try:
    with open("/sys/class/gpio/export", mode='w') as f:
        f.write("56")
    print("export")
except: pass
try:
    with open("/sys/class/gpio/gpio56/direction", mode='w') as f:
        f.write("out")
    print("direction")
except: pass



try:
    with open("/sys/class/gpio/export", mode='w') as f:
        f.write("57")
    print("export")
except: pass
try:
    with open("/sys/class/gpio/gpio57/direction", mode='w') as f:
        f.write("out")
    print("direction")
except: pass



try:
    with open("/sys/class/gpio/export", mode='w') as f:
        f.write("58")
    print("export")
except: pass
try:
    with open("/sys/class/gpio/gpio58/direction", mode='w') as f:
        f.write("out")
    print("direction")
except: pass





while True:
    try:
        print("while prvni")
        GPIO.setup(12,GPIO.IN,GPIO.PUD_DOWN)
        y=1
        print("while ceka na signal z plc, az bude 23 true")
        if GPIO.wait_for_edge(12,GPIO.RISING):#po prijmuti signalu posle do PC signal pro snimani
                #je treba v plc nastavit aby hodil ihned po tomto signalu z aretace false na 23 a zase pri aretaci nastavil true
                print("if G23 je true a spojujem se s pc")
                try:
                    with open("/sys/class/gpio/gpio55/value", mode='w') as f:
                        f.write("0")
                except: pass
                try:
                    with open("/sys/class/gpio/gpio56/value", mode='w') as f:
                        f.write("0")
                except: pass
                try:
                    with open("/sys/class/gpio/gpio57/value", mode='w') as f:
                        f.write("0")
                except: pass
                try:
                    with open("/sys/class/gpio/gpio58/value", mode='w') as f:
                        f.write("0")
                except: pass

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((TCP_IP, TCP_PORT))
                s.send(MESSAGE.encode())
                #s.close()
        while y>0:#smycka, ktera ceka na prijem vyhodnoceni z PC
                print("while cekame na prijem z pc ")

                q.listen(1)
                conn, adress = q.accept()
                data = conn.recv(BUFFER_SIZE)
                dat=data.decode("ascii")
                #zde jsou nastaveny vystupy z Raspberry do plc, ktere sitky jsou ok ci nikoliv
                #0 = spatna sitka
                if dat[0] == "1":
                    try:
                        with open("/sys/class/gpio/gpio55/value", mode='w') as f:
                            f.write("1")
                    except: pass
                else:
                    try:
                        with open("/sys/class/gpio/gpio55/value", mode='w') as f:
                            f.write("0")
                    except: pass
                if dat[1] == "1":
                    try:
                        with open("/sys/class/gpio/gpio56/value", mode='w') as f:
                            f.write("1")
                    except: pass
                else:
                    try:
                        with open("/sys/class/gpio/gpio56/value", mode='w') as f:
                            f.write("0")
                    except: pass
                if dat[2] == "1":
                    try:
                        with open("/sys/class/gpio/gpio57/value", mode='w') as f:
                            f.write("1")
                    except: pass
                else:
                    try:
                        with open("/sys/class/gpio/gpio57/value", mode='w') as f:
                            f.write("0")
                    except: pass
                if dat[3] == "1":
                    try:
                        with open("/sys/class/gpio/gpio58/value", mode='w') as f:
                            f.write("1")
                    except: pass
                else:
                    try:
                        with open("/sys/class/gpio/gpio58/value", mode='w') as f:
                            f.write("0")
                    except: pass
                print("svetla")
                y=0
    except:
        print("Except")
