import os
from PioClassV0_9_5 import Pio
def title():
    print("      ___                       ___     ")
    print("     /\  \          ___        /\  \    ")
    print("    /::\  \        /\  \      /::\  \   ")
    print("   /:/\:\  \       \:\  \    /:/\:\  \  ")
    print("  /::\~\:\  \      /::\__\  /:/  \:\  \ ")
    print(" /:/\:\ \:\__\  __/:/\/__/ /:/__/ \:\__\\")
    print(" \/__\:\/:/  / /\/:/  /    \:\  \ /:/  /")
    print("      \::/  /  \::/__/      \:\  /:/  / ")
    print("       \/__/    \:\__\       \:\/:/  /  ")
    print("                 \/__/        \::/  /   ")
    print("                               \/__/    ")
    print("\nCreated By: stx3rror©")
    print("GitHub: https://github.com/stx3rror")
    print("Contact: stx3rror@gmail.com\n")
        
def options():
        
    print("1. Escaneo de puertos ")
    print("2. Escaneo de puerto especifico ")
    print("3. Escaneo de rangos de IPs")
    print("4. Escaneo de rutas HTTP")
    print("5. Obtener IP de un host") 
    print("6. Ver mi Ip")
    print("7. Salir")
       
    option = input("\n[*] Introduce la opcion que prefieras... ")
    selectOption(option)
def selectOption(option):
    try:
        option = int(option)
    except:
        raise TypeError("The option mustn't be a integer")
            
    if(option < 1 or option > 7):
        raise TypeError("The option selected not exists")

    pio = Pio()
    #<---------- | Escaneo de puertos | ---------->
        
    if(option == 1):
        host = input("Introduce el host... ")#str
        numPuerts = input("[*] Introduce el numero de puertos... ")#int
        interval = input("Introduce el tiempo entre paquetes (en milisegundos)... ")#int
        try:
            numPuerts = int(numPuerts)
            interval = float(interval)
        except:
            raise TypeError("The number of ports and the interval must be a integer")

        pio.setIp(host)
        pio.setNumberPorts(numPuerts)
        pio.setIntervaleRequests(interval)

        arrayPorts = pio.scanPorts()
        if(len(arrayPorts) > 0):
            for port in arrayPorts:
                print('\t[+] Open port found: ',port)
        else:
            print("[-] No open ports found!")

    #<---------- | Escaneo de un puerto | ---------->
    elif(option == 2):
        host = input("[*] Introduce el host... ")#str
        port = input("[*] Introduce el puerto... ")#int
        try:
            port = int(port)
        except:
            raise TypeError("The port must be a integer")
            
        pio.setIp(host)
        pio.setPort(port)
        isOpen = pio.scanOnePort()
        if(len(isOpen)>0):
            print("[+] The port {} is open!".format(port))
        else:
            print("[-] The port {} is close".format(port))


    #<---------- | Escaneo de equipos de red | ---------->
    elif(option == 3):
        rangeOfIps = input("Example. 192.168.1.32-87\nRange of IPs to scan... ")
        pio.setRangeIps(rangeOfIps)
        debugOutput = pio.activateDebug(1)
        arrayOfIps = pio.scanRangesNetwork()
        if(debugOutput != True!=True):
            
            if(len(arrayOfIps)>0):
                for ip in arrayOfIps:
                    print("\t[+] The host {} is online!".format(ip))
            else:
                print("[-] All hosts on this network are offline")


    #<---------- | Escaneo de rutas HTTP | ---------->
    elif(option == 4):
        urlAddress = input("Example. http://url.com\n[*] Introduce la url para escanear... ")
        file = input("[*] Introduce la ruta del archivo del diccionario... ")
        print("Example. num>0 -> cantidad de rutas. num=0 -> todas las rutas")
        intervaleRutes = input("[*] Introduce la cantidad de rutas a probar ... ")
           
        try:
            file = str(file)
            intervaleRutes=int(intervaleRutes)
            urlAddress = str(urlAddress)
        except:
            raise TypeError("The values of the params are wrong")
            
        pio.setFile(file)
        pio.setIntervaleRutes(intervaleRutes)
        pio.setUrlAddress(urlAddress)

        arrayUrls = pio.scanRutesHttp()
        if(len(arrayUrls)>0):
            for url in arrayUrls:
                print("[+] {} found!".format(url))
        else:
            print("[-] No rutes found")

    #<---------- | Conseguir ip de un hostname | ---------->       
    elif(option == 5):
        host = input("Example. www.url.com\n[*] Introduce el host... ")#str
        pio.setHostname(host)
        ipLocal = pio.getIpFromHostname()
        if(ipLocal != ""):
            print("[+] The Ip Address of [{}] is {}".format(host,ipLocal))
        else:
            print("[-] The host {} is offline or the firewall is blocking it")


    #<---------- | Conseguir mi ip | ---------->        
    elif(option == 6):
        myIp = pio.getMyOwnIp()
        if(myIp!=""):
            print("My Ip address is {}".format(myIp))
        else:
            print("My Ip address not found")


    #<---------- | Salir | ---------->
    elif(option == 7):
        os.system("exit")

    input("Pulse una tecla para continuar...")
        
if __name__ != '__init__':
    while(True):
        title()
        options()
        os.system("cls")
