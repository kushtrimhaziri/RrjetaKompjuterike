import time
import socket

v = True

while v:
    servetName = ""
    serverPort = 1
    print(
        "Shtyp 1 per te vazhduar me vlera default, shtyp 2 per tí shkruar vlerat manualisht, shtyp 0 per ta ndalur programin: ")
    var = input("Zgjedhja juaj: ")

    if (int(var) == 1):
        serverName = 'localhost'
        serverPort = 13000
    elif int(var) == 0:
        v = False
        break
    elif int(var) == 2:
        serverName = input("Shenoni emrin e serverit:")
        Port = input("Shenoni portin:")
        serverPort = int(Port)
    else:
        print("Shtyp 0 1 ose 2")
        v = True

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        addr = (serverName, serverPort)
        print(
            "-----------------------------------------------------------------------------------------------------------")
        try:
            while v:
                var = input(
                    "Zgjedhni njeren nga kerkesat: \n IPADDRESS\n PORT\n COUNT\n REVERSE\n TIME\n PALINDROME\n GAME\n GCF\n" + " CONVERT\n PAGANETO\n RPS\n" + " Ose shenoni 0 per ta mbyllyr programin\n ")
                if len(var) > 128:
                    print("Kerkesa nuk mund te jete me e gjate se 128 karaktere!")
                    continue
                elif not var:
                    print("Ju lutem shenoni nje kerkese!")
                    continue
                elif var == "0":
                    s.close()
                    break
                else:
                    request = var.lower()
                    request = request.split(" ")
                try:
                    if request[0] == 'ipaddress':
                        if (len(request) == 1):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda IPADDRESS ka vetem nje parameter")
                            continue
                    elif request[0] == "port":
                        if (len(request) == 1):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda PORT ka vetem nje parameter")
                            continue
                    elif request[0] == "count":
                        if (len(request) == 1):
                            print("Metoda COUNT duhet te kete me shume se nje parameter")
                            continue
                        else:
                            sent = client_socket.sendto(var.encode(), addr)
                    elif request[0] == "reverse":
                        if (len(request) == 1):
                            print("Metoda COUNT duhet te kete me shume se nje parameter")
                            continue
                        else:
                            sent = client_socket.sendto(var.encode(), addr)
                    elif request[0] == "palindrome":
                        if (len(request) == 2):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda PALINDROME duhet te kete saktesisht vetem dy parametra")
                            continue
                    elif request[0] == "game":
                        if (len(request) == 1):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda GAME nuk lejon me shume se nje argument")
                            continue
                    elif request[0] == "gcf":
                        if (len(request) == 3):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda GCF duhet te kete 3 argumente")
                            continue
                    elif request[0] == "convert":

                        if (len(request) == 3):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda Convert duhet te kete 3 argumente")
                            continue
                    elif request[0] == "time":
                        if (len(request) == 1):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda TIME lejon vetem nje argument")
                            continue
                    elif request[0] == "rps":
                        if (len(request) == 2):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda RPS lejon vetem dy argumente")
                            continue
                    elif request[0] == "paganeto":
                        if (len(request) == 3):
                            sent = client_socket.sendto(var.encode(), addr)
                        else:
                            print("Metoda PAGANETO lejon vetem tre argumente")
                            continue
                    else:
                        print("Kerkesa juaj nuk eshte valide")
                        continue
                except Exception as e:
                    print(e)
                    continue

                data, server = client_socket.recvfrom(4096)
                print('{!r}'.format(data))

        finally:
            print('Soketi u mbyll')
            client_socket.close()
    except:
        print("Connection failed")
        continue
