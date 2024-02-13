import os
from PioClass import *

class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
    print("\nCreated By: XSFrenetic©")
    print("Contact: wwbhty@gmail.com\n")
        
def options():
        
    print("1. Escaneo de puertos ")
    print("2. Escaneo de puerto especifico ")
    print("3. Escaneo de rangos de IPs")
    print("4. Escaneo de rutas HTTP")
    print("5. Obtener IP de un host") 
    print("6. Ver mi Ip")
    print("7. Configuracion")
    print("8. Salir")
    
    option = input("\n[*] Introduce la opcion que prefieras... ")
    
    selectOption(option)
def selectOption(option):
    try:
        option = int(option)
    except:
        raise TypeError("The option mustn't be a integer")
            
    if(option < 1 or option > 7):
        raise TypeError("The option selected not exists")

    #<---------- | Escaneo de puertos | ---------->
        
    if(option == 1):
        host = input("Introduce el host... ")#str
        numPuerts = input("[*] Introduce el numero de puertos... ")#int
        interval = input("Introduce el tiempo entre paquetes (en segundos)... ")#int
        try:
            numPuerts = int(numPuerts)
            interval = float(interval)
        except:
            raise TypeError("The number of ports and the interval must be a integer")

        pio.setIp(host)
        pio.setNumberPorts(numPuerts)
        pio.setIntervaleRequests(interval)

        arrayPorts = pio.scanPorts(title)

        if(len(arrayPorts) > 0):
            for port in arrayPorts:
                print(COLORS.OKGREEN + '\t[+] Open port found: {}'.format(port) + COLORS.ENDC)
        else:
            print(COLORS.FAIL + "[-] No open ports found!" + COLORS.ENDC)




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
            print(COLORS.OKGREEN + "[+] The port {} is open!".format(port) + COLORS.ENDC)
        else:
            print(COLORS.FAIL + "[-] The port {} is close".format(port) + COLORS.ENDC)


    #<---------- | Escaneo de equipos de red | ---------->
    elif(option == 3):
        rangeOfIps = input("Example. 192.168.1.32-87\nRange of IPs to scan... ")
        pio.setRangeIps(rangeOfIps)
        arrayOfIps = pio.scanRangesNetwork()
        if(not(pio.getVerbose())):
            if(len(arrayOfIps)>0):
                for ip in arrayOfIps:
                    print(COLORS.OKGREEN + "\t[+] El host {} esta conectado!".format(ip) + COLORS.ENDC)
            else:
                print(COLORS.FAIL + "[-] Todos los hots de esta red están desconectados" + COLORS.ENDC)


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
                print(COLORS.OKGREEN + "[+] {} encontrada!".format(url) + COLORS.ENDC)
        else:
            print(COLORS.FAIL + "[-] Ninguna ruta encontrada" + COLORS.ENDC)

    #<---------- | Conseguir ip de un hostname | ---------->       
    elif(option == 5):
        host = input("Example. www.url.com\n[*] Introduce el host... ")#str
        pio.setHostname(host)
        ipLocal = pio.getIpFromHostname()
        if(ipLocal != ""):
            print(COLORS.OKGREEN + "[+] La direccion ip de [{}] es {}".format(host,ipLocal) + COLORS.ENDC)
        else:
            print(COLORS.FAIL + "[-] El host {} está desconectado o el firewall lo está bloqueando" + COLORS.ENDC)


    #<---------- | Conseguir mi ip | ---------->        
    elif(option == 6):
        myIp = pio.getMyOwnIp()
        if(myIp!=""):
            print("Mi direcction ip es {}".format(myIp))
        else:
            print("Direccion ip no encontrada")

    #<---------- | Configuracion | ---------->
    elif(option == 7):
        
        os.system("cls")
        title()
        print("1. Alternar verbose (Estado actual: {})".format("Activado"if(pio.getVerbose())else"Desactivado"))
        if(input("Selecciona opcion de configuración: ") == '1'):
            pio.toggleVerbose()
        else:
            pass

    #<---------- | Salir | ---------->
    elif(option == 8):
        #Utils.loading()
        os.system("exit")

    input("Pulse una tecla para continuar...")
        
if __name__ != '__init__':
    pio = Pio()
    while(True):
        try:
            title()
            options()
            os.system("cls")
        except(KeyboardInterrupt):
            os.system("cls")
            pass
