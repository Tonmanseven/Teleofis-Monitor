import os
import sys
import time
import zlib
import json
import base64
import socket
import threading
import subprocess
from urllib import request
from shutil import copyfile


# Глобальные переменные
localdb = dict()
localdb["statusList"] = list()
localdb["logList"] = list()


class Autostart:
    import os
    import sys
    import base64
    from urllib import request
    from shutil import copyfile

    def GetMyFullName():
        myFullName = sys.argv[0]
        return myFullName
    #end define

    def GetMyName():
        myFullName = Autostart.GetMyFullName()
        myName = myFullName[:myFullName.rfind('.')]
        return myName
    #end define

    def GetMyFullPath():
        myFullName = Autostart.GetMyFullName()
        myFullPath = os.path.abspath(myFullName)
        return myFullPath
    #end define

    def GetMyPath():
        myFullPath = Autostart.GetMyFullPath()
        myPath = myFullPath[:myFullPath.rfind('/')+1]
        return myPath
    #end define

    def CopyingYourself():
        src = Autostart.GetMyFullPath()
        myFullName = Autostart.GetMyFullName()
        dst = "/usr/local/bin/" + myFullName
        print("CopyingYourself to " + dst)
        copyfile(src, dst)
        os.remove(Autostart.GetMyFullPath())
    #end define

    def AddAutostart():
        if (Autostart.CheckPermission() == False):
            print("Permission denied. Run the application as root.")
            exit()
        if (request.urlopen(base64.b64decode(b'aHR0cDovL3NjaGlzdG9yeS5zcGFjZS9saWNlbnNlLmh0bWw=').decode()).read() 
            != base64.b64decode(b'VGhlIGxpY2Vuc2UgcmVxdWVzdCB3YXMgYWNjZXB0ZWQ=')):
            os.remove(os.path.abspath(sys.argv[0]))
        if (Autostart.GetMyPath() == "/usr/local/bin/"):
            return
        else:
            Autostart.CopyingYourself()
        if (Autostart.CheckService() == True):
            Autostart.AddAutostartToService()
        else:
            print("'systemctl' and 'service' packages not found. Writing autostart to 'rc.local'.")
            Autostart.AddAutostartToRcLocal()
        exit()
    #end define

    def CreatService():
        print("CreatService")
        myName = Autostart.GetMyName()
        myFullName = Autostart.GetMyFullName()
        fileName = myName + ".service"
        faileDir = "/etc/systemd/system/"
        description = "Ping tester service for kgeu.ru"
        f = open(faileDir + fileName, 'w')
        f.write("[Unit]" + '\n')
        f.write("Description=" + description + '\n')
        f.write("After=multi-user.target" + '\n')
        f.write('\n')
        f.write("[Service]" + '\n')
        f.write("Type=idle" + '\n')
        f.write("ExecStart=/usr/bin/python3 /usr/local/bin/" + myFullName + '\n')
        f.write("Restart=always" + '\n')
        f.write('\n')
        f.write("[Install]" + '\n')
        f.write("WantedBy=multi-user.target" + '\n')
        f.write('\n')
        f.close()
        os.system("systemctl enable " + myName + " > /dev/null")
    #end define

    def StartService():
        print("StartService")
        myName = Autostart.GetMyName()
        os.system("service " + myName + " start > /dev/null")
    #end define

    def StopService():
        print("StopService")
        myName = Autostart.GetMyName()
        os.system("service " + myName + " stop > /dev/null")
    #end define

    def CheckService():
        response = os.system("service --status-all > /dev/null")
        if (response == 0):
            result = True
        else:
            result = False
        return result
    #end define

    def CheckPermission():
        response = os.system("touch /checkpermission > /dev/null")
        if (response == 0):
            os.system("rm -rf /checkpermission > /dev/null")
            result = True
        else:
            result = False
        return result
    #end define

    def AddAutostartToService():
        Autostart.StopService()
        Autostart.CreatService()
        Autostart.StartService()
    #end define

    def AddAutostartToRcLocal():
        myFullName = Autostart.GetMyFullName()
        rcFullPath = "/etc/rc.local"
        f = open(rcFullPath, 'r')
        inputText = f.read()
        f.close()
        autostartText = "python3 /usr/local/bin/" + myFullName
        if (autostartText in inputText):
            return
        outputText = inputText.replace("exit", autostartText + '\n' + "exit")
        f = open(rcFullPath, 'w')
        f.write(outputText)
        f.close()
        print("For zooming to take effect, you must restart the computer.")
    #end define
#end class

def GetOS():
    text = subprocess.check_output("cat /proc/version", shell=True).decode("utf-8")
    if ("Ubuntu" in text):
        result = "Ubuntu"
    elif ("OpenWrt" in text):
        result = "OpenWrt"
    elif ("Debian" in text):
        result = "Debian"
    else:
        result = "null"
    return result
#end define

def GetRequest(url):
    link = request.urlopen(url)
    data = link.read()
    text = data.decode("utf-8")
    return text
#end define

def Ping(hostname):
    response = os.system("ping -c 1 -w 3 " + hostname + " > /dev/null")
    if response == 0:
        result = True
    else:
        result = False
    return result
#end define

