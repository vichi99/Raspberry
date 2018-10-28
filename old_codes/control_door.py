#!/usr/bin/python3.4
#####
# this code has been successfully tested on Raspberry 3b
#####

import socket
import RPi.GPIO as GPIO
import os
import sys
import time
import smtplib


#zadejte cas intervalu v sekundach
limit = 120

#Nastaveni komunikace
IP = '0.0.0.0'
PORT = 25
odesilatel = 'xxx@xxx.cz'
prijemce = 'xxx@xxx.cz'

#predmet a text odesilajiciho mailu
PREDMET = "Otevřené dveře, Hlavní vchod E"
TEXT = "Prosím zkontrolujte dovření dveří, Hlavní vchod E. Dveře jsou otevřené déle než 2 minuty."

header = 'To:' + prijemce + '\n' + 'From: ' + odesilatel + '\n' + 'Subject: {}\n\n{}'.format(PREDMET,TEXT)


#nastaveni boardu a pinu snimace dveri
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


#vytvoreni log souboru
filename = "/home/pi/Desktop/log.txt"
if os.path.isfile(filename):
    #print("existujem")#soubor neexistuje
    print("soubor existuje")
else:
    os.makedirs(os.path.dirname(filename),exist_ok=True)
    print("soubor neexistuje")


from time import localtime, strftime
t = strftime("\n%d %b %Y %a, %H:%M:%S",localtime())
with open(filename,"a") as f:
    f.write(t + "  Raspberry se zapnulo \n")

while True:
    #print("kontrola dveri")
    GPIO.output(24,0)
    time.sleep(1)
    if GPIO.input(23)!=1: #zacne snimat kdyz jsou dvere otevreny
        #time.sleep(1)
        GPIO.output(24,1)
        start=time.time() #zacina stopovat cas
        #print("stopuji")

        #ulozi informace do souboru log
        from time import localtime, strftime
        t = strftime("\n%d %b %Y %a, %H:%M:%S",localtime())
        with open(filename,"a") as f:
            f.write(t + "  Dvere se otevrely \n")

        a = 1 #deklaruje vystup z whilu nize pri uzavreni dveri
        while a > 0 :
            #print("cekam na zavreni")
            end=time.time()
            if GPIO.input(23) == 1: #po zavreni dveri opusti tento while
                a = 0
            time.sleep(1)
            z=(end-start) #pocita cas od doby otevreni dveri
            if z > limit :
                #print(z)
                start = start + limit # dekalaruje cas startu, aby se email posilal ve stejnem intervalu jako cas deklarovany pro upozorneni
                try: #zkusi poslat email
                    mail = smtplib.SMTP(IP,PORT)
                    mail.ehlo()
                    #mail.starttls()
                    #mail.login()
                    mail.sendmail(odesilatel,prijemce,header.encode('ISO-8859-2'))
                    mail.close

                    #ulozi informace do souboru log
                    from time import localtime, strftime
                    t=strftime("\n%d %b %Y %a, %H:%M:%S",localtime())
                    with open(filename,"a") as f:
                        f.write(t + "  Dvere jsou otevreny dele nez je limit -> odeslan mail \n")

                    #print("bylo otevreno vic nez limit a posilam mail  %.2f" %z)
                except: #v pripade poruchy provede
                    from time import localtime, strftime
                    t=strftime("\n%d %b %Y %a, %H:%M:%S",localtime())
                    with open(filename,"a") as f:
                        f.write(t + "  Nepodarilo se poslat mail \n")
                    #print("except email")
            #print("%.2f" %z)
