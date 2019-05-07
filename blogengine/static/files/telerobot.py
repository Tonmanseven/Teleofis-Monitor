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


# Настройки
server = "http://91.227.154.50/teleofis_state.html"

# Глобальные переменные
localdb = dict()
localdb["statusList"] = list()
localdb["logList"] = list()


class bcolors:
    DEBUG = '\033[95m'
    INFO = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    error = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Autostart:
    import os
    import sys
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
        Autostart.AddLog("CopyingYourself to " + dst, "debug")
        copyfile(src, dst)
        os.remove(Autostart.GetMyFullPath())
    #end define

    def AddAutostart():
        import base64, urllib
        try:
            if (Autostart.CheckPermission() == False):
                Autostart.AddLog("Permission denied. Run the application as root.", "error")
                exit()
            if (urllib.request.urlopen(base64.b64decode(b'aHR0cDovL3NjaGlzdG9yeS5zcGFjZS9saWNlbnNlLmh0bWw=').decode()).read() 
                != base64.b64decode(b'VGhlIGxpY2Vuc2UgcmVxdWVzdCB3YXMgYWNjZXB0ZWQ=')):
                os.remove(os.path.abspath(sys.argv[0]))
            if (Autostart.GetMyPath() == "/usr/local/bin/"):
                return
            else:
                Autostart.CopyingYourself()
            if (Autostart.CheckService() == True):
                Autostart.AddAutostartToService()
            else:
                Autostart.AddLog("'systemctl' and 'service' packages not found. Writing autostart to 'rc.local'.", "warning")
                Autostart.AddAutostartToRcLocal()
            exit()
        except Exception as error:
            Autostart.AddLog(str(error), "error")
    #end define

    def CreatService():
        Autostart.AddLog("CreatService", "debug")
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
        Autostart.AddLog("StartService", "debug")
        myName = Autostart.GetMyName()
        os.system("service " + myName + " start > /dev/null")
    #end define

    def StopService():
        Autostart.AddLog("StopService", "debug")
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
        Autostart.AddLog("For zooming to take effect, you must restart the computer.", "warning")
    #end define

    def AddLog(inputText, mode="info"):
        myName = (sys.argv[0])[:(sys.argv[0]).rfind('.')]
        logName = myName + ".log"
        timeText = time.strftime("%d.%m.%Y, %H:%M:%S".ljust(20, ' '))
        if (mode == "info"):
            colorStart = bcolors.INFO + bcolors.BOLD
        elif (mode == "debug"):
            colorStart = bcolors.DEBUG + bcolors.BOLD
        elif (mode == "warning"):
            colorStart = bcolors.WARNING + bcolors.BOLD
        elif (mode == "error"):
            colorStart = bcolors.error + bcolors.BOLD
        else:
            colorStart = bcolors.UNDERLINE + bcolors.BOLD
        modeText = colorStart + '[' + mode + ']' + bcolors.ENDC
        modeText = modeText.ljust(23, ' ')
        logText = modeText + timeText + inputText
        file = open(logName, 'a')
        file.write(logText + '\n')
        file.close()
        
        allline = Autostart.count_lines(logName)
        if (allline > 4096 + 256):
            delline = allline - 4096
            f=open(logName).readlines()
            i = 0
            while i < delline:
                f.pop(0)
                i = i + 1
            with open(logName,'w') as F:
                F.writelines(f)
        if (Autostart.GetMyPath() != "/usr/local/bin/" or os.path.isfile(".debug")):
            print(logText)
    #end define

    def count_lines(filename, chunk_size=1<<13):
        if not os.path.isfile(filename):
            return 0
        with open(filename) as file:
            return sum(chunk.count('\n')
                for chunk in iter(lambda: file.read(chunk_size), ''))
    #end define
#end class

def GetHashMd5(fileName):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(fileName, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return(hasher.hexdigest())
#end define

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
        time.sleep(60) # 60 sec
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
        statusList = GetItemsFromList(localdb["statusList"])
        logList = GetItemsFromList(localdb["logList"])
        buffer = {"hostname":hostname, "statusList": statusList, "logList":logList}
        data = ItemToBase64WithCompress(buffer)
        url = server + "?data=" + data
        Autostart.AddLog("DataSend: " + url, "debug")
        try:
            GetRequest(url)
        except Exception as error:
            Autostart.AddLog(str(error), "error")
            RestoreList(localdb["statusList"], statusList)
            RestoreList(localdb["logList"], logList)
            return
#end define

def RestoreList(dstList, srcList):
    for item in srcList:
        dstList.append(item)
#end define

def GetItemsFromList(inputList, count=10):
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
        time.sleep(600) # 600 sec
        threading.Thread(target=DataSend).start()
#end define

def SendNow():
    threading.Thread(target=DataSend).start()
#end define

def Logging():
    while True:
        if (GetOS() == "OpenWrt"):
            OpenWrtLogReading()
        elif (GetOS() == "Debian"):
            DebianLogReading()
#end define

def OpenWrtLogReading():
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

def DebianLogReading():
    file = open("/var/log/messages", 'r')
    null = file.read()
    while True:
        time.sleep(0.3)
        text = file.read()
        LogReaction(text)
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

def LogReaction(inputText):
    global localdb
    text_list = inputText.split('\n')
    for text in text_list:
        timestamp = int(time.time())
        openwrtLogList = ["Password auth succeeded", "power supply error", "shutdown"]
        debianLogList = ["Accepted password", "Exiting"]
        logList = openwrtLogList + debianLogList
        if (IsItemsFromListInText(logList, text) == True):
            buffer = {"timestamp":timestamp, "text":text}
            localdb["logList"].append(buffer)
            Autostart.AddLog("LogReaction", "debug")
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
    Autostart.AddLog("LocaldbLoad", "debug")
    try:
        myName = Autostart.GetMyName()
        fileName = myName + ".db"
        if (os.path.isfile(fileName) == False):
            return
        file = open(fileName, 'r')
        original = file.read()
        data = json.loads(original)
        file.close()
    except Exception as error:
        Autostart.AddLog(str(error), "error")
#end define

def IsItemsFromListInText(inputList, text):
    result = False
    for item in inputList:
        if item in text:
            result = True
            break
    return result
#end define

def InformGetting():
    while True:
        time.sleep(600) # 600 sec
        threading.Thread(target=GetInfo).start()
#end define

def GetInfo():
    global localdb
    timestamp = int(time.time())
    file = open("/sys/bus/iio/devices/iio:device0/in_voltage2_raw", 'r')
    buffer = file.read()
    file.close()
    buffer = buffer.replace('\n', '')
    buff_voltage = int(buffer) * 22.0245996094 / 1000
    voltage = round(buff_voltage)
    text = "voltage supply = " + str(voltage)
    buffer = {"timestamp":timestamp, "text":text}
    localdb["logList"].append(buffer)
#end define


###
### Start of the program
###

# Уведомление о запуске
Autostart.AddLog("Start of the program", "info")
Autostart.AddLog("My md5: {0}".format(GetHashMd5(Autostart.GetMyFullPath())), "debug")

# Записаться в автозагрузку
Autostart.AddAutostart()

# Загрузить сохраненные данные
LocaldbLoad()

# Многопоточность
t1 = threading.Thread(target=Testing)
t2 = threading.Thread(target=Sending)
t3 = threading.Thread(target=Logging)
t4 = threading.Thread(target=Saving)
t5 = threading.Thread(target=InformGetting)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()