import subprocess
import os
import datetime, time, json
from datetime import datetime, date
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, StreamingHttpResponse
# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3, base64, zlib
from blog.models import telelog, teleping
from .forms import UserForm, SensForm


######## data from server ########
def all_routers_ping(hname, startD, endD):

    start_date = datetime.strptime(startD, "%Y-%m-%d")
    end_date = datetime.strptime(endD, "%Y-%m-%d")
    
    tele_data = teleping.objects.filter(host = '{}'.format(hname), timestamp__range=(start_date, end_date)).order_by('timestamp')

    j = 0
    auff = []
    host = []
    inet = []
    vpn = []
    dt_pub = []
    for i in tele_data:
        auff.append(i)
        host.append(auff[j].host)
        inet.append(int(auff[j].inet))
        vpn.append(int(auff[j].vpn))
        dt_pub.append(auff[j].timestamp.strftime('%d-%m-%Y %H:%M'))  
        j += 1 

    opora_all = {
        
        'host_router': host,
        'vpn_router': vpn,
        'internet_router': inet,
        'date_router': dt_pub,
            
    }                

    # частота выполнений 3600
    return opora_all 

def all_routers_log(hname, startD, endD):

    start_date = datetime.strptime(startD, "%Y-%m-%d")
    end_date = datetime.strptime(endD, "%Y-%m-%d")
    
    tele_data = telelog.objects.filter(log_name = '{}'.format(hname), log_time__range =(start_date, end_date)).order_by('log_time') 

    j = 0
    auff = []
    host = []
    text_log = []
    dt_pub = []
    for i in tele_data:
        auff.append(i)
        host.append(auff[j].log_name)
        text_log.append(auff[j].log_text)
        dt_pub.append(auff[j].log_time.strftime('%d-%m-%Y %H:%M'))  
        j += 1 

    opora_all = {
        
        'host_log': host,
        'date_log': dt_pub,
        'text_log': text_log,
            
    }                

    # частота выполнений 3600
    return opora_all     

def new_ping(hname, daterange):
    start = daterange[0:10]
    end = daterange[13:]

    start_date = datetime.strptime(start, "%m/%d/%Y")
    end_date = datetime.strptime(end, "%m/%d/%Y")

    tele_data = teleping.objects.filter(host = '{}'.format(hname), timestamp__range=(start_date, end_date)).order_by('timestamp')

    j = 0
    auff = []
    host = []
    inet = []
    vpn = []
    dt_pub = []
    for i in tele_data:
        auff.append(i)
        host.append(auff[j].host)
        inet.append(int(auff[j].inet))
        vpn.append(int(auff[j].vpn))
        dt_pub.append(auff[j].timestamp.strftime('%d-%m-%Y %H:%M'))  
        j += 1 

    opora_all = {
        
        'host_router': host,
        'vpn_router': vpn,
        'internet_router': inet,
        'date_router': dt_pub,
            
    }                

    # частота выполнений 3600
    return opora_all 

#####################################################

def posts_list(request):
    return render(request, 'blog/index.html') 
