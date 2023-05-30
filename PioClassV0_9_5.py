import socket
import os
import time
import requests
import re

class Pio:  

    #TODO Cambiar la asignacion de __ip por getIp() dentro de los metodos
#====================VARIABLES====================    

    __openPorts=[]
    __urlsOnline=[]
    __ranges=[]
    __const={}
    
    __numberPorts = None
    __ip = None
    __hostname = None
    __intervaleRequests = None
    __rute = None
    __port = None
    __rangeIps = None
    __finalRange = None
    __firstRange = None
    __netAddress = None
    __file = None
    __intervaleRutes = None
    __urlAddress = None
    __sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    __myIp = None  
    debugLevel = 0
    
#<--------------------- | CONSTRUCTOR | --------------------->
    
    def __init__(self):
        
        self.__openPorts=[]
        self.__urlsOnline=[]
        self.__const={}

#<--------------------- | SETTERS | --------------------->
        
    def setNumberPorts(self,numberPorts):
        
        if(type(numberPorts) == int):
            #Validation is correct!
            self.__numberPorts = numberPorts
        else:
          raise TypeError("The number of ports must be a integer")


    def setIp(self,ip):

        if(type(ip) == str):
            #Validation is correct!
            self.__ip = ip
        else:
          raise TypeError("The ip must be a string")

    def setHostname(self,hostname):
    
        if(type(hostname) == str):
            #Validation is correct!
            self.__hostname = hostname
        else:
          raise TypeError("The hostname must be a string")


    def setPort(self,port):
        
        if(type(port) == int):
            #Validation is correct!
            self.__port = port
        else:
          raise TypeError("The port must be a integer")

    def setIntervaleRequests(self,intervaleRequests):

        #Si es un numero
        if(type(intervaleRequests) == int or type(intervaleRequests) == float):

            self.__intervaleRequests = intervaleRequests
            
        else:
          raise TypeError("The intervale of requests must be a integer")
        
    def setRute(self,rute):
    
        if(type(rute) == str):
            #Validation is correct!
            self.__rute = rute
        else:
          raise TypeError("The rute must be a string")

    def setRangeIps(self,rangeIps):
    
        if(type(rangeIps) == str):
            #Validation is correct but i need validate format!
            #
            #Corrects formats:
            #
            #XXX.XXX.XXX.XXX-XXX (example 192.168.0.1-255)
            #XXX.XXX.XXX.XXX-XXX.XXX.XXX.XXX (example 192.168.0.1-192.168.0.255)
            #
            #Second in Progress!!!
            self.__rangeIps = rangeIps
        else:
          raise TypeError("The range of IPs must be a string")

    def setFile(self,file):
        self.__file = file

    def setIntervaleRutes(self,intervaleRutes):

        #Si es un numero
        if(type(intervaleRutes) == int):

            self.__intervaleRutes = intervaleRutes
            
        else:
          raise TypeError("The intervale of requests must be a integer")
        
    def setUrlAddress(self,url):
        if(type(url) == str):
            self.__urlAddress = url
        else:
            raise TypeError("The intervale of requests must be a string")

    def setOpenPorts(self,port):
        self.__openPorts.append(port)

    def setIpsAddressOnline(self,address):
        self.__ranges.append(address)

    def setUrlsOnline(self,url):
        self.__urlsOnline.append(url)
#<--------------------- | GETTERS | --------------------->


    def getNumberPorts(self):

        if(self.__numberPorts==None):
            raise ValueError("The number of ports is empty, please assign a value")
        else:
            return self.__numberPorts

    def getIp(self):

        if(self.__ip==None):
            raise ValueError("The ip is empty, please assign a value")
        else:
            return self.__ip

    def getHostname(self):
    
        if(self.__hostname==None):
            
            raise ValueError("The hostname is empty, please assign a value")
        else:
          return self.__hostname

    def getPort(self):

        if(self.__port==None):
            raise ValueError("The port is empty, please assign a value")
        else:
            return self.__port

    def getIntervaleRequests(self):

        if(self.__intervaleRequests==None):
            raise ValueError("The interval of requests is empty, please assign a value")
        else:
            return self.__intervaleRequests

    def getRute(self):

        if(self.__rute==None):
            raise ValueError("The rute is empty, please assign a value")
        else:
            return self.__rute

    def getRangeIps(self):

        if(self.__rangeIps==None):
            raise ValueError("The range of IPs is empty, please assign a value")
        else:
            return self.__rangeIps
        
    def getFile(self):
        return self.__file

    def getIntervaleRutes(self):
        return self.__intervaleRutes
        
    def getIpFromHostname(self):
    
        return socket.gethostbyname(self.getHostname())

    def getMyOwnIp(self):
        #IPv4 Address. . . . . . . . . . . :
        resultCmd = os.popen("ipconfig") #Esta funcion te ejecuta un comando com si fuese os.system() pero te devuelve el resultado de la ejecucion de comandos
        for line in resultCmd.readlines():
            #Leemos un array de lineas con cada linea del resultado
            if("IPv4 Address" in line): #Si se encuentra la cadena "TTL" en cualquier linea entonces sera porque ha habido respuerta de la ip
                self.__myIp=line.split(":")[1].split("\n")[0].replace(" ","")
                break
        return self.__myIp
    
    def getUrlAddress(self):
        return self.__urlAddress

    def getOpenPorts(self):
        return self.__openPorts

    def getIpsAddressOnline(self):
        return self.__ranges

    def getUrlsOnline(self):
        return self.__urlsOnline
