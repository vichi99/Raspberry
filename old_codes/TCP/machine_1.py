#!/usr/bin/python
import socket
import RPi.GPIO as GPIO
import os
import sys
import time
print("try")
BUFFER_SIZE = 4
GPIO.cleanup()
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
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.output(4,0)
GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)

while True:
    try:
        print("while prvni")
        GPIO.setup(23,GPIO.IN,GPIO.PUD_DOWN)
        y=1
        print("while ceka na signal z plc, az bude 23 true")
        if GPIO.wait_for_edge(23,GPIO.RISING):#po prijmuti signalu posle do PC signal pro snimani
                #je treba v plc nastavit aby hodil ihned po tomto signalu z aretace false na 23 a zase pri aretaci nastavil true
                print("if G23 je true a spojujem se s pc")
                GPIO.output(4,0)
                GPIO.output(17,0)
                GPIO.output(27,0)
                GPIO.output(22,0)
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
                  GPIO.output(4,1)
                else:
                  GPIO.output(4,0)
                if dat[1] == "1":
                  GPIO.output(17,1)
                else:
                  GPIO.output(17,0)
                if dat[2] == "1":
                  GPIO.output(27,1)
                else:
                  GPIO.output(27,0)
                if dat[3] == "1":
                  GPIO.output(22,1)
                else:
                  GPIO.output(22,0)
                print("svetla")
                y=0
    except:
        print("Except")
