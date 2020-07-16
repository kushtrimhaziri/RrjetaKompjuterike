import random
import socket
from datetime import datetime
import random

serverS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverS.bind(('', 13000))

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
        elif (i>='a' and i<='z') or (i>'A' and i<="Z"):
            b += 1

    return "Teksti ka " + str(z) + " zanore dhe " + str(b) + " bashketingellore"
def REVERSE(str):
        s = str.strip()
        reversedString = ""
        index = len(s)  # calculate length of string and save in index
        while index > 0:
            reversedString += s[index - 1]  # save the value of str[index-1] in reverseString
            index = index - 1  # decrement index
        return reversedString
def PALINDROME(teksti):
    if (teksti[:: - 1] == teksti):
        return "True"
    else:
        return "False"
def GCF(a, b):
    if a % b == 0:
        return str(b)
    return GCF(b, a % b)

def PAGANETO(bruto, kontributi):
    if bruto<0:
        return "Paga nuk mund te jete me e vogel se 0"
    elif kontributi > 15 or kontributi < 5:
        return "Kontributi pensional duhet te jete mes 5% dhe 15%"

    else:
        bruto1 = bruto - ((kontributi / 100) * bruto)
        if bruto1>0 and bruto1<=80:
            return round(bruto1,2)
        elif bruto1>80 and  bruto1<=250:
            return round(bruto1-6.8,2)
        elif bruto1>250 and bruto1<=450:
            return round(bruto1-16,2)
        elif bruto1>450 and bruto1<=800:
            return round(bruto1-30,2)
        elif bruto1>800 and bruto1<=1000:
            return round(bruto1-40,2)
        else:
            return round(bruto1-(8/100)*bruto1,2)
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
                comp_choice_name = 'scissors'

            if (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (
                    choice == 3 and comp_choice == 2):
                return "Ju keni fituar. Kompjuteri zgjodhi " + comp_choice_name
            elif (choice == comp_choice):
                return "Barazim. Edhe kompjuteri zgjodhi " + comp_choice_name
            else:
                return "Fitoi kompjuteri . Kompjuteri zgjodhi " + comp_choice_name
def GAME():
    arr = (random.sample(range(1, 35), 5))
    arr.sort()
    return str(arr)





def CONVERT(s, gjatesia):
    if (s == "CMTOFEET"):
        return round(gjatesia * 0.0328084,3)
    elif (s == "FEETTOCM"):

        return round(gjatesia * 30.48,3);
    elif (s == "KMTOMILES"):

        return round(gjatesia * 0.621371,3)
    elif (s == "MILETOKM"):
        return round(gjatesia * 1.60934,3)
    else:
        return "Lloji i konvertimit gabim. Shtyp cmtofeet, feettocm ,kmtomiles ose milestokm"




def dergokerkesen(request,conn, addr):
    requestarray = request.upper()
    requestarray = requestarray.split(" ")
    kerkesa1 = request.split(" ")
    if (requestarray[0]=='IPADDRESS'):
        if len(requestarray) == 1:
            k=IPADDRESS()
            serverS.sendto(str.encode("IP adresa e klientit eshte : " + k),addr)
        else:
            serverS.sendto(str.encode("Metoda IPADDRESS duhet te permbaje vetem nje argument"), addr)
    elif(requestarray[0]=='PORT'):
        if len(requestarray) == 1:
            k=PORT()
            serverS.sendto(str.encode("PORTI i klientit eshte : " + k), addr)
        else:
            serverS.sendto(str.encode("Metoda PORT duhet te permbaje vetem nje argument"), addr)
    elif(requestarray[0]=='GAME'):
        if len(requestarray) == 1:
            k=GAME()
            serverS.sendto(str.encode(k), addr)
        else:
            serverS.sendto(str.encode("Metoda GAME duhet te permbaje vetem nje argument"),addr)
    elif (requestarray[0] == 'TIME'):
        if len(requestarray) == 1:
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
            serverS.sendto(str.encode(time), addr);
        else:
            serverS.sendto(str.encode("Metoda TIME duhet te permbaje vetem nje argument"), addr)
    elif(requestarray[0]=='COUNT'):
        if len(requestarray) == 1:
            serverS.sendto(str.encode("Metoda COUNT duhet te permbaje me shume se nje argument"), addr)

        else:
            s = requestarray[1:]
            k=COUNT(s)
            serverS.sendto(str.encode(k), addr)
    elif(requestarray[0]=='REVERSE'):
        if len(requestarray) == 1:
            serverS.sendto(str.encode("Metoda COUNT duhet te permbaje me shume se nje argument"), addr)
        else:
            s = request[len(requestarray[0]):]
            k=REVERSE(s)
            serverS.sendto(str.encode(k), addr)
    elif(requestarray[0]=='PALINDROME'):
        if len(requestarray) != 2:
            serverS.sendto(str.encode("Metoda PALINDROME duhet te permbaje dy argumente"), addr)

        else:
            s = requestarray[1]
            k=PALINDROME(s)
            serverS.sendto(str.encode(k), addr)
    elif(requestarray[0]=='GCF'):
        if len(requestarray)!=3:
            serverS.sendto(str.encode("Metoda GCF duhet te permbaje 3 argumente"), addr)

        elif len(requestarray) == 3:
            if requestarray[1].isdigit() and requestarray[2].isdigit():
                nr1 = int(requestarray[1])
                nr2 = int(requestarray[2])
                k=GCF(nr1,nr2)

                serverS.sendto(str.encode(k), addr)
            else:
                serverS.sendto(str.encode("Metoda GCF duhet te permbaje 3 argumente"),
                                     addr)
    elif (requestarray[0] == 'RPS'):
        if len(requestarray) != 2:
            serverS.sendto(str.encode("Metoda RPS duhet te permbaje 2 argumente"), addr)

        else:
            s = kerkesa1[1]
            k = RPS(s)
            serverS.sendto(str.encode(k), addr)
    elif (requestarray[0] == 'CONVERT'):
        helpString1 = "Mundesite per konvertime:\ncmToFeet  \nFeetToCm  \nkmToMiles \nMileToKm";

        try:
            s = requestarray[1]
            n = float(requestarray[2])
            serverS.sendto(str.encode(str(CONVERT(s, n))), addr)
        except IndexError:
            serverS.sendto(str.encode(
                "Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" + helpString1 ), addr)
        except ValueError:
            serverS.sendto(str.encode(
                "Ju lutem shenoni cka deshironi te konvertoni pastaj shifren!\n " + helpString1 ), addr)
    elif requestarray[0]== 'PAGANETO':
        try:
            s = float(kerkesa1[1])
            n = float(kerkesa1[2])
            serverS.sendto(str.encode("Paga neto eshte " + str(PAGANETO(s, n))), addr)

        except IndexError:
            serverS.sendto(str.encode("Ju lutem shenoni pagen bruto dhe pasta kontributin pensional \n"),
                                 addr)

        except ValueError:
            serverS.sendto(str.encode("Ju lutem shenoni pagen bruto dhe pasta kontributin pensional \n"),
                                 addr)



    else:
        serverS.sendto(str.encode(
            "Ju lutem shenoni njerat nga kerkesat!!\n "), addr)



while True:
    request, addr = serverS.recvfrom(1024)
    request = request.decode('utf-8')
    requestarray = request.split()
    dergokerkesen(request, serverS, addr)