#<--------------------- | SCANNERS | --------------------->

    def scanPorts(self):
        
        #This local variable is only for best view of code, i can use drectly a getter
        localNumberPorts = self.getNumberPorts()
        localIntervalRequests = self.getIntervaleRequests()
        localIp = self.getIp()
        for port in range (1,localNumberPorts+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(localIntervalRequests)
            result = sock.connect_ex((localIp,port))
            if result == 0:
                self.setOpenPorts(port)

            sock.close()
        return self.getOpenPorts()

    def scanOnePort(self):
        
        #This local variable is only for best view of code, i can use drectly a getter
        localPort = self.getPort()
        localIp = self.getIp()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3.5)
        result = sock.connect_ex((localIp,localPort))
        
        if result == 0:
            self.setOpenPorts(localPort)
            
        sock.close()
        return self.getOpenPorts()

    def scanRangesNetwork(self):
        
        arrayFirstAndLast = self.getRangeIps().split("-") #Separo la cadena en dos partes ['192.168.0.1','255']
        finalRange = arrayFirstAndLast[1] #Consigo la ultima parte '255'
        stringFirstRange = arrayFirstAndLast[0] #Consigo la primera cadena '192.168.0.1'
        arrayFirstRange = stringFirstRange.split(".") #Separo la cadena en cuatro partes ['192','168','0','1']
        firstRange = arrayFirstRange[-1] #Consigo la ultima parte '1'
        netAddress = arrayFirstRange[0]+"."+arrayFirstRange[1]+"."+arrayFirstRange[2]+"." #Consigo la direccion de red
        """
        for byte in range(int(firstRange),int(finalRange)+1):
            
            ipToPing = str(netAddress) + str(byte)
            #Hariamos ping a cada ip
            resultPing = os.popen("ping -n 1 " + ipToPing) #Esta funcion te ejecuta un comando com si fuese os.system() pero te devuelve el resultado de la ejecucion de comandos
            print(resultPing.read()) if (self.debugLevel == 2) else None
            for line in resultPing.readlines():
                #Leemos un array de lineas con cada linea del resultado
                if("TTL" in line): #Si se encuentra la cadena "TTL" en cualquier linea entonces sera porque ha habido respuerta de la ip
                    self.setIpsAddressOnline(ipToPing)
                    print("[DEBUG] {} is online!".format(ipToPing)) if (self.debugLevel == 1 or 2) else None
                    break
        return self.getIpsAddressOnline()
        """

        for byte in range(int(firstRange),int(finalRange)+1):
            
            ipToPing = str(netAddress) + str(byte)
            #Hariamos ping a cada ip
            resultPing = os.popen("ping -n 1 " + ipToPing).read() #Esta funcion te ejecuta un comando com si fuese os.system() pero te devuelve el resultado de la ejecucion de comandos
            print(resultPing) if (self.debugLevel == 2) else None
            if(re.search(r'\bTTL\b',resultPing) is None):
                continue
            else:
                self.setIpsAddressOnline(ipToPing)
                print("[DEBUG] {} is online!".format(ipToPing)) if (self.debugLevel == 1 or 2) else None
                
        return self.getIpsAddressOnline()
    
    def scanRutesHttp(self):
        cont=0
        file=open(self.getFile(),"r")
    
        if(self.getIntervaleRutes!=0):
            contMax=int(self.getIntervaleRutes())
        else:
            contMax=len(file.readlines())

        for linea in file:
            if(cont==contMax):
                break
            else:
                url=self.getUrlAddress()+"/"+linea
                url=url.strip()            
                code=requests.get(url).status_code
                if(code==200):
                    self.setUrlsOnline(url)
                else:
                    pass
                cont+=1
        file.close()
        return self.getUrlsOnline()

#<--------------------- | METHODS | --------------------->

    def activateDebug(self,level):
        #0 -> desactivate, 1 -> Low (Scanners in live time...), 2 -> High (all)
        try:
            level=int(level)
        except:
            raise TypeError("The hostname must be a integer")

        if(level<0 or level==0):
            level = 0
        elif(level>2 or level==2):
            level = 2
        self.debugLevel = level
        return True