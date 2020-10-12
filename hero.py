from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import io
import csv
import mysql.connector
import datetime
from datetime import timedelta
import schedule
import time
import random
import json
import requests
import http.client 
from base64 import b64encode


app = Flask(__name__)

db = mysql.connector.connect(
        host="localhost",
        user="id15103051_root",
        passwd="Ilovetheworld@99",
        database="id15103051_kudzi"
    )
mycursor = db.cursor()

DOWNLOAD_DIRECTORY = '.\img'


@app.route("/sms", methods=["GET", "POST"])

def sms_reply():

    un = request.form.get('From')

    reformed = un.replace("whatsapp:", "")

    messages = []

    users = []

    msg = request.form.get('Body')

    
    resp = MessagingResponse()

    csv_file=csv.reader(open('users.csv','r'))

    #Huvuru intergration section
    if "*2000*" in msg:

        un1 = request.form.get('From')

        reformed2 = un1.replace("whatsapp:+", "")

        wes = random.randint(1,29999)

        ref = "ref" + str(wes)

        eco = msg.replace("*2000*","")

        conn = http.client.HTTPSConnection("api.huvuru.com")

        userAndPass = b64encode(b"132:Hv_lpk_0Hwh9CFt8fxigz4BsOTW6KpdY5f633f9de8055").decode("ascii")

        headers = { 'Authorization' : 'Basic %s' %  userAndPass }

        conn.request('POST', '/v1/payments/initialize?ecocash=' + eco + '&email=wmambinge@gmail.com&environment=live&currency=ZWL&amount=40&reference=' + ref + '&returnUrl=https://wa.me/' + reformed2,headers=headers)

        res = conn.getresponse()

        data = res.read()

        data.decode("utf-8")

        sta_data = data.decode("utf-8")

        

        if sta_data == data.decode("utf-8"):

            resp.message("Your payment is being processed\n*Transaction processing might take up to 15 minutes,  please be patient...*")

            return str(resp)

        

    if "*2100*" in msg:

        un1 = request.form.get('From')

        reformed2 = un1.replace("whatsapp:+", "")

        wes = random.randint(1,29999)

        ref = "ref" + str(wes)

        eco = msg.replace("*2000*","")

        conn = http.client.HTTPSConnection("api.huvuru.com")

        userAndPass = b64encode(b"132:Hv_lpk_0Hwh9CFt8fxigz4BsOTW6KpdY5f633f9de8055").decode("ascii")

        headers = { 'Authorization' : 'Basic %s' %  userAndPass }

        conn.request('POST', '/v1/payments/initialize?ecocash=' + eco + '&email=wmambinge@gmail.com&environment=live&currency=ZWL&amount=270&reference=' + ref + '&returnUrl=https://wa.me/' + reformed2,headers=headers)

        res = conn.getresponse()

        data = res.read()

        data.decode("utf-8")

        

        if sta_data == data.decode("utf-8"):

            resp.message("Your payment is being processed\n*Transaction processing might take up to 15 minutes,  please be patient...*")

            return str(resp)

    if "*2200*" in msg:

        un1 = request.form.get('From')

        reformed2 = un1.replace("whatsapp:+", "")

        wes = random.randint(1,29999)

        ref = "ref" + str(wes)

        eco = msg.replace("*2000*","")

        conn = http.client.HTTPSConnection("api.huvuru.com")

        userAndPass = b64encode(b"132:Hv_lpk_0Hwh9CFt8fxigz4BsOTW6KpdY5f633f9de8055").decode("ascii")

        headers = { 'Authorization' : 'Basic %s' %  userAndPass }

        conn.request('POST', '/v1/payments/initialize?ecocash=' + eco + '&email=wmambinge@gmail.com&environment=live&currency=ZWL&amount=972&reference=' + ref + '&returnUrl=https://wa.me/' + reformed2,headers=headers)

        res = conn.getresponse()

        data = res.read()

      

        if sta_data == data.decode("utf-8"):

            resp.message("Your payment is being processed\n*Transaction processing might take up to 15 minutes,  please be patient...*")

            return str(resp)
    
    #end of intergration section

    
    while True:

        #Greeting messages section

        if msg.lower() == "hi":

            mycursor.execute("SELECT name,number FROM subscribers WHERE number='%s'" %reformed)
            myresi = mycursor.fetchall()

            for r in myresi:
                if reformed in r[1]:
                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf10
                
                        idcf10 = idc[0]
                    resp.message('Welcome back ' + str(r[0]))
                    
                    df = resp.message("_______________________\n*-ZIMBABWE-*\n*PROPERTY CLASSIFIEDS.*\n_______________________\nWelcome to Zimbabwe’s LITE classifieds for properties. Covering Houses, industrials, shops, stands, farms, hospitality.\n*Rentals, Sales and accommodation Bookings.*\n \n*S1*: View Houses to rent\n*S2*:  View Commercial/Shops to rent \n*S3*: View Farms to rent\n*S4*: View Industrials to rent\n*S5*:View Houses for sale\n*S6*:View Shops for sale\n*S7*:View Industrials for sale\n*S8*:View Farms for sale\n*S9*:View Stands for Sale\n*S10*:Request Valuation Service\n*S11*:HOLIDAY ACCOMMODATION\n*S12*:HOLIDAY ACCOMMODATION FOR SALE\n \n_______________________\n*PROPERTY ADVERTISERS*\nIf you wish to upload a property kindly send UPL1 or follow\n https://wa.me/263774767325?text=UPL1\n_______________________\nTo subscribe to regular morning news on property investments and tips, send SUBS1 or follow\nhttps://wa.me/263774767325?text=SUBS1")
                    df.media(idcf10)
                    return str(resp)
            resp.message("_______________________\n*-WELCOME-*\n*PROPERTY ADVERTS.*\n_______________________\nGreetings\n\nThis is C-Lite Zimbabwe. Would you kindly give me your name so that I recognise you every time we chat :-)\n\n*Simply enter* *name Full Name\n\n*Example>* *name Grace Chiwocha")
            return str(resp)

        #Normal registration section
   
        if "*name" in msg:

            mycursor.execute("SELECT img FROM headimg")
                                
            imgg = mycursor.fetchall()

            for idc in imgg:
                global idcf12


                idcf12 = idc[0]

            mycursor.execute("SELECT img1 FROM headimg")
                                
            imgg1 = mycursor.fetchall()

            for idc in imgg1:
                global idcf13


                idcf13 = idc[0]

            nam = msg.replace("*name", "")

            start_day = datetime.datetime.now()
            plus1 = start_day + timedelta(days=4)
            sqli = "INSERT INTO subscribers (name, number, reg_time, status) VALUES (%s, %s, %s, %s)"
            vali = (nam, reformed, plus1, "paid")
            mycursor.execute(sqli, vali)

            db.commit()

            de = resp.message("_______________________\n*-WELCOME-*\n*PROPERTY ADVERTS.*\n_______________________\nThank you, %s\n\nCongratulations! You have been awarded 4 days of free access to the prime services. Proceed to explore our services in this chatbot.\n\n*Use the following format to subscribe now:*\n*2000*your Ecocash number# - Daily Sub $10ZWL\n*2100*your Ecocash number – Weekly Sub $40ZWL\n*2200*your Ecocash number# Monthly Sub $90ZWL"%nam)
            de.media(idcf12)
            dd = resp.message("(thd)e to meet you %s\n\n_______________________\n*-ZIMBABWE-*\n*PROPERTY CLASSIFIEDS.*\n_______________________\nWelcome to Zimbabwe’s LITE classifieds for properties. Covering Houses, industrials, shops, stands, farms, hospitality.\n*Rentals, Sales and accommodation Bookings.*\n \n*S1*: View Houses to rent\n*S2*:  View Commercial/Shops to rent \n*S3*: View Farms to rent\n*S4*: View Industrials to rent\n*S5*:View Houses for sale\n*S6*:View Shops for sale\n*S7*:View Industrials for sale\n*S8*:View Farms for sale\n*S9*:View Stands for Sale\n*S10*:Request Valuation Service\n \n_______________________\n*PROPERTY ADVERTISERS*\nIf you wish to upload a property kindly send UPL1 or follow\n https://wa.me/263774767325?text=UPL1\n_______________________\nTo subscribe to regular morning news on property investments and tips, send SUBS1 or follow\nhttps://wa.me/263774767325?text=SUBS1"%(nam))
            dd.media(idcf13)
            return str(resp)

        #Listing section

        if msg.lower() == "sr":

            mycursor.execute("SELECT img FROM headimg")
                                
            imgg = mycursor.fetchall()

            for idc in imgg:
                global idcf11
        
                idcf11 = idc[0]

            mycursor.execute("SELECT img1 FROM headimg")
                                
            imgg1 = mycursor.fetchall()

            for idc in imgg1:
        
                idcf15 = idc[0]

            dc = resp.message("_______________________\n*-ZIMBABWE-*\n*PROPERTY CLASSIFIEDS.*\n_______________________\nWelcome to Zimbabwe’s LITE classifieds for properties. Covering Houses, industrials, shops, stands, farms, hospitality.\n*Rentals, Sales and accommodation Bookings.*\n \n*S1*: View Houses to rent\n*S2*:  View Commercial/Shops to rent \n*S3*: View Farms to rent\n*S4*: View Industrials to rent\n*S5*:View Houses for sale\n*S6*:View Shops for sale\n*S7*:View Industrials for sale\n*S8*:View Farms for sale\n*S9*:View Stands for Sale\n*S10*:Request Valuation Service\n \n_______________________\n*PROPERTY ADVERTISERS*\nIf you wish to upload a property kindly send UPL1 or follow\n https://wa.me/263774767325?text=UPL1\n_______________________\nTo subscribe to regular morning news on property investments and tips, send SUBS1 or follow\nhttps://wa.me/263774767325?text=SUBS1")
            dc.media(idcf11)
            return str(resp)
        if msg.upper() == "SUBS1":
            mycursor.execute("SELECT img1 FROM headimg")
                                
            imgg1 = mycursor.fetchall()

            for idc in imgg1:
        
                idcf15 = idc[0]

            dt = resp.message("*In order to view detailed info and be able to commu(thd)ate with the advertisers directly.*\n_______________________\n*Use the following format to subscribe now:*\n*2000*your Ecocash number - Daily Sub $10ZWL\n*2100*your Ecocash number – Weekly Sub $40ZWL\n*2200*your Ecocash number Monthly Sub $90ZWL")
            dt.media(idcf15)
            return str(resp)

        
        if request.method =="POST":

            #Advert viewing section
            
            if msg.upper() == "S1":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                myresult = mycursor.fetchall()

                resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                S1_list = [] 

                str1 = "\n"              

                for row in myresult:

                    S1_list.append("*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n")

                    real = str1.join(S1_list)

                    
                mycursor.execute("SELECT img FROM headimg")
                                
                imgg = mycursor.fetchall()

                for idc in imgg:
                    global idcf100
                
                    idcf100 = idc[0]
                sq = resp.message(real)
                sq.media(idcf100)
                   
                return str(resp) 

            if msg.upper() == "S2":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S2_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S2_list.append(intiu)

                        real2 = str1.join(S2_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf101
                    
                        idcf101 = idc[0]
                    sq = resp.message(real2)
                    sq.media(idcf101)    
                        
                    return str(resp)
                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)
            if msg.upper() == "S3":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S3_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S3_list.append(intiu)

                        real3 = str1.join(S3_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf102
                    
                        idcf102 = idc[0]
                    sq = resp.message(real3)
                    sq.media(idcf102)

                    return str(resp)  
                
                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)

            if msg.upper() == "S4":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S4_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S4_list.append(intiu)

                        real4 = str1.join(S4_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf103
                    
                        idcf103 = idc[0]
                    sq = resp.message(real4)
                    sq.media(idcf103)
                    return str(resp) 
                
                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)

            if msg.upper() == "S5":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S5_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S5_list.append(intiu)

                        real5 = str1.join(S5_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf104
                    
                        idcf104 = idc[0]
                    sq = resp.message(real5)
                    sq.media(idcf104)
                    return str(resp)

                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)  

            if msg.upper() == "S6":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S6_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S6_list.append(intiu)

                        real6 = str1.join(S6_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf105
                    
                        idcf105 = idc[0]
                    sq = resp.message(real6)
                    sq.media(idcf105)
                    return str(resp)

                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)

            if msg.upper() == "S7":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S7_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S7_list.append(intiu)

                        real7 = str1.join(S7_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf106
                    
                        idcf106 = idc[0]
                    sq = resp.message(real7)
                    sq.media(idcf106)
                    return str(resp) 

                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp) 

            if msg.upper() == "S8":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S8_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S8_list.append(intiu)

                        real8 = str1.join(S8_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf107
                    
                        idcf107 = idc[0]
                    sq = resp.message(real8)
                    sq.media(idcf107)
                    return str(resp)

                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)  

            if msg.upper() == "S9":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S9_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S9_list.append(intiu)

                        real9 = str1.join(S9_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf108
                    
                        idcf108 = idc[0]
                    sq = resp.message(real9)
                    sq.media(idcf108) 
                    return str(resp)

                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)

            if msg.upper() == "S11":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S11_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S11_list.append(intiu)

                        real11 = str1.join(S11_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf109
                    
                        idcf109 = idc[0]
                    sq = resp.message(real11)
                    sq.media(idcf109) 
                    return str(resp) 

                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)

            if msg.upper() == "S12":
                messages.append(msg)
                with io.open("messages.csv", "a", encoding="utf-8") as f1:
                    f1.write(str(messages))
                try:
                    mycursor.execute("SELECT code,location,price,date FROM advert WHERE adcode='%s'" %msg.upper())
                    myresult = mycursor.fetchall()

                    resp.message("Wait your information is loading\nEnter Advert code to view more details about the advert")  

                    S12_list = [] 

                    str1 = "\n"              

                    for row in myresult:


                        intiu = "*Advert Code* :" + row[0] + "\n" + "*Location* :" + row[1] + "\n" + row[2] +  "\n" + row[3] + "\n" + "\n"

                        S12_list.append(intiu)

                        real12 = str1.join(S12_list)

                    mycursor.execute("SELECT img FROM headimg")
                                
                    imgg = mycursor.fetchall()

                    for idc in imgg:
                        global idcf1011
                    
                        idcf1011 = idc[0]
                    sq = resp.message(real12)
                    sq.media(idcf1011) 
                    return str(resp) 

                except UnboundLocalError:

                    resp.message("*Oops* This advert code is still empty\nsend *SR* to return to main menu and try another one")

                    return str(resp)                

            if msg.upper() == "UPL1":

                mycursor.execute("SELECT img FROM headimg")
                                
                imgg = mycursor.fetchall()

                for idc in imgg:
                    global idcf1012
                    
                    idcf1012 = idc[0]
                sq = resp.message("_______________________\n*-UPLOADING- PROPERTY ADVERT.*\n_______________________\n*550 : Uploading Houses to RENT\n*560 : Uploading Commercial/Shops to RENT\n*570 : Uploading Farm to RENT\n*580 : Uploading Industrial to RENT\n*590 : Uploading Short Stay Accommodation\n_______________________\n*650 : Uploading Houses for SALE\n*660 : Uploading Commercial/Shops for SALE\n*670 : Uploading Farm for SALE\n*680 : Uploading Industrial for SALE\n*690 : Uploading Holiday Accommodation for SALE\n*540 : Uploading stand for SALE")
                sq.media(idcf1012)

                return str(resp)

            if "PR" in msg.upper():

                mycursor.execute("SELECT reg_time FROM subscribers WHERE number='%s' " % reformed)      
                mytime = mycursor.fetchall()
                cur_date = datetime.datetime.now()

                for the_time in mytime:
                        
                    format = "%Y-%m-%d %H:%M:%S.%f"
                    here = datetime.datetime.strptime(the_time[0], format)

                    if cur_date >= here:

                        mycursor.execute("UPDATE subscribers SET status='unpaid' WHERE number='%s'" %reformed)

                        db.commit()

                mycursor.execute("SELECT * FROM subscribers WHERE status = 'paid'")
                
                result = mycursor.fetchall()

                mycursor.execute("SELECT * FROM subscribers WHERE status = 'unpaid'")
                
                results = mycursor.fetchall()
                
                for row in result:

                    if reformed in row:

                        messages.append(msg)
                        with io.open("messages.csv", "a", encoding="utf-8") as f1:

                            f1.write(str(messages))

                        mycursor.execute("SELECT code, price, details, extras, location, date, whatsapp, img FROM advert WHERE code='%s' " % msg.upper())
                                
                        myresult = mycursor.fetchall()

                        resp.message("Advert loading...")


                        for row in myresult:



                            sr = resp.message("*Advert Code* : "+row[0] + "\n" + row[1] + "\n" + "*Details* : "+row[2] + "\n" + "*Extras* : "+row[3] + "\n" + row[4] + "\n" + row[5] + "\n" + "*Agent link* : "+row[6]+"?text=I%20am%20interested%20in%20your%20advert%20with%20code:%20"+row[0] + "\n\n\n" + "Enter *S1* to return to *Houses to rent*")
                            sr.media(row[7])

                        return str(resp)

                for i in results:

                    if "unpaid" in i:

                        resp.message("Ooops … . It looks like you forgot something! To view this section , please update your subscription . It could have expired.\n_______________________\nIn order to view detailed info and commu(thd)ate with the advertiser directly, you need to be subscribed.\n*Use the following format:*\n*2000*your Ecocash number# - Daily Sub\n*2100*your Ecocash number – Weekly Sub\n*2200*your Ecocash number# Monthly Sub\n_______________________\n*If you are seeing this message whilst you are fully subscribed, kindly report to*\nhttps://wa.me/263734277826?text=Hi,%20%20I%20am%20having%20problems%20viewing%20adverts%20the%20section,%20can%20you%20check%20for%20me\nPlease accept our sincere apologies")

                return str(resp)
           
            

            #Agent registration Process
            ###########################
            ###########################
            ###########################
            ###########################

            if msg.upper() == "*550*1":

                resp.message("_______________________\n*ADVERTISER*\n*REGISTRATION PROCESS*\n_______________________\nTo advertise Y ou are required to register as an advertiser  To register, please enter the following code and your informatio\n*REG Full Name\n*Example* *REG John Hoko")
                
                return str(resp)

            if "*REG" in msg.upper():

                ag = msg.upper().replace("*REG", "")

                agcd = random.randint(1,2999)

                agcod = "AG" + str(agcd)

                sq = "INSERT INTO agents (name,agentcode,number) VALUES (%s,%s,%s)"
                val0 = (ag, agcod, reformed)
                mycursor.execute(sq, val0)

                db.commit()

                resp.message("_______________________\n*ADVERTISER*\n*REGISTRATION PROCESS*\n_______________________\nThank you %s,  Now enter *120 together with your National ID\n*Example* *120 63-21223-D-63"%ag)
                
                return str(resp)

            if "*120" in msg.upper():

                idn = msg.upper().replace("*120", "")

                mycursor.execute("UPDATE agents SET idnumber='%s' WHERE number = '%s'" %(idn,reformed))

                db.commit()

                resp.message("_______________________\n*ADVERTISER*\n*REGISTRATION PROCESS*\n_______________________\nWonderful! ID recorded successfully, Now enter *121 together with your residential address\n*Example* *121  14 Mopani Avenue Glen Norah, Harare")

                return str(resp)

            if "*121" in msg.upper():

                addre = msg.upper().replace("*121", "")

                mycursor.execute("UPDATE agents SET address='%s' WHERE number = '%s'" %(addre,reformed))

                db.commit()

                resp.message("_______________________\n*ADVERTISER*\n*REGISTRATION PROCESS*\n_______________________\nWonderful! address recorded successfully, Now enter tag *IMG to your ID image\n*Example* take a photo of your ID from this chat and add the text *IMG then press send.")

                return str(resp)
            
            if "*IMG" in msg.upper():

                image_urli = request.values['MediaUrl0']

                mycursor.execute("UPDATE agents SET image='%s' WHERE number='%s'" %(image_urli,reformed))
                
                db.commit()

                resp.message("_______________________\n*ADVERTISER*\n*REGISTRATION PROCESS*\n_______________________\nWonderful! ID image recorded successfully\nNow enter tag *IMES to your image\nTake a current picture of yourself and attach *IMES to image")

                return str(resp)

            if "*IMES" in msg.upper():
    
                image_urlii = request.values['MediaUrl0']

                mycursor.execute("UPDATE agents SET smage='%s' WHERE number='%s'" %(image_urlii,reformed))
                
                db.commit()

                resp.message("_______________________\n*End of REGISTRATION PROCESS*\n_______________________\nYour registration is complete enter *550 to start uploading")

                return str(resp)

            ###########################
            ###########################
            ###########################
            ###########################
            #end of registration process

            if msg == "SaGeNtS":

                mycursor.execute("SELECT name, agentcode, number, idnumber, address, image, smage FROM agents")
                                
                myresulto = mycursor.fetchall()

                


                for rowo in myresulto:



                    sre = resp.message("*Advertiser Name* : "+rowo[0] + "\n" "*Advertiser Code* : "+ rowo[1] + "\n" + "*Advertiser Number* : "+rowo[2] + "\n" + "*ID number* : "+rowo[3] + "\n" + "*Advertiser Address* : "+rowo[4])
                    sre.media(rowo[5])

                    srre = resp.message("Advertiser Picture" + "\n" + "*Advertiser Name* : "+rowo[0] + "\n" "*Advertiser Code* : "+ rowo[1])
                    srre.media(rowo[6])
                    

                return str(resp)


            #Uploading houses for rent section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*550":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S1"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                            
                            idrow = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*HOUSE TO RENT ADVERT*\n______________________\n\nIn case you will need to correct an error\n\nChoose appropriate code for your amendments\n\n155*%s*Location of property\n\n156*%s*Details of property\n\n157*%s*Rent for property\n\n158*%s*Extra facilities/amenities\n\n159*%s* upload best picture"%(idrow,idrow,idrow,idrow,idrow))

                        resp.message("_______________________\n*UPLOADING*\n*HOUSE TO RENT ADVERT*\n______________________\n\nThank you, Your advert code %s\n\nNow to add location\n155*%s*Location of Property\n*Example* 155*%s*Harare, Borrowdale\n156*%s*Details of property\n157*%s*Rent for property\n158*%s*Extra facilities/amenities\n159*%s* upload best picture" %(cod,idrow,idrow,idrow,idrow,idrow,idrow))
                        
                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)



            if "155*" in msg:
    
                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]





                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSE TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n156*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "156*" in msg:

                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSE TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n157*%s*$500USD per month"%the_id)
                
            
                return str(resp)


            if "157*" in msg:
                    
                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSE TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n158*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "158*" in msg:
                        
                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSE TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 159*%s* to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "159*" in msg:

                initial = 2
                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*HOUSE TO RENT ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)

             ##########################
            ##########################
            ##########################
            #end of house for rent upload section



            
            #Uploading Commercial/Shops for rent section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*560":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S2"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                            
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*Commercial/Shops TO RENT ADVERT*\n______________________\n\nIn case you will need to correct an error\n\nChoose appropriate code for your amendments\n\n165*%s*Location of property\n\n166*%s*Details of property\n\n167*%s*Rent for property\n\n168*%s*Extra facilities/amenities\n\n169*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*Commercial/Shops TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n165*%s*Location of Property\n*Example* 165*%sHarare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)
                        

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)


            if "165*" in msg:

                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Commercial/Shops TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n166*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "166*" in msg:

                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]


                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Commercial/Shops TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n167*%s*$500USD per month"%the_id)
                
            
                return str(resp)


            if "167*" in msg:

                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]
                    
                

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Commercial/Shops TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n168*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "168*" in msg:

                initial = 2
                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Commercial/Shops TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 169*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "169*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*Commercial/Shops TO RENT ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)

             ##########################
            ##########################
            ##########################
            #end of commercial / shops for rent upload section



            #Uploading Industrial for rent section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*580":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S4"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:

                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*Industrial TO RENT ADVERT*\n______________________\n\nIn case you will need to correct an error\n\nChoose appropriate code for your amendments\n\n175*%s*Location of property\n\n176*%s*Details of property\n\n177*%s*Rent for property\n\n178*%s*Extra facilities/amenities\n\n179*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*Industrial TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n175*%s*Location of Property\n*Example* 175*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)
 


            if "175*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Industrial TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n176*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "176*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]


                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Industrial TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n177*%s*$500USD per month"%the_id)
                
            
                return str(resp)


            if "177*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Industrial TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n178*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "178*" in msg:
                        
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Industrial TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 179*%s*to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "179*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*Industrial TO RENT ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)

             ##########################
            ##########################
            ##########################
            #end of Industrial for rent upload section



            #Uploading Farm for rent section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*570":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S3"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:

                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*Farm TO RENT ADVERT*\n______________________\n\nIn case you will need to correct an error\nChoose appropriate code for your amendments\n\n185*%s*Location of property\n\n186*%s*Details of property\n\n187*%s*Rent for property\n\n188*%s*Extra facilities/amenities\n\n189*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*Farml TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n185*%s*Location of Property\n*Example* 185*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)


            if "185*" in msg:
    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Farm TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n186*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "186*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Farm TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n187*%s*$500USD per month"%the_id)
                
            
                return str(resp)


            if "187*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]


                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Farm TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n188*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "188*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*Farm TO RENT ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 189*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "189*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*Farm TO RENT ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)

             ##########################
            ##########################
            ##########################
            #end of Farm for rent upload section



            #Uploading HOUSES FOR SALE section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*650":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S5"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                            
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*HOUSES FOR SALE ADVERT*\n______________________\n\nIn case you will need to correct an error\nChoose appropriate code for your amendments\n\n195*%s*Location of property\n\n196*%s*Details of property\n\n197*%s*Rent for property\n\n198*%s*Extra facilities/amenities\n\n199*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*HOUSES FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n195*%s*Location of Property\n*Example* 195*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)

            if "195*" in msg:
    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSES FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n196*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "196*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSES FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n197*%s*$500USD per month"%the_id)
                
            
                return str(resp)


            if "197*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSES FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n198*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "198*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOUSES FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 199*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "199*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*HOUSES FOR SALE ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)

             ##########################
            ##########################
            ##########################
            #end of Houses for sale upload section



            #Uploading COMMERCIAL/SHOPS FOR SALE section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*660":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S6"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                            
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*COMMERCIAL/SHOPS FOR SALE ADVERT*\n______________________\n\nIn case you will need to correct an error\nChoose appropriate code for your amendments\n\n145*%s*Location of property\n\n146*%s*Details of property\n\n147*%s*Rent for property\n\n148*%s*Extra facilities/amenities\n\n149*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*COMMERCIAL/SHOPS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n145*%s*Location of Property\n*Example* 145*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)


            if "145*" in msg:
    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*COMMERCIAL/SHOPS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n146*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "146*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*COMMERCIAL/SHOPS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n147*%s*$500USD per month"%the_id)
                
            
                return str(resp)


            if "147*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*COMMERCIAL/SHOPS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n148*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "148*" in msg:
                        
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*COMMERCIAL/SHOPS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 149*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "149*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*COMMERCIAL/SHOPS FOR SALE ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)

             ##########################
            ##########################
            ##########################
            #end of COMMERCIAL/SHOPS upload section



            #Uploading INDUSTRIALS FOR SALE section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*680":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S7"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                    
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*INDUSTRIALS FOR SALE ADVERT*\n______________________\n\nIn case you will need to correct an error\nChoose appropriate code for your amendments\n\n135*%s*Location of property\n\n136*%s*Details of property\n\n137*%s*Rent for property\n\n138*%s*Extra facilities/amenities\n\n139*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*INDUSTRIALS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n135*%s*Location of Property\n*Example* 135*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)


            if "135*" in msg:
    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*INDUSTRIALS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n136*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "136*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*INDUSTRIALS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n137*%s*$500USD per month"%the_id)
                
            
                return str(resp)


            if "137*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*INDUSTRIALS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n138*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "138*" in msg:
                        
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*INDUSTRIALS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 139*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "139*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*INDUSTRIALS FOR SALE ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)

             ##########################
            ##########################
            ##########################
            #end of INDUSTRIALS FOR SALE upload section



            #Uploading FARM FOR SALE section
             ##########################
            ##########################
            ##########################

            if msg.upper() == "*670":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S8"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                            
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*FARM FOR SALE ADVERT*\n______________________\n\nIn case you will need to correct an error\nChoose appropriate code for your amendments\n\n125*%s*Location of property\n\n126*%s*Details of property\n\n127*%s*Rent for property\n\n128*%s*Extra facilities/amenities\n\n129*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*FARM FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n125*%s*Location of Property\n*Example* 125*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)


            if "125*" in msg:
    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*FARM FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n126*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "126*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*FARM FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n127*%s*$500USD"%the_id)
                
            
                return str(resp)


            if "127*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*FARM FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n128*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "128*" in msg:
                        
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*FARM FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 129*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "129*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*FARM FOR SALE ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)
            
            ##########################
            ##########################
            ##########################
            #end of FARM FOR SALE upload section



            

            #Uploading STANDS FOR SALE section
            ##########################
            ##########################
            ##########################

            if msg.upper() == "*540":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S9"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                            
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*STANDS FOR SALE ADVERT*\n______________________\n\nIn case you will need to correct an error\nChoose appropriate code for your amendments\n\n115*%s*Location of property\n\n116*%s*Details of property\n\n117*%s*Rent for property\n\n118*%s*Extra facilities/amenities\n\n119*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*STANDS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n115*%s*Location of Property\n*Example* 115*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)



            if "115*" in msg:
    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*STANDS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n116*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "116*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*STANDS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n117*%s*$500USD"%the_id)
                
            
                return str(resp)


            if "117*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*STANDS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n118*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "118*" in msg:
                        
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*STANDS FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 119*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "119*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*STANDS FOR SALE ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)
            
            ##########################
            ##########################
            ##########################
            #end of STANDS FOR SALE upload section


            #Uploading HOLIDAY ACCOMMODATION section
            ##########################
            ##########################
            ##########################

            if msg.upper() == "*590":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S11"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                        
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION ADVERT*\n______________________\n\nIn case you will need to correct an error, just enter\n\n%s\n\nThen choose appropriate code for your amendments\n\n160*%s*Location of property\n\n161*%s*Details of property\n\n162*%s*Rent for property\n\n163*%s*Extra facilities/amenities\n\n164*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n160*%s*Location of Property\n*Example* 160*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)

          


            if "160*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n161*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "161*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n162*%s*$500USD"%the_id)
                
            
                return str(resp)


            if "162*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n163*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "163*" in msg:
                        
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 164*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "164*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]


                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*HOLIDAY ACCOMMODATION ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)
            
            ##########################
            ##########################
            ##########################
            #end of HOLIDAY ACCOMMODATION upload section


            #Uploading HOLIDAY ACCOMMODATION FOR SALE section
            ##########################
            ##########################
            ##########################

            if msg.upper() == "*690":

                mycursor.execute("SELECT number FROM agents")
                                
                agn = mycursor.fetchall()

                mycursor.execute("SELECT number FROM agents")
                                
                ang = mycursor.fetchall()

                for bn in agn:

                    if reformed in bn:

                        n = random.randint(1,99999)
                        cur_date = datetime.datetime.now()
                        cod = "PR" + str(n)
                        reform = un.replace("whatsapp:", "")
                        num = reform.replace("+", "")
                        link = "https://wa.me/" + str(num)
                        adcod = "S12"
                        newdate = "*Date posted* : " + cur_date.strftime("%d-%b-%Y (%H:%M:%S)")

                        sql = "INSERT INTO advert (number_id, date, whatsapp, code, adcode) VALUES (%s, %s, %s, %s, %s)"
                        val = (reformed, newdate, link, cod, adcod)
                        mycursor.execute(sql, val)

                        db.commit()

                        mycursor.execute("SELECT id FROM advert WHERE code = '%s'"%cod)
                
                        re = mycursor.fetchall()
                        
                        for c in re:
                            
                            the_id = str(c[0])

                        resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION FOR SALE ADVERT*\n______________________\n\nIn case you will need to correct an error, just enter\n\n%s\n\nThen choose appropriate code for your amendments\n\n165*%s*Location of property\n\n166*%s*Details of property\n\n167*%s*Rent for property\n\n168*%s*Extra facilities/amenities\n\n169*%s upload best picture"%(the_id,the_id,the_id,the_id,the_id))

                        resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\n\nYour advert code %s\n\nNow to add location\n165*%s*Location of Property\n*Example* 165*%s*Harare, Borrowdale" %(cod,the_id,the_id))

                        return str(resp)

                resp.message("Inorder to upload you need to register as an advertiser first\nEnter *550*1 to start registration process")
                return str(resp)


            if "150*" in msg:
    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn10 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET location='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn10,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit details *Example*\n151*%s*A Duplex Flat \nFirst Floor - 4 Bedrooms, Main en-suite, two bath-toilet with showers, living room. \nGround Floor - Modern fitted kitchen, lounge, dinning, and double lock-up garage"%the_id)
                
            
                return str(resp)
                   
            if "151*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn1 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET details='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn1,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit price *Example*\n152*%s*$500USD"%the_id)
                
            
                return str(resp)


            if "152*" in msg:
                    
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn2 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET price='%s' WHERE id='%s' AND number_id='%s'" %("*Price* : " + msg_turn2,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nNow to add/edit extras if any*Example*\n153*%s*Solar power, Bolehole, swimming pool etc"%the_id)

                return str(resp)

            if "153*" in msg:
                        
                initial = 2

                the_id = msg.split('*')[initial-1]

                msg_turn3 = msg.split('*')[initial]

                mycursor.execute("UPDATE advert SET extras='%s' WHERE id='%s' AND number_id='%s'" %(msg_turn3,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*UPLOADING*\n*HOLIDAY ACCOMMODATION FOR SALE ADVERT*\n______________________\n\nThank you information successfully uploaded\nIf you wish to attach an image to you advert\nAttach 154*%s to image and send\n*Enter SR to return to main menu* "%the_id)

                return str(resp)

            if "154*" in msg:

                initial = 2

                the_id = msg.split('*')[initial-1]

                image_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE advert SET img='%s' WHERE id='%s' AND number_id='%s'" %(image_url,the_id,reformed))
                db.commit()

                resp.message("_______________________\n*END OF UPLOAD*\n*HOLIDAY ACCOMMODATION FOR SALE ADVERT*\n______________________\n\nThanks for the image!\nYour Advert has been successfully placed\nTo view it enter your advert code\n*Enter SR to return to main menu* ")

                return str(resp)
            
            ##########################
            ##########################
            ##########################
            #end of HOLIDAY ACCOMMODATION FOR SALE upload section


               

            if "*LOGOS1" in msg:
    
                img_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE headimg SET img = '%s' WHERE id = '1'"%img_url)
                db.commit()

                resp.message("DONE!")

                return str(resp)

            if "*BANNERS1" in msg:
        
                img_url = request.values['MediaUrl0']
                mycursor.execute("UPDATE headimg SET img1 = '%s' WHERE id = '1'"%img_url)
                db.commit()

                resp.message("DONE!")

    
                return str(resp) 



@app.route("/response", methods=["GET", "POST"])

def response():

    account_sid = 'ACe0f2a11ce63bac299e2db3dba4944759'
    auth_token = '5614da80d6bdcdaeea826bfc3fd818ab'
    client = Client(account_sid,auth_token)

    from_whatapp_number='whatsapp:+14155238886'
    #to_whatsapp_number='whatsapp:+263714349795'

    #client.messages.create(body='You did it',
    #                       from_=from_whatapp_number,
    #                       to=to_whatsapp_number)

    resp = MessagingResponse()

    un = request.form.get('From')
    
    json_res = request.get_json(force=True)

    print(json_res)

    json_explanation = json_res['explanation']

    print(json_explanation)

    json_load = json_res['trans_load']

    json_amount = json_load['amount']

    send_number = json_load['returnUrl']

    to_whatsapp_number = send_number.replace("https://wa.me/","whatsapp:+")

    data_number = send_number.replace("https://wa.me/","+")

    print(to_whatsapp_number)

    print(data_number)


    if json_explanation == 'Paid':

        if json_amount =="972":

            start_date = datetime.datetime.now()

            plus = start_date + timedelta(days=30)

            mycursor.execute("UPDATE subscribers SET reg_time='%s' WHERE number='%s'" %(plus,data_number))

            db.commit()
                
            mycursor.execute("UPDATE subscribers SET status='paid' WHERE number='%s'" %(data_number))

            db.commit()

            client.messages.create(body='*Thank you Monthly Subscribtion successfully paid*\nEnter *SR* to return to main menu',
                                   from_=from_whatapp_number,
                                   to=to_whatsapp_number)

        if json_amount =="270":

            start_date = datetime.datetime.now()

            plus = start_date + timedelta(days=7)

            mycursor.execute("UPDATE subscribers SET reg_time='%s' WHERE number='%s'" %(plus,data_number))

            db.commit()
                
            mycursor.execute("UPDATE subscribers SET status='paid' WHERE number='%s'" %(data_number))

            db.commit()

            client.messages.create(body='*Thank you Weekly Subscribtion successfully paid*\nEnter *SR* to return to main menu',
                                   from_=from_whatapp_number,
                                   to=to_whatsapp_number)

        if json_amount =="40":

            start_date = datetime.datetime.now()

            plus = start_date + timedelta(hours=24)

            mycursor.execute("UPDATE subscribers SET reg_time='%s' WHERE number='%s'" %(plus,data_number))

            db.commit()

            mycursor.execute("UPDATE subscribers SET status='paid' WHERE number='%s'" %(data_number))

            db.commit()

            client.messages.create(body='*Thank you Daily Subscribtion successfully paid*\nEnter *SR* to return to main menu',
                                   from_=from_whatapp_number,
                                   to=to_whatsapp_number)

    else:

        if json_explanation == "FAILED":

            client.messages.create(body='This transaction was unsuccessful',
                                   from_=from_whatapp_number,
                                   to=to_whatsapp_number) 

          


if __name__ == "__main__":
    app.run(debug=True)