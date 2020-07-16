

import socket
from _thread import *
from datetime import datetime
import random




serverName = ''
serverPort = 13000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serverSocket.bind((serverName, serverPort))
except socket.error as e:
    print(str(e))

print('Serveri u startua ne localhost:' + str(serverPort))
serverSocket.listen(10)
print('Serveri eshte i gatshem te pranoj kerkesa')




def IPADDRESS():
    return str(addr[0])


def PORT():
    return str(addr[1])


def COUNT(tekstiDhene):
    zanore = ['A', 'a', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    z = 0
    b = 0
    for i in str(tekstiDhene):
        if i in zanore:
            z += 1
        elif (i >= 'a' and i <= 'z') or (i > 'A' and i <= "Z"):
            b += 1

    return "Teksti ka " + str(z) + " zanore dhe " + str(b) + " bashketingellore"


def GAME():
    arr = (random.sample(range(1, 35), 5))
    arr.sort()
    return str(arr)


def REVERSE(str):
    s = str.strip()
    reversed = ""
    indeksi = len(s)
    while indeksi > 0:
        reversed += s[indeksi - 1]
        indeksi = indeksi - 1
    return reversed


def PALINDROME(string):
    if (string == string[::-1]):
        return "True"
    else:
        return "False"


def GCF(a, b):
    if a % b == 0:
        return b
    return GCF(b, a % b)


def CONVERT(s, gjatesia):
    s=s.lower()
    if (s == "cmtofeet"):
        return round(gjatesia * 0.0328084,3)
    elif (s == "feettocm"):

        return round(gjatesia * 30.48,3)
    elif (s == "kmtomiles"):

        return round(gjatesia * 0.621371,3)
    elif (s == "milestokm"):
        return round(gjatesia * 1.60934,2)
    else:
        return "Lloji i konvertimit gabim. Shtyp cmtofeet, feettocm ,kmtomiles ose milestokm"


def PAGANETO(bruto, kontributi):
    if bruto < 0:
        return "Paga nuk mund te jete me e vogel se 0"
    elif kontributi > 15 or kontributi < 5:
        return "Kontributi pensional duhet te jete mes 5% dhe 15%"
    else:
        bruto1 = bruto - ((kontributi / 100) * bruto)
        if 0 < bruto1 <= 80:
            return bruto1
        elif 80 < bruto1 <= 250:
            return bruto1 - 6.8
        elif 250 < bruto1 <= 450:
            return bruto1 - 16
        elif 450 < bruto1 <= 800:
            return bruto1 - 30
        elif 800 < bruto1 <= 1000:
            return bruto1 - 40
        else:
            return bruto1 - (8 / 100) * bruto1


def RPS(choice_name):
    choice_name = choice_name.lower()
    if choice_name == 'rock':
        choice = 1
    elif choice_name == 'paper':
        choice = 2
    elif choice_name == 'scissors':
        choice = 3
    else:
        return "Keni shtypur opsion jo-valid. Shtyp rock , paper apo scissors per te vazhduar"

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    if (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2):
        return "Ju keni fituar. Kompjuteri zgjodhi " + comp_choice_name
    elif (choice == comp_choice):
        return "Barazim. Edhe kompjuteri zgjodhi " + comp_choice_name
    else:
        return "Fitoi kompjuteri . Kompjuteri zgjodhi " + comp_choice_name



def dergokerkesen(request, conn, addr):
    requestarray = request.upper()
    requestarray = requestarray.split(" ")
    kerkesa1 = request.split(" ")
    if (requestarray[0] == 'IPADDRESS'):
        if len(requestarray) == 1:
            conn.send(str.encode('IP Adresa e klientit eshte:' + IPADDRESS()))
        else:
            conn.send(str.encode("Metoda IPADDRESS duhet te permbaje vetem nje argument"))



    elif (requestarray[0] == 'PORT'):
        if len(requestarray) == 1:
            conn.send(str.encode(" Klienti eshte duke perdorur portin " + PORT()))
        else:
            conn.send(str.encode("Metoda PORT duhet te permbaje vetem nje argument"))
    elif (requestarray[0] == 'COUNT'):
        if len(requestarray) == 1:
            conn.send(str.encode("Metoda COUNT duhet te permbaje me shume se nje argument"))
        else:
            s = requestarray[1:]
            conn.send(str.encode(str(COUNT(s))))
    elif (requestarray[0] == 'REVERSE'):
        if len(requestarray) == 1:
            conn.send(str.encode("Metoda REVERSE duhet te permbaje me shume se nje argument"))
        else:
            s = request[len(requestarray[0]):]
            conn.send(str.encode((REVERSE(str(s)))))
    elif (requestarray[0] == 'GCF'):
        if len(requestarray) == 1:
            conn.send(str.encode("Metoda GCF duhet te permbaje 3 argumente"))
        elif len(requestarray) == 3:
            if requestarray[1].isdigit() and requestarray[2].isdigit():
                nr1 = int(requestarray[1])
                nr2 = int(requestarray[2])
                conn.send(str.encode(str(GCF(nr1, nr2))))
            else:
                conn.send(str.encode("Metoda GCF duhet te permbaje ne 2 argumentet e fundit vetem numra"))

        else:
            conn.send(str.encode("Metoda GCF duhet te permbaje 3 argumente"))
    elif (requestarray[0] == 'PALINDROME'):
        if len(requestarray) != 2:

            conn.send(str.encode("Metoda PALINDROME duhet te permbaje dy argumente"))
        else:
            s = requestarray[1]
            k = PALINDROME(s)
            conn.send(str.encode(str(k)))
    elif (requestarray[0] == 'TIME'):
        if len(requestarray) == 1:
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            conn.send(str.encode(time))
        else:
            conn.send(str.encode("Metoda TIME duhet te permbaje vetem nje argument"))
    elif (requestarray[0] == 'GAME'):
        if len(requestarray) == 1:
            conn.send(str.encode(str(GAME())))
        else:
            conn.send(str.encode("Metoda GAME duhet te permbaje vetem nje argument"))
    elif requestarray[0] == 'CONVERT':
        mundesite = "Mundesite per konvertime:\ncmToFeet  \nFeetToCm  \nkmToMiles \nMileToKm";

        try:
            s = kerkesa1[1]
            n = float(kerkesa1[2])
            conn.send(str.encode(str(CONVERT(s, n))))
        except IndexError:
            conn.send(str.encode(
                "Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" + mundesite))
        except ValueError:
            conn.send(str.encode(
                "Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" + mundesite))
    elif (requestarray[0] == 'RPS'):
        if len(requestarray) != 2:
            conn.send(str.encode("Metoda RPS duhet te permbaje vetem dy argumente"))
        else:
            s = kerkesa1[1]
            conn.send(str.encode(str(RPS(s))))
    elif (requestarray[0] == 'PAGANETO'):
        try:
            s = float(kerkesa1[1])
            n = float(kerkesa1[2])
            conn.send(str.encode( str(PAGANETO(s, n))))
        except IndexError:
            conn.send(str.encode(
                "Ju lutem shenoni pagen bruto dhe pasta kontributin pensional \n"))
        except ValueError:
            conn.send(str.encode(
                "Ju lutem shenoni pagen bruto dhe pasta kontributin pensional \n"))





    else:
        conn.send(str.encode("Ju lutem shenoni njerat nga kerkesat!"));


def klient_thread(conn, addr):
    while True:
        try:
            data = conn.recv(1024);
            request = data.decode();
            requestarray = request.split();
            try:
                dergokerkesen(request, conn, addr);
            except IndexError:
                conn.send(str.encode("Kerkesa nuk eshte valide!"))
        except OSError:
            conn.close();



while True:
    connectionSocket, addr = serverSocket.accept()
    print('Klienti u lidh ne serverin %s me port %s' % addr)
    start_new_thread(klient_thread, (connectionSocket, addr,))
