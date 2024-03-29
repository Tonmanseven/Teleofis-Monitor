
import subprocess
import os, sys
import json, datetime, time, hashlib
from datetime import datetime as dateone
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.core.files import File
# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3, base64, zlib
from blog.models import telelog, teleping, telemetry
from .forms import UserForm, SensForm, FileForm
from django.http import JsonResponse, FileResponse
from static.files.getexel import write_exel

######## data from server ########
   
def new_ping(hname, daterange):
    start = daterange[0:10]
    end = daterange[13:]

    start_date =dateone.strptime(start, "%m/%d/%Y")
    end_date = dateone.strptime(end, "%m/%d/%Y") + datetime.timedelta(days=1)

    tele_data = teleping.objects.filter(host = '{}'.format(hname), timestamp__range=(start_date, end_date)).order_by('timestamp')
    metry_data = telemetry.objects.filter(tele_name = '{}'.format(hname), timetel__range=(start_date, end_date)).order_by('timetel')

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

    k = 0
    aumm = []
    temp_cpu = []
    board_cpu = []
    vin_value = []
    date_metry = []
    for l in metry_data:
        aumm.append(l)
        
        cp = aumm[k].cpu_temp
        brd = aumm[k].board_temp
        vn = aumm[k].vin

        if cp in [' ']:
            cp = 0   
        else:
            cp = float(aumm[k].cpu_temp)

        if brd in [' ']:
            brd = 0    
        else:
           brd = float(aumm[k].board_temp) 

        if vn in [' ']:
            vn = 0  
        else:
            vn = float(aumm[k].vin)        

        temp_cpu.append(cp)
        board_cpu.append(brd)
        vin_value.append(vn)

        date_metry.append(aumm[k].timetel.strftime('%d-%m-%Y %H:%M'))  
        k += 1


    opora_all = {
        
        'host_router': host,
        'vpn_router': vpn,
        'internet_router': inet,
        'date_router': dt_pub,

        'temp_cpu': temp_cpu,
        'temp_board': board_cpu,
        'vin_value': vin_value,
        'date_metry': date_metry,
            
    }                

    # частота выполнений 3600
    return opora_all 

#### Небольшой api для iPhone 
def swift_log(hname, start, end):

    start_date = dateone.strptime(start, "%Y-%m-%d")
    end_date = dateone.strptime(end, "%Y-%m-%d")+ datetime.timedelta(days=1)

    log_router = telelog.objects.filter(log_name = '{}'.format(hname), log_time__range =(start_date, end_date)).order_by('log_time')

    j = 0
    auff = []
    host = []
    text = []
    dt_pub = []
    for i in log_router:
        auff.append(i)
        host.append(auff[j].log_name)
        text.append(str(auff[j].log_text))
        dt_pub.append(auff[j].log_time.strftime('%d-%m-%Y'))  
        j += 1 

    opora_all = {
        
        'host_log': host,
        'text_log': text,
        'date_log': dt_pub,
            
    }                

    # частота выполнений 3600
    return opora_all   

def logexel(hname, start, end):

    start_date = dateone.strptime(start, "%m/%d/%Y")
    end_date = dateone.strptime(end, "%m/%d/%Y")+ datetime.timedelta(days=1)

    log_router = telelog.objects.filter(log_name = '{}'.format(hname), log_time__range =(start_date, end_date)).order_by('log_time')

    j = 0
    auff = []
    host = []
    text = []
    dt_pub = []
    for i in log_router:
        auff.append(i)
        host.append(auff[j].log_name)
        text.append(str(auff[j].log_text))
        dt_pub.append(auff[j].log_time.strftime('%d-%m-%Y'))  
        j += 1 

    opora_all = {
        
        'host_log': host,
        'text_log': text,
        'date_log': dt_pub,
            
    }                

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

        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(end, "%m/%d/%Y")+ datetime.timedelta(days=1)
