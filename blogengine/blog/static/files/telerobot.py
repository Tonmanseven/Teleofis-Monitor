<<<<<<< HEAD
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
import hashlib


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
				sys.exit()
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
			sys.exit()
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
	internetStatus = Ping("google.com") or Ping("yandex.ru") or Ping("8.8.8.8")
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

def SelfUpdating():
	while True:
		time.sleep(10) # 600 sec
		threading.Thread(target=SelfUpdate).start()
#end define

def SelfUpdate():
	md5Url = "http://invent-monitor.scorpclub.ru/teleofis_files.html"
	appUrl = "http://invent-monitor.scorpclub.ru/static/files/telerobot.py"
	
	myFullPath = Autostart.GetMyFullPath()
	text = GetRequest(md5Url)
	md5FromServer = Pars(text, "md5")
	myMd5 = GetHashMd5(myFullPath)
	if (myMd5 == md5FromServer):
		return
	Autostart.AddLog("SelfUpdate", "debug")
	data = request.urlopen(appUrl).read()
	file = open(myFullPath, 'wb')
	file.write(data)
	file.close()
	os.system("reboot -f")
#end define

def Pars(text, pars):
	return text[text.find("<{0}>".format(pars)) + len("<{0}>".format(pars)):text.find("</{0}>".format(pars))]
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
t6 = threading.Thread(target=SelfUpdating)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
=======
2019.03.29 0.09
2019.03.29 0.39
2019.03.29 1.1
2019.03.29 1.4
2019.03.29 2.1
2019.03.29 2.4
2019.03.29 3.11
2019.03.29 3.41
2019.03.29 4.11
2019.03.29 4.41
2019.03.29 5.12
2019.03.29 5.42
2019.03.29 6.12
2019.03.29 6.42
2019.03.29 7.12
2019.03.29 7.43
2019.03.29 8.13
2019.03.29 8.43
2019.03.29 9.13
2019.03.29 9.43
2019.03.29 10.13
2019.03.29 10.43
2019.03.29 11.14
2019.03.29 11.44
2019.03.29 12.14
2019.03.29 12.44
2019.03.29 13.14
2019.03.29 13.44
2019.03.29 14.15
2019.03.29 14.45
2019.03.29 15.15
2019.03.29 15.45
2019.03.29 16.15
2019.03.29 16.46
2019.03.29 17.16
2019.03.29 17.46
2019.03.29 18.16
2019.03.29 18.46
2019.03.29 19.16
2019.03.29 19.47
2019.03.29 20.17
2019.03.29 20.47
2019.03.29 21.17
2019.03.29 21.48
2019.03.29 22.18
2019.03.29 22.48
2019.03.29 23.18
2019.03.29 23.48
2019.03.30 0.19
2019.03.30 0.49
2019.03.30 1.19
2019.03.30 1.49
2019.03.30 2.2
2019.03.30 2.5
2019.03.30 3.2
2019.03.30 3.5
2019.03.30 4.2
2019.03.30 4.51
2019.03.30 5.21
2019.03.30 5.51
2019.03.30 6.21
2019.03.30 6.52
2019.03.30 7.22
2019.03.30 7.52
2019.03.30 8.22
2019.03.30 8.52
2019.03.30 9.22
2019.03.30 9.53
2019.03.30 10.23
2019.03.30 10.53
2019.03.30 11.23
2019.03.30 11.53
2019.03.30 12.24
2019.03.30 12.54
2019.03.30 13.24
2019.03.30 13.54
2019.03.30 14.24
2019.03.30 14.54
2019.03.30 15.25
2019.03.30 15.55
2019.03.30 16.25
2019.03.30 16.55
2019.03.30 17.25
2019.03.30 17.55
2019.03.30 18.26
2019.03.30 18.56
2019.03.30 19.26
2019.03.30 19.56
2019.03.30 20.27
2019.03.30 20.57
2019.03.30 21.27
2019.03.30 21.57
2019.03.30 22.28
2019.03.30 22.58
2019.03.30 23.28
2019.03.30 23.58
2019.03.31 0.29
2019.03.31 0.59
2019.03.31 1.29
2019.03.31 1.59
2019.03.31 2.3
2019.03.31 3
2019.03.31 3.3
2019.03.31 4
2019.03.31 4.31
2019.03.31 5.01
2019.03.31 5.31
2019.03.31 6.01
2019.03.31 6.32
2019.03.31 7.02
2019.03.31 7.32
2019.03.31 8.03
2019.03.31 8.33
2019.03.31 9.03
2019.03.31 9.33
2019.03.31 10.03
2019.03.31 10.34
2019.03.31 11.04
2019.03.31 11.34
2019.03.31 12.04
2019.03.31 12.34
2019.03.31 13.05
2019.03.31 13.35
2019.03.31 14.05
2019.03.31 14.35
2019.03.31 15.05
2019.03.31 15.36
2019.03.31 16.06
2019.03.31 16.36
2019.03.31 17.06
2019.03.31 17.36
2019.03.31 18.07
2019.03.31 18.37
2019.03.31 19.07
2019.03.31 19.37
2019.03.31 20.07
2019.03.31 20.38
2019.03.31 21.08
2019.03.31 21.38
2019.03.31 22.09
2019.03.31 22.39
2019.03.31 23.09
2019.03.31 23.39
2019.04.01 0.1
2019.04.01 0.4
2019.04.01 1.1
2019.04.01 1.4
2019.04.01 2.11
2019.04.01 2.41
2019.04.01 3.11
2019.04.01 3.41
2019.04.01 4.12
2019.04.01 4.42
2019.04.01 5.12
2019.04.01 5.42
2019.04.01 6.13
2019.04.01 6.43
2019.04.01 7.13
2019.04.01 7.43
2019.04.01 8.13
2019.04.01 8.44
2019.04.01 9.14
2019.04.01 9.44
2019.04.01 10.14
2019.04.01 10.44
2019.04.01 11.14
2019.04.01 11.44
2019.04.01 12.15
2019.04.01 12.45
2019.04.01 13.15
2019.04.01 13.45
2019.04.01 14.15
2019.04.01 14.45
2019.04.01 15.15
2019.04.01 15.45
2019.04.01 16.16
2019.04.01 16.46
2019.04.01 17.16
2019.04.01 17.46
2019.04.01 18.16
2019.04.01 18.46
2019.04.01 19.16
2019.04.01 19.47
2019.04.01 20.17
2019.04.01 20.47
2019.04.01 21.17
2019.04.01 21.48
2019.04.01 22.18
2019.04.01 22.48
2019.04.01 23.18
2019.04.01 23.48
2019.04.02 0.19
2019.04.02 0.49
2019.04.02 1.19
2019.04.02 1.49
2019.04.02 2.19
2019.04.02 2.5
2019.04.02 3.2
2019.04.02 3.5
2019.04.02 4.2
2019.04.02 4.51
2019.04.02 5.21
2019.04.02 5.51
2019.04.02 6.21
2019.04.02 6.51
2019.04.02 7.22
2019.04.02 7.52
2019.04.02 8.22
2019.04.02 8.52
2019.04.02 9.22
2019.04.02 9.52
2019.04.02 10.22
2019.04.02 10.52
2019.04.02 11.22
2019.04.02 11.53
2019.04.02 12.23
2019.04.02 12.53
2019.04.02 13.23
2019.04.02 13.53
2019.04.02 14.23
2019.04.02 14.53
2019.04.02 15.23
2019.04.02 15.54
2019.04.02 16.24
2019.04.02 16.54
2019.04.02 17.24
2019.04.02 17.55
2019.04.02 18.25
2019.04.02 18.55
2019.04.02 19.25
2019.04.02 19.55
2019.04.02 20.26
2019.04.02 20.56
2019.04.02 21.26
2019.04.02 21.56
2019.04.02 22.27
2019.04.02 22.57
2019.04.02 23.27
2019.04.02 23.57
2019.04.03 0.27
2019.04.03 0.57
2019.04.03 1.28
2019.04.03 1.58
2019.04.03 2.28
2019.04.03 2.58
2019.04.03 3.29
2019.04.03 3.59
2019.04.03 4.29
2019.04.03 4.59
2019.04.03 5.3
2019.04.03 6
2019.04.03 6.3
2019.04.03 7
2019.04.03 7.3
2019.04.03 8
2019.04.03 8.3
2019.04.03 9.01
2019.04.03 9.31
2019.04.03 10.01
2019.04.03 10.31
2019.04.03 11.01
2019.04.03 11.31
2019.04.03 12.02
2019.04.03 12.32
2019.04.03 13.02
2019.04.03 13.32
2019.04.03 14.02
2019.04.03 14.32
2019.04.03 15.03
2019.04.03 15.33
2019.04.03 16.03
2019.04.03 16.33
2019.04.03 17.03
2019.04.03 17.33
2019.04.03 18.04
2019.04.03 18.34
2019.04.03 19.04
2019.04.03 19.34
2019.04.03 20.04
2019.04.03 20.34
2019.04.03 21.04
2019.04.03 21.35
2019.04.03 22.05
2019.04.03 22.35
2019.04.03 23.05
2019.04.03 23.35
2019.04.04 0.05
2019.04.04 0.35
2019.04.04 1.05
2019.04.04 1.35
2019.04.04 2.05
2019.04.04 2.36
2019.04.04 3.06
2019.04.04 3.36
2019.04.04 4.06
2019.04.04 4.36
2019.04.04 5.06
2019.04.04 5.37
2019.04.04 6.07
2019.04.04 6.37
2019.04.04 7.07
2019.04.04 7.37
2019.04.04 8.07
2019.04.04 8.37
2019.04.04 9.08
2019.04.04 9.38
2019.04.04 10.08
2019.04.04 10.38
2019.04.04 11.08
2019.04.04 11.38
2019.04.04 12.08
2019.04.04 12.39
2019.04.04 13.09
2019.04.04 13.39
2019.04.04 14.09
2019.04.04 14.39
2019.04.04 15.09
2019.04.04 15.39
2019.04.04 16.1
2019.04.04 16.4
2019.04.04 17.1
2019.04.04 17.4
2019.04.04 18.1
2019.04.04 18.4
2019.04.04 19.1
2019.04.04 19.4
2019.04.04 20.1
2019.04.04 20.4
2019.04.04 21.11
2019.04.04 21.41
2019.04.04 22.11
2019.04.04 22.41
2019.04.04 23.11
2019.04.04 23.41
2019.04.05 0.11
2019.04.05 0.41
2019.04.05 1.12
2019.04.05 1.42
2019.04.05 2.12
2019.04.05 2.42
2019.04.05 3.12
2019.04.05 3.42
2019.04.05 4.12
2019.04.05 4.42
2019.04.05 5.13
2019.04.05 5.43
2019.04.05 6.13
2019.04.05 6.43
2019.04.05 7.13
2019.04.05 7.43
2019.04.05 8.13
2019.04.05 8.43
2019.04.05 9.13
2019.04.05 9.44
2019.04.05 10.14
2019.04.05 10.44
2019.04.05 11.14
2019.04.05 11.44
2019.04.05 12.14
2019.04.05 12.44
2019.04.05 13.14
2019.04.05 13.44
2019.04.05 14.14
2019.04.05 14.45
2019.04.05 15.15
2019.04.05 15.45
2019.04.05 16.15
2019.04.05 16.45
2019.04.05 17.15
2019.04.05 17.46
2019.04.05 18.16
2019.04.05 18.46
2019.04.05 19.16
2019.04.05 19.46
2019.04.05 20.16
2019.04.05 20.46
2019.04.05 21.16
2019.04.05 21.46
2019.04.05 22.17
2019.04.05 22.47
2019.04.05 23.17
2019.04.05 23.47
2019.04.06 0.17
2019.04.06 0.47
2019.04.06 1.18
2019.04.06 1.48
2019.04.06 2.18
2019.04.06 2.48
2019.04.06 3.18
2019.04.06 3.48
2019.04.06 4.18
2019.04.06 4.48
2019.04.06 5.19
2019.04.06 5.49
2019.04.06 6.19
2019.04.06 6.49
2019.04.06 7.19
2019.04.06 7.49
2019.04.06 8.19
2019.04.06 8.5
2019.04.06 9.2
2019.04.06 9.5
2019.04.06 10.2
2019.04.06 10.5
2019.04.06 11.2
2019.04.06 11.5
2019.04.06 12.2
2019.04.06 12.51
2019.04.06 13.21
2019.04.06 13.51
2019.04.06 14.21
2019.04.06 14.51
2019.04.06 15.21
2019.04.06 15.51
2019.04.06 16.21
2019.04.06 16.51
2019.04.06 17.22
2019.04.06 17.52
2019.04.06 18.22
2019.04.06 18.52
2019.04.06 19.22
2019.04.06 19.52
2019.04.06 20.22
2019.04.06 20.52
2019.04.06 21.22
2019.04.06 21.53
2019.04.06 22.23
2019.04.06 22.53
2019.04.06 23.23
2019.04.06 23.53
2019.04.07 0.23
2019.04.07 0.54
2019.04.07 1.24
2019.04.07 1.54
2019.04.07 2.24
2019.04.07 2.54
2019.04.07 3.25
2019.04.07 3.55
2019.04.07 4.25
2019.04.07 4.55
2019.04.07 5.26
2019.04.07 5.56
2019.04.07 6.26
2019.04.07 6.56
2019.04.07 7.26
2019.04.07 7.57
2019.04.07 8.27
2019.04.07 8.57
2019.04.07 9.27
2019.04.07 9.57
2019.04.07 10.27
2019.04.07 10.57
2019.04.07 11.27
2019.04.07 11.58
2019.04.07 12.28
2019.04.07 12.58
2019.04.07 13.28
2019.04.07 13.58
2019.04.07 14.28
2019.04.07 14.58
2019.04.07 15.28
2019.04.07 15.59
2019.04.07 16.29
2019.04.07 16.59
2019.04.07 17.29
2019.04.07 17.59
2019.04.07 18.29
2019.04.07 18.59
2019.04.07 19.29
2019.04.07 19.59
2019.04.07 20.29
2019.04.07 21
2019.04.07 21.3
2019.04.07 22
2019.04.07 22.3
2019.04.07 23
2019.04.07 23.3
2019.04.08 0
2019.04.08 0.3
2019.04.08 1.01
2019.04.08 1.31
2019.04.08 2.01
2019.04.08 2.31
2019.04.08 3.01
2019.04.08 3.32
2019.04.08 4.02
2019.04.08 4.32
2019.04.08 5.02
2019.04.08 5.33
2019.04.08 6.03
2019.04.08 6.33
2019.04.08 7.03
2019.04.08 7.33
2019.04.08 8.03
2019.04.08 8.33
2019.04.08 9.03
2019.04.08 9.34
2019.04.08 10.04
2019.04.08 10.34
2019.04.08 11.04
2019.04.08 11.34
2019.04.08 12.04
2019.04.08 12.34
2019.04.08 13.04
2019.04.08 13.34
2019.04.08 14.04
2019.04.08 14.35
2019.04.08 15.05
2019.04.08 15.35
2019.04.08 16.05
2019.04.08 16.35
2019.04.08 17.05
2019.04.08 17.35
2019.04.08 18.05
2019.04.08 18.36
2019.04.08 19.06
2019.04.08 19.36
2019.04.08 20.06
2019.04.08 20.36
2019.04.08 21.06
2019.04.08 21.36
2019.04.08 22.07
2019.04.08 22.37
2019.04.08 23.07
2019.04.08 23.38
2019.04.09 0.08
2019.04.09 0.38
2019.04.09 1.08
2019.04.09 1.38
2019.04.09 2.09
2019.04.09 2.39
2019.04.09 3.09
2019.04.09 3.39
2019.04.09 4.1
2019.04.09 4.4
2019.04.09 5.1
2019.04.09 5.4
2019.04.09 6.1
2019.04.09 6.41
2019.04.09 7.11
2019.04.09 7.41
2019.04.09 8.11
2019.04.09 8.42
2019.04.09 9.12
2019.04.09 9.42
2019.04.09 10.12
2019.04.09 10.42
2019.04.09 11.13
2019.04.09 11.43
2019.04.09 12.13
2019.04.09 12.43
2019.04.09 13.13
2019.04.09 13.43
2019.04.09 14.13
2019.04.09 14.43
2019.04.09 15.14
2019.04.09 15.44
2019.04.09 16.14
2019.04.09 16.44
2019.04.09 17.14
2019.04.09 17.44
2019.04.09 18.14
2019.04.09 18.44
2019.04.09 19.15
2019.04.09 19.45
2019.04.09 20.15
2019.04.09 20.45
2019.04.09 21.15
2019.04.09 21.45
2019.04.09 22.15
2019.04.09 22.46
2019.04.09 23.16
2019.04.09 23.46
2019.04.10 0.16
2019.04.10 0.47
2019.04.10 1.17
2019.04.10 1.47
2019.04.10 2.17
2019.04.10 2.47
2019.04.10 3.18
2019.04.10 3.48
2019.04.10 4.18
2019.04.10 4.48
2019.04.10 5.18
2019.04.10 5.49
2019.04.10 6.19
2019.04.10 6.49
2019.04.10 7.19
2019.04.10 7.49
2019.04.10 8.19
2019.04.10 8.49
2019.04.10 9.2
2019.04.10 9.5
2019.04.10 10.2
2019.04.10 10.5
2019.04.10 11.2
2019.04.10 11.5
2019.04.10 12.2
2019.04.10 12.51
2019.04.10 13.21
2019.04.10 13.51
2019.04.10 14.21
2019.04.10 14.51
2019.04.10 15.21
2019.04.10 15.51
2019.04.10 16.22
2019.04.10 16.52
2019.04.10 17.22
2019.04.10 17.52
2019.04.10 18.22
2019.04.10 18.52
2019.04.10 19.22
2019.04.10 19.52
2019.04.10 20.23
2019.04.10 20.53
2019.04.10 21.23
2019.04.10 21.53
2019.04.10 22.24
2019.04.10 22.54
2019.04.10 23.24
2019.04.10 23.54
2019.04.11 0.24
2019.04.11 0.55
2019.04.11 1.25
2019.04.11 1.55
2019.04.11 2.25
2019.04.11 2.56
2019.04.11 3.26
2019.04.11 3.56
2019.04.11 4.26
2019.04.11 4.56
2019.04.11 5.27
2019.04.11 5.57
2019.04.11 6.27
2019.04.11 6.57
2019.04.11 7.27
2019.04.11 7.57
2019.04.11 8.28
2019.04.11 8.58
2019.04.11 9.28
2019.04.11 9.58
2019.04.11 10.28
2019.04.11 10.58
2019.04.11 11.29
2019.04.11 11.59
2019.04.11 12.29
2019.04.11 12.59
2019.04.11 13.29
2019.04.11 13.59
2019.04.11 14.29
2019.04.11 15
2019.04.11 15.3
2019.04.11 16
2019.04.11 16.3
2019.04.11 17
2019.04.11 17.3
2019.04.11 18
2019.04.11 18.3
2019.04.11 19.01
2019.04.11 19.31
2019.04.11 20.01
2019.04.11 20.31
2019.04.11 21.01
2019.04.11 21.31
2019.04.11 22.02
2019.04.11 22.32
2019.04.11 23.02
2019.04.11 23.32
2019.04.12 0.02
2019.04.12 0.33
2019.04.12 1.03
2019.04.12 1.33
2019.04.12 2.04
2019.04.12 2.34
2019.04.12 3.04
2019.04.12 3.34
2019.04.12 4.04
2019.04.12 4.35
2019.04.12 5.05
2019.04.12 5.35
2019.04.12 6.05
2019.04.12 6.35
2019.04.12 7.06
2019.04.12 7.36
2019.04.12 8.06
2019.04.12 8.36
2019.04.12 9.06
2019.04.12 9.36
2019.04.12 10.06
2019.04.12 10.36
2019.04.12 11.06
2019.04.12 11.37
2019.04.12 12.07
2019.04.12 12.37
2019.04.12 13.07
2019.04.12 13.37
2019.04.12 14.07
>>>>>>> 710dc9b40dc2c2dbf8fd7d5525b72669f1e8f08d
