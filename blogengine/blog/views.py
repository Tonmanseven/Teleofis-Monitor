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


    
######################################################################################################

def posts(request):
    return render(request, 'blog/iesk.html')    
            # Create your views here
def posts_list(request):
    return render(request, 'blog/index.html') 

def station_1(request):

    useform = UserForm()
    if request.method == "POST":
        start = request.POST.get("startDate")
        end = request.POST.get("endDate")

        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")

        log_mark1 = telelog.objects.filter(log_name = 'mark_1', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark2 = telelog.objects.filter(log_name = 'mark_2', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark9 = telelog.objects.filter(log_name = 'mark_9', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = all_routers_ping('mark_001', start, end)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

<<<<<<< HEAD
        log_spb5 = all_routers_log('mark_2', start, end)
        logtime_spb5 = log_spb5['date_log']
        loghost_spb5 = log_spb5['host_log']
        logtext_spb5 = log_spb5['text_log']

        ping_spb5 = all_routers_ping('mark_2', start, end)
=======
        ping_spb5 = all_routers_ping('mark_002', start, end)
>>>>>>> 8b5ffb40f5477eddb5830b4146b32960ca010dfa
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

<<<<<<< HEAD
        log_spb6 = all_routers_log('mark_9', start, end)
        logtime_spb6 = log_spb6['date_log']
        loghost_spb6 = log_spb6['host_log']
        logtext_spb6 = log_spb6['text_log']

        ping_spb6 = all_routers_ping('mark_9', start, end)
=======
        ping_spb6 = all_routers_ping('mark_009', start, end)
>>>>>>> 8b5ffb40f5477eddb5830b4146b32960ca010dfa
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/station_3.html', context={ 'form': useform, 'inet_spb4': inet_spb4, 'inet_spb5': inet_spb5, 'inet_spb6': inet_spb6, 
                    'times_spb4': date_spb4, 'vpn_spb4': vpn_spb4, 'table_mark1': log_mark1, 'table_mark2': log_mark2, 'table_mark9': log_mark9,
                    'times_spb5': date_spb5,'vpn_spb5': vpn_spb5,  
                    'times_spb6': date_spb6,'vpn_spb6': vpn_spb6,})
    else:
        return render(request, 'blog/station_3.html', context={'form': useform})

def station_2(request):

    useform = UserForm()
    if request.method == "POST":
        start = request.POST.get("startDate")
        end = request.POST.get("endDate")
        
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")

        log_mark3 = telelog.objects.filter(log_name = 'mark_3', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark4 = telelog.objects.filter(log_name = 'mark_4', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark5 = telelog.objects.filter(log_name = 'mark_5', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = all_routers_ping('mark_003', start, end)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = all_routers_ping('mark_004', start, end)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = all_routers_ping('mark_005', start, end)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/station_2.html', context={ 'form': useform, 'inet_spb4': inet_spb4, 'inet_spb5': inet_spb5, 'inet_spb6': inet_spb6, 
                    'times_spb4': date_spb4, 'vpn_spb4': vpn_spb4, 'times_spb5': date_spb5,'vpn_spb5': vpn_spb5, 'times_spb6': date_spb6,'vpn_spb6': vpn_spb6,      
                    'table_mark1': log_mark3, 'table_mark2': log_mark4, 'table_mark9': log_mark5,})
    else:
        return render(request, 'blog/station_2.html', context={'form': useform})

def station_3(request):
    useform = UserForm()
    if request.method == "POST":
        start = request.POST.get("startDate")
        end = request.POST.get("endDate")
        
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")

        log_mark6 = telelog.objects.filter(log_name = 'mark_6', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_mark7 = telelog.objects.filter(log_name = 'mark_7', log_time__range =(start_date, end_date)).order_by('log_time')
        log_mark8 = telelog.objects.filter(log_name = 'mark_8', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = all_routers_ping('mark_006', start, end)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = all_routers_ping('mark_007', start, end)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = all_routers_ping('mark_008', start, end)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/station_1.html', context={ 'form': useform, 'inet_spb4': inet_spb4, 'inet_spb5': inet_spb5, 'inet_spb6': inet_spb6, 
                    'times_spb4': date_spb4, 'vpn_spb4': vpn_spb4, 'times_spb5': date_spb5,'vpn_spb5': vpn_spb5, 'times_spb6': date_spb6,'vpn_spb6': vpn_spb6,  
                    'table_mark1': log_mark6, 'table_mark2': log_mark7, 'table_mark9': log_mark8,})
    else:
        return render(request, 'blog/station_1.html', context={'form': useform})


def test(request):
    useform = UserForm()

    log_mark = all_routers_log('mark_014', datetime.strftime(datetime.today(), "%Y-%m-%d"), datetime.strftime(datetime.today(), "%Y-%m-%d"))
    logtime = log_mark['date_log']
    loghost = log_mark['host_log']
    logtext = log_mark['text_log']

    data_opora = all_routers_ping('mark_014', datetime.strftime(datetime.today(), "%Y-%m-%d"), datetime.strftime(datetime.today(), "%Y-%m-%d"))
    vpn_mk14 = data_opora['vpn_router']
    inet_mk14 = data_opora['internet_router']
    date14 = data_opora['date_router']
 

    if request.method == "POST":
        start = request.POST.get("startDate")
        end = request.POST.get("endDate")
        period = "{} / {}".format(start, end)

        data_opora = all_routers_ping('mark_014', start, end)
        vpn_mk14 = data_opora['vpn_router']
        inet_mk14 = data_opora['internet_router']
        date14 = data_opora['date_router']

        log_mark = all_routers_log('mark_014', start, end)
        logtime = log_mark['date_log']
        loghost = log_mark['host_log']
        logtext = log_mark['text_log']
        
        return render(request, 'blog/test.html', context={ 'form': useform, "period": period, 
                                                            'mark014': vpn_mk14, 'times14': date14, 'loghost': loghost,
                                                            'logtime': logtime, 'logtext': logtext, 'vpn_mark_014': vpn_mk14, 'inet_mark_014': inet_mk14}
                                                           )
    else:
        return render(request, 'blog/test.html', context={ 'form': useform, 'mark014': vpn_mk14,
                                                           'times14': date14, 'loghost': loghost, 'logtime': logtime, 'logtext': logtext,
                                                           'vpn_mark_014': vpn_mk14, 'inet_mark_014': inet_mk14})

def fins(request):
    useform = UserForm()

    if request.method == "POST":
        start = request.POST.get("startDate")
        end = request.POST.get("endDate")

        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")

        log_spb1 = telelog.objects.filter(log_name = 'spb_001', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_spb2 = telelog.objects.filter(log_name = 'spb_002', log_time__range =(start_date, end_date)).order_by('log_time')
        log_spb3 = telelog.objects.filter(log_name = 'spb_003', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb1 = all_routers_ping('spb_001', start, end)
        vpn_spb1 = ping_spb1['vpn_router']
        inet_spb1 = ping_spb1['internet_router']
        date_spb1 = ping_spb1['date_router']

        ping_spb2 = all_routers_ping('spb_002', start, end)
        vpn_spb2 = ping_spb2['vpn_router']
        inet_spb2 = ping_spb2['internet_router']
        date_spb2 = ping_spb2['date_router']

        ping_spb3 = all_routers_ping('spb_003', start, end)
        vpn_spb3 = ping_spb3['vpn_router']
        inet_spb3 = ping_spb3['internet_router']
        date_spb3 = ping_spb3['date_router']

        return render(request, 'blog/fins.html', context= { 'form': useform, 'inet_spb1': inet_spb1, 'inet_spb2': inet_spb2, 'inet_spb3': inet_spb3, 
            'times_spb1': date_spb1, 'vpn_spb1': vpn_spb1, 'table_spb1': log_spb1, 'table_spb2': log_spb2, 'table_spb3': log_spb3, 'times_spb2': date_spb2,
            'vpn_spb2': vpn_spb2, 'times_spb3': date_spb3,'vpn_spb3': vpn_spb3,})
    else:
        return render(request, 'blog/fins.html', context={'form': useform})

def sibur(request):
    useform = UserForm()
    
    if request.method == "POST":
        start = request.POST.get("startDate")
        end = request.POST.get("endDate")
        
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")

        log_spb6 = telelog.objects.filter(log_name = 'spb_006', log_time__range =(start_date, end_date)).order_by('log_time') 
        log_spb5 = telelog.objects.filter(log_name = 'spb_005', log_time__range =(start_date, end_date)).order_by('log_time')
        log_spb4 = telelog.objects.filter(log_name = 'spb_004', log_time__range =(start_date, end_date)).order_by('log_time')

        ping_spb4 = all_routers_ping('spb_004', start, end)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        ping_spb5 = all_routers_ping('spb_005', start, end)
        vpn_spb5 = ping_spb5['vpn_router']
        inet_spb5 = ping_spb5['internet_router']
        date_spb5 = ping_spb5['date_router']

        ping_spb6 = all_routers_ping('spb_006', start, end)
        vpn_spb6 = ping_spb6['vpn_router']
        inet_spb6 = ping_spb6['internet_router']
        date_spb6 = ping_spb6['date_router']

        return render(request, 'blog/sibur.html', context={ 'form': useform, 'inet_spb4': inet_spb4, 'inet_spb5': inet_spb5, 'inet_spb6': inet_spb6,
                'table_spb6': log_spb6,'times_spb4': date_spb4, 'vpn_spb4': vpn_spb4, 'table_spb4': log_spb4, 'vpn_spb6': vpn_spb6,
                'times_spb5': date_spb5,'vpn_spb5': vpn_spb5,'table_spb5': log_spb5, 'times_spb6': date_spb6,})
    else:
        return render(request, 'blog/sibur.html', context={'form': useform})                                                            

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