#wirenboard-AXGDGLNQ
        log_mark1 = telelog.objects.filter(log_name = 'wirenboard-AXGDGLNQ', log_time__range =(start_date, end_date)).order_by('log_time') 
        
        ping_spb4 = new_ping('wirenboard-AXGDGLNQ', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']
       
        cpu_spb4 = ping_spb4['temp_cpu']
        board_spb4 = ping_spb4['temp_board']
        vin_spb4 = ping_spb4['vin_value']
        tel_spb4 = ping_spb4['date_metry']
        
        return render(request, 'blog/post1_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1,
                    'cpu':cpu_spb4, 'board':board_spb4, 'vin': vin_spb4, 'teltime': tel_spb4 })

    else:
        start = datetime.datetime.strftime( datetime.datetime.now(), "%m/%d/%Y")
        daterange = '{} - {}'.format(start, start)
        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(start, "%m/%d/%Y")+ datetime.timedelta(days=1)

        log_mark1 = telelog.objects.filter(log_name = 'wirenboard-AXGDGLNQ', log_time__range =(start_date, end_date)).order_by('log_time') 
        
        ping_spb4 = new_ping('wirenboard-AXGDGLNQ', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        cpu_spb4 = ping_spb4['temp_cpu']
        board_spb4 = ping_spb4['temp_board']
        vin_spb4 = ping_spb4['vin_value']
        tel_spb4 = ping_spb4['date_metry']
        print(cpu_spb4)

        return render(request, 'blog/post1_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4,
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, 
                    'cpu':cpu_spb4, 'board':board_spb4, 'vin': vin_spb4, 'teltime': tel_spb4 })

def post2_iesk(request):
    sensform = SensForm()
    
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(end, "%m/%d/%Y")+ datetime.timedelta(days=1)

        log_mark1 = telelog.objects.filter(log_name = 'wirenboard-AD7R5B2', log_time__range =(start_date, end_date)).order_by('log_time') 
        
        ping_spb4 = new_ping('wirenboard-AD7R5B2', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        cpu_spb4 = ping_spb4['temp_cpu']
        board_spb4 = ping_spb4['temp_board']
        vin_spb4 = ping_spb4['vin_value']
        tel_spb4 = ping_spb4['date_metry']

        return render(request, 'blog/post2_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1,
                    'cpu':cpu_spb4, 'board':board_spb4, 'vin': vin_spb4, 'teltime': tel_spb4 })

    else:
        start = datetime.datetime.strftime( datetime.datetime.now(), "%m/%d/%Y")
        daterange = '{} - {}'.format(start, start)
        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(start, "%m/%d/%Y")+ datetime.timedelta(days=1)
        log_mark1 = telelog.objects.filter(log_name = 'wirenboard-AD7R5B2', log_time__range =(start_date, end_date)).order_by('log_time') 
        
        ping_spb4 = new_ping('wirenboard-AD7R5B2', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        cpu_spb4 = ping_spb4['temp_cpu']
        board_spb4 = ping_spb4['temp_board']
        vin_spb4 = ping_spb4['vin_value']
        tel_spb4 = ping_spb4['date_metry']

        return render(request, 'blog/post2_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4,
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1,
                    'cpu':cpu_spb4, 'board':board_spb4, 'vin': vin_spb4, 'teltime': tel_spb4 })

def post3_iesk(request):
    sensform = SensForm()
    
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(end, "%m/%d/%Y")+ datetime.timedelta(days=1)

        log_mark1 = telelog.objects.filter(log_name = 'wirenboard-AO5Y5KPU', log_time__range =(start_date, end_date)).order_by('log_time') 
        
        ping_spb4 = new_ping('wirenboard-AO5Y5KPU', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        cpu_spb4 = ping_spb4['temp_cpu']
        board_spb4 = ping_spb4['temp_board']
        vin_spb4 = ping_spb4['vin_value']
        tel_spb4 = ping_spb4['date_metry']

        return render(request, 'blog/post3_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4,  
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1,
                    'cpu':cpu_spb4, 'board':board_spb4, 'vin': vin_spb4, 'teltime': tel_spb4 })

    else:
        start = datetime.datetime.strftime( datetime.datetime.now(), "%m/%d/%Y")
        daterange = '{} - {}'.format(start, start)
        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(start, "%m/%d/%Y")+ datetime.timedelta(days=1)

        log_mark1 = telelog.objects.filter(log_name = 'wirenboard-AO5Y5KPU', log_time__range =(start_date, end_date)).order_by('log_time') 
        
        ping_spb4 = new_ping('wirenboard-AO5Y5KPU', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        cpu_spb4 = ping_spb4['temp_cpu']
        board_spb4 = ping_spb4['temp_board']
        vin_spb4 = ping_spb4['vin_value']
        tel_spb4 = ping_spb4['date_metry']

        return render(request, 'blog/post3_iesk.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1,
                    'cpu':cpu_spb4, 'board':board_spb4, 'vin': vin_spb4, 'teltime': tel_spb4 })
### BEELINE ###    
def beeline(request):
    
    sensform = SensForm()
    
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = datetime.datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.datetime.strptime(end, "%m/%d/%Y") + datetime.timedelta(days=1) 

        log_mark1 = telelog.objects.filter(log_name = 'mark_014', log_time__range =(start_date, end_date)).order_by('log_time') 

        ping_spb4 = new_ping('mark_014', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        return render(request, 'blog/beeline.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1, })
    else:
        start = datetime.datetime.strftime( datetime.datetime.now(), "%m/%d/%Y")
        daterange = '{} - {}'.format(start, start)
        ping_spb4 = new_ping('mark_014', daterange)
        vpn_spb4 = ping_spb4['vpn_router']
        inet_spb4 = ping_spb4['internet_router']
        date_spb4 = ping_spb4['date_router']

        start_date = datetime.datetime.strptime(start, "%m/%d/%Y")
        end_date = datetime.datetime.strptime(start, "%m/%d/%Y") + datetime.timedelta(days=1) 

        log_mark1 = telelog.objects.filter(log_name = 'mark_014', log_time__range =(start_date, end_date)).order_by('log_time') 

        return render(request, 'blog/beeline.html', context={ 'form': sensform, 'inet_router1': inet_spb4, 
                    'times_router1': date_spb4, 'vpn_router1': vpn_spb4, 'table_router1': log_mark1,})
### MRSKSZ ###
def mrks(request):
    sensform = SensForm()
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(end, "%m/%d/%Y")+ datetime.timedelta(days=1)

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
        start = datetime.datetime.strftime( datetime.datetime.now(), "%m/%d/%Y")
        daterange = '{} - {}'.format(start, start)

        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(start, "%m/%d/%Y")+ datetime.timedelta(days=1)

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
### SIBUR ###
def sibur(request):
    sensform = SensForm()
    if request.method == "POST":
        daterange = request.POST.get("daterange")
        
        start = daterange[0:10]
        end = daterange[13:]

        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(end, "%m/%d/%Y")+ datetime.timedelta(days=1)

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
        start = datetime.datetime.strftime( datetime.datetime.now(), "%m/%d/%Y")
        daterange = '{} - {}'.format(start, start)

        start_date = dateone.strptime(start, "%m/%d/%Y")
        end_date = dateone.strptime(start, "%m/%d/%Y")+ datetime.timedelta(days=1)

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

def tele_robot(request):
    
    teleofis_new = teleping()
   
    
    if request.method == "GET":
        
        tel_data = request.GET.get("data")
        data = decript(tel_data)
        hostname = data["hostname"]
        statusList = data["statusList"]
        logList = data["logList"]
        telemetryList = data["telemetryList"]

        if (len(logList) > 0):
            for item in logList:
                tele_log = telelog()
                
                text = item["text"] ## - текст события 
                timestamp_i = item["timestamp"] # - время события
                #print(text, ": ", timestamp_i)
                logtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp_i))

                tele_log.log_name = hostname
                tele_log.log_text = text
                tele_log.log_time = logtime

                tele_log.save()    

        print(telemetryList)
        if (len(telemetryList) > 0):
            for item in telemetryList:
                metry = telemetry()

                time_i = item["timestamp"]
                tele_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_i))
                v_in = item["vIn"] ## - напр на входе
                
                
                if ("boardTemp" in item):
                    brdTemp = item["boardTemp"] ## - темп на борту
                else: 
                    brdTemp = " "

                if ("cpuTemp" in item):
                    cpuTemp = item["cpuTemp"] ## - темп процессора 
                else: 
                    cpuTemp = " "

                metry.vin = v_in
                metry.timetel = tele_time
                metry.cpu_temp = cpuTemp
                metry.board_temp = brdTemp
                metry.tele_name = hostname

                metry.save()

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

    return render(request, 'blog/teleofis_state.html') 