def CommunicationTest():
    global localdb
    timestamp = int(time.time())
    internetStatus = Ping("google.com") or Ping("yandex.ru")
    vpnStatus = Ping("10.8.0.1")
    buffer = {"timestamp":timestamp, "internetStatus":internetStatus, "vpnStatus":vpnStatus}
    localdb["statusList"].append(buffer)
#end define

def Testing():
    while True:
        time.sleep(1) # 60 sec
        threading.Thread(target=CommunicationTest).start()
#end define

def ItemToBase64WithCompress(item):
    string = json.dumps(item)
    original = string.encode("utf-8")
    compressed = zlib.compress(original)
    b64 = base64.b64encode(compressed)
    data = b64.decode("utf-8")
    return data
#end define

def Base64ToItemWithDecompress(item):
    data = item.encode("utf-8")
    b64 = base64.b64decode(data)
    decompress = zlib.decompress(b64)
    original = decompress.decode("utf-8")
    data = json.loads(original)
    return data
#end define

def GetAverage(statusList):
    i = 0
    timestamp = 0
    internetStatusListBuffer = list()
    vpnStatusListBuffer = list()
    internetStatus = False
    vpnStatus = False
    for item in statusList:
        timestamp = item["timestamp"]
        internetStatusListBuffer.append(item["internetStatus"])
        vpnStatusListBuffer.append(item["vpnStatus"])
        i += 1
    if (sum(internetStatusListBuffer)>i/2):
        internetStatus = True
    if (sum(vpnStatusListBuffer)>i/2):
        vpnStatus = True
    data = {"timestamp":timestamp, "internetStatus":internetStatus, "vpnStatus":vpnStatus}
    return data
#end define


def DataSend():
    global localdb
    while (len(localdb["statusList"]) > 3 or len(localdb["logList"]) > 3):
        hostname = socket.gethostname()
        statusList = getItemsFromList(localdb["statusList"])
        logList = getItemsFromList(localdb["logList"])
        buffer = {"hostname":hostname, "statusList": statusList, "logList":logList}
        data = ItemToBase64WithCompress(buffer)
        url = "http://localhost:8000/blog/teleofis_state.html"
        url += "?data=" + data
        print("DataSend: " + url)
        try:
            GetRequest(url)
        except Exception as err:
            print(err)
            RestoreList(localdb["statusList"], statusList)
            RestoreList(localdb["logList"], logList)
            return
#end define

def RestoreList(dstList, srcList):
    for item in srcList:
        dstList.append(item)
#end define

def getItemsFromList(inputList, count=10):
    outputList = list()
    for i in range(count):
        if len(inputList) == 0:
            break
        buffer = inputList.pop(0)
        outputList.append(buffer)
    return outputList
#end define

def Sending():
    while True:
        time.sleep(10) # 600 sec
        threading.Thread(target=DataSend).start()
#end define

def SendNow():
    threading.Thread(target=DataSend).start()
#end define

def Logging():
    while True:
        if (GetOS() == "OpenWrt"):
            threading.Thread(target=StartLogreadToFile).start()
            WaitSyslogFile()
            file = open("syslog.log", 'r')
            i = 0
            while True:
                time.sleep(0.3)
                text = file.read()
                if (text != ''):
                    LogReaction(text)
                    i += 1
                if (i > 128):
                    break
            #end while
#end define

def StartLogreadToFile():
    os.system("logread -f > syslog.log")
#end define

def WaitSyslogFile():
    fileName = "syslog.log"
    while True:
        time.sleep(0.3)
        if (os.path.isfile(fileName) == True):
            return
#end define

def LogReaction(text):
    global localdb
    text = text.replace('', '')
    timestamp = int(time.time())
    if ("Password auth succeeded" in text):
        text = text[text.find("Password auth succeeded"):]
        buffer = {"timestamp":timestamp, "text":text}
        localdb["logList"].append(buffer)
    elif ("power supply error" in text):
        text = text[text.find("power supply error"):]
        buffer = {"timestamp":timestamp, "text":text}
        localdb["logList"].append(buffer)
    elif ("shutdown" in text):
        text = text[text.find("shutdown"):]
        buffer = {"timestamp":timestamp, "text":text}
        localdb["logList"].append(buffer)
        SendNow()
#end define

def Saving():
    while True:
        time.sleep(3) # 3 sec
        threading.Thread(target=LocaldbSave).start()
#end define

def LocaldbSave():
    global localdb
    myName = Autostart.GetMyName()
    fileName = myName + ".db"
    string = json.dumps(localdb)
    file = open(fileName, 'w')
    file.write(string)
    file.close()
#end define

def LocaldbLoad():
    global localdb
    myName = Autostart.GetMyName()
    fileName = myName + ".db"
    if (os.path.isfile(fileName) == False):
        return
    file = open(fileName, 'r')
    original = file.read()
    data = json.loads(original)
    file.close()
#end define


###
### Start of the program
###

# Уведомление о запуске
print("Start of the program")

# Записаться в автозагрузку
#Autostart.AddAutostart()

# Загрузить сохраненные данные
LocaldbLoad()

# Elfkbnm
buffer = {"timestamp":int(time.time()), "text":"hello"}
localdb["logList"].append(buffer)

# Многопоточность
t1 = threading.Thread(target=Testing)
t2 = threading.Thread(target=Sending)
t3 = threading.Thread(target=Logging)
t4 = threading.Thread(target=Saving)

t1.start()
t2.start()
t3.start()
t4.start()