### IESK ###
def post1_iesk(request):
    sensform = SensForm()
    
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.strptime(end, "%m/%d/%Y")

        log_mark1 = telelog.objects.filter(log_name = 'mark_3', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark2 = telelog.objects.filter(log_name = 'mark_4', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark9 = telelog.objects.filter(log_name = 'mark_5', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = new_ping('mark_3', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = new_ping('mark_4', daterange)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = new_ping('mark_5', daterange)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/post1_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 'inet_router2': inet_spb5, 'inet_router3': inet_spb6, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, 'table_router2': log_mark2, 'table_router3': log_mark9,
                    'times_router2': date_spb5,'vpn_router2': vpn_spb5,  
                    'times_router3': date_spb6,'vpn_router3': vpn_spb6,})

    else:
        return render(request, 'blog/post1_iesk.html', context={ 'form': sensform })

def post2_iesk(request):
    sensform = SensForm()
    
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.strptime(end, "%m/%d/%Y")

        log_mark1 = telelog.objects.filter(log_name = 'mark_6', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark2 = telelog.objects.filter(log_name = 'mark_7', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark9 = telelog.objects.filter(log_name = 'mark_8', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = new_ping('mark_6', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = new_ping('mark_7', daterange)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = new_ping('mark_8', daterange)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/post2_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 'inet_router2': inet_spb5, 'inet_router3': inet_spb6, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, 'table_router2': log_mark2, 'table_router3': log_mark9,
                    'times_router2': date_spb5,'vpn_router2': vpn_spb5,  
                    'times_router3': date_spb6,'vpn_router3': vpn_spb6,})

    else:
        return render(request, 'blog/post2_iesk.html', context={ 'form': sensform })

def post3_iesk(request):
    sensform = SensForm()
    
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.strptime(end, "%m/%d/%Y")

        log_mark1 = telelog.objects.filter(log_name = 'mark_1', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark2 = telelog.objects.filter(log_name = 'mark_2', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark9 = telelog.objects.filter(log_name = 'mark_9', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = new_ping('mark_1', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = new_ping('mark_2', daterange)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = new_ping('mark_9', daterange)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/post3_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 'inet_router2': inet_spb5, 'inet_router3': inet_spb6, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, 'table_router2': log_mark2, 'table_router3': log_mark9,
                    'times_router2': date_spb5,'vpn_router2': vpn_spb5,  
                    'times_router3': date_spb6,'vpn_router3': vpn_spb6,})

    else:
        return render(request, 'blog/post3_iesk.html', context={ 'form': sensform })
### BEELINE ###    
def beeline(request):
    sensform = SensForm()
    
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.strptime(end, "%m/%d/%Y")

        log_mark1 = telelog.objects.filter(log_name = 'mark_014', log_time__range =(start_date, end_date)).order_by('log_time') 

        ping_spb4 = new_ping('mark_014', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        return render(request, 'blog/beeline.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, })
    else:
        return render(request, 'blog/beeline.html', context={ 'form': sensform })
### MRSKSZ ###
def mrks(request):
    sensform = SensForm()
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.strptime(end, "%m/%d/%Y")

        log_mark1 = telelog.objects.filter(log_name = 'spb_001', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark2 = telelog.objects.filter(log_name = 'spb_002', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark9 = telelog.objects.filter(log_name = 'MRSKSZ_002', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = new_ping('spb_001', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = new_ping('spb_002', daterange)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = new_ping('MRSKSZ_002', daterange)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/mrsk.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 'inet_router2': inet_spb5, 'inet_router3': inet_spb6, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, 'table_router2': log_mark2, 'table_router3': log_mark9,
                    'times_router2': date_spb5,'vpn_router2': vpn_spb5,  
                    'times_router3': date_spb6,'vpn_router3': vpn_spb6,})

    else:
        return render(request, 'blog/mrsk.html', context={ 'form': sensform })
### SIBUR ###
def sibur(request):
    sensform = SensForm()
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.strptime(end, "%m/%d/%Y")

        log_mark1 = telelog.objects.filter(log_name = 'spb_004', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark2 = telelog.objects.filter(log_name = 'spb_005', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark9 = telelog.objects.filter(log_name = 'spb_006', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = new_ping('spb_004', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = new_ping('spb_005', daterange)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = new_ping('spb_006', daterange)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/sibur.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 'inet_router2': inet_spb5, 'inet_router3': inet_spb6, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, 'table_router2': log_mark2, 'table_router3': log_mark9,
                    'times_router2': date_spb5,'vpn_router2': vpn_spb5,  
                    'times_router3': date_spb6,'vpn_router3': vpn_spb6,})

    else:
        return render(request, 'blog/sibur.html', context={ 'form': sensform })                                                               

def tele_robot(request):
    
    teleofis_new = teleping()
    tele_log = telelog()
    
    if request.method == "GET":
        
        tel_data = request.GET.get("data")
        data = decript(tel_data)
        hostname = data["hostname"]
        statusList = data["statusList"]
        logList = data["logList"]


        if (len(logList) > 0):
            for item in logList:
                text = item["text"] ## - текст события 
                timestamp_i = item["timestamp"] # - время события
                print(text, ": ", timestamp_i)
                logtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp_i))

            tele_log.log_name = hostname
            tele_log.log_text = text
            tele_log.log_time = logtime

            tele_log.save()    

        buffer = GetAverage(statusList)
        timestamp = buffer["timestamp"] # - время пингования 
        internetStatus = buffer["internetStatus"] # 
        vpnStatus = buffer["vpnStatus"]
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

        teleofis_new.host = hostname
        teleofis_new.timestamp = datetime
        teleofis_new.inet = internetStatus
        teleofis_new.vpn = vpnStatus

        teleofis_new.save()

        print(hostname, ": ", datetime, ": ", internetStatus, ": ", vpnStatus)
          
    return render(request, 'blog/teleofis_state.html')     
                                                                           
def decript(t_data):
    
    tel_data = t_data.replace(' ', '+')
    data = tel_data.encode("utf-8")
    b64 = base64.b64decode(data)
    decompress = zlib.decompress(b64)
    original = decompress.decode("utf-8")
    data = json.loads(original)

    return data

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