def swift(request):
    
    if request.method == "GET":

        hostname = request.GET.get("hostname")
        start = request.GET.get("start")
        end = request.GET.get("end")
        
        log_router = swift_log(hostname, start, end)

        log_text = log_router['text_log']
        log_date = log_router['date_log']

        message = []
        for i,j in zip(log_date, log_text):
            message.append("{} {}".format(i, j))
        
        new_jsn = []
        nam = []
        for n in message:
            new_jsn = {"hostname": hostname, "logtext": n}
            nam.append(new_jsn)
        print(nam)
        return JsonResponse(nam , safe=False)
    return render(request, 'blog/swift.html') 
                                                                           
def work_exel(request):
    sensform = SensForm()
    if request.method == "POST":
        daterange = request.POST.get("daterange")

        start = daterange[0:10]
        end = daterange[13:]

        #getdate(start, end)

        mk1 = logexel("wirenboard-AXGDGLNQ", start, end)
        mk2 = logexel("wirenboard-AD7R5B2", start, end)
        mk3 = logexel("wirenboard-AO5Y5KPU", start, end)
       
        mk14 = logexel("mark_014", start, end)

        sp1 = logexel("spb_001", start, end)
        sp2 = logexel("spb_002",start, end)
        mrs = logexel("MRSKSZ_002", start, end)

        sp4 = logexel("spb_004", start, end)
        sp5 = logexel("spb_005", start, end)
        sp6 = logexel("spb_006", start, end)

        log_mk1 = mk1['text_log']
        log_mk2 = mk2['text_log']
        log_mk3 = mk3['text_log']
        log_bee = mk14['text_log']
        log_spb1 = sp1['text_log']
        log_spb2 = sp2['text_log']
        log_mrs = mrs['text_log']
        log_spb4 = sp4['text_log']
        log_spb5 = sp5['text_log']
        log_spb6 = sp6['text_log']

        log_iesk = [log_mk1, log_mk2, log_mk3]
        log_mrsk = [log_spb1, log_spb2, log_mrs]
        log_sibur = [log_spb4, log_spb5, log_spb6]
        write_exel(log_iesk, log_bee, log_mrsk, log_sibur)
        
        response = FileResponse(open('/home/pluto/file/teleofismonitor/blogengine/static/files/telemonitor.xls', 'rb'))
        response['Content-Disposition'] = 'attachment; filename="telemonitor.xls"'
        return response
        
    return render(request, 'blog/fromexel.html', context={ 'form': sensform}) 

def handle_uploaded_file(f):
    with open('/home/pluto/file/teleofismonitor/blogengine/static/files/telerobot.py', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def filexel(f):
    with open('/home/bulat/Git/teleofismonitor/blogengine/telemonitor.xls', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)            

def tele_file(request):
    filefome = FileForm()
    
    path_file = '/home/pluto/file/teleofismonitor/blogengine/static/files/telerobot.py'

    md5str = GetHashMd5(path_file)

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
           handle_uploaded_file(request.FILES['fileform'])    
           return HttpResponseRedirect('teleofis_files.html')
    else:
        form = FileForm()    

    return render(request, 'blog/teleofis_files.html', context={'md5': md5str, 'file': filefome})     

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
