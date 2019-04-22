import subprocess
import os
import datetime, time, json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, StreamingHttpResponse
# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3, base64, zlib
from blog.models import telelog, teleping
from .forms import UserForm, SensForm

now = datetime.datetime.now()


######## data from luna server ########
 #### IESK ####
def all_routers_ping():
    

    opora_all = {

            ########### IESK ############
        'state_mark_1': state1,
        'date_mark_1': date_now1,

        'state_mark_2': state2,
        'date_mark_2': date_now2,

        'state_mark_9': state9,
        'date_mark_9': date_now9,
        
        'state_mark_3': state3,
        'date_mark_3': date_now3,

        'state_mark_4': state4,
        'date_mark_4': date_now4,

        'state_mark_5': state5,
        'date_mark_5': date_now5,

        'state_mark_6': state6,
        'date_mark_6': date_now6,

        'state_mark_7': state7,
        'date_mark_7': date_now7,

        'state_mark_8': state8,
        'date_mark_8': date_now8,

        'state_mark_10': state10,
        'date_mark_10': time_state10,

        'state_mark_11': state11,
        'date_mark_11': time_state11,
        
        'state_mark_12': state12,
        'date_mark_12': time_state12, 

        'state_mark_13': state13,
        'date_mark_13': time_state13, 

        'state_mark_14': state14,
        'date_mark_14': date_now14,

         #### МРСК СЗ ####
        'state_spb1': state_spb1,
        'date_spb1': date_spb1,

        'state_spb2': state_spb2,
        'date_spb2': date_spb2,

        'state_spb3': state_spb3,
        'date_spb3': date_spb3,
        #### СИБУР ####
        'state_spb4': state_spb4,
        'date_spb4': date_spb4,

        'state_spb5': state_spb5,
        'date_spb5': date_spb5,

        'state_spb6': state_spb6,
        'date_spb6': date_spb6,
           
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

    data_opora_3 = all_routers_ping()

    state1 = data_opora_3['state_mark_1']
    date1 = data_opora_3['date_mark_1']
    state2 = data_opora_3['state_mark_2']
    date2 = data_opora_3['date_mark_2']
    state9 = data_opora_3['state_mark_9']
    date9 = data_opora_3['date_mark_9']

    return render(request, 'blog/station_3.html', context={'mark009': state9[0], 'mark002': state2[0],
                                                           'mark001': state1[0], 'times1': my_datetime1,                                                  
                                                            'state1': state1, 'times2': my_datetime2,
                                                            'state2': state2, 'times9': my_datetime9,
                                                            'state9': state9,
                                                           })


def station_2(request):

    data_opora_2 = all_routers_ping()

    state3 = data_opora_2['state_mark_3']
    date3 = data_opora_2['date_mark_3']
    state4 = data_opora_2['state_mark_4']
    date4 = data_opora_2['date_mark_4']
    state5 = data_opora_2['state_mark_5']
    date5 = data_opora_2['date_mark_5']


    return render(request, 'blog/station_2.html', context={'mark003': state3[0], 'mark004': state4[0],
                                                           'mark005': state5[0], 'times3': my_datetime3,
                                                           'state3': state3, 'times4': my_datetime4,
                                                           'state4': state4, 'times5': my_datetime5,
                                                           'state5': state5})


def station_3(request):
    data_opora = all_routers_ping()

    state6 = data_opora['state_mark_6']
    date6 = data_opora['date_mark_6']
    state7 = data_opora['state_mark_7']
    date7 = data_opora['date_mark_7']
    state8 = data_opora['state_mark_8']
    date8 = data_opora['date_mark_8']


    return render(request, 'blog/station_1.html', context={'mark006': state6[0], 'mark007': state7[0],
                                                           'mark008': state8[0], 'times6': my_datetime6,
                                                           'state6': state6, 'times7': my_datetime7,
                                                           'state7': state7, 'times8': my_datetime8,
                                                           'state8': state8})

def test(request):
    useform = UserForm()
    data_opora = all_routers_ping()

    state14 = data_opora['state_mark_14']
    date14 = data_opora['date_mark_14']

    if request.method == "POST":
        start = request.POST.get("startDate")
        #end = request.POST.get("endDate")
        print(start)
        
        return render(request, 'blog/test.html', context={ 'form': useform, 'mark014': state14[0],
                                                           'times14': my_datetime,
                                                           'state14': state14})
    else:
        return render(request, 'blog/test.html', context={ 'form': useform, 'mark014': state14[0],
                                                           'times14': my_datetime,
                                                           'state14': state14})

def fins(request):
    
    data_fins = all_routers_ping()

    state_spb1 = data_fins['state_spb1']
    date_spb1 = data_fins['date_spb1']

    state_spb2 = data_fins['state_spb2']
    date_spb2 = data_fins['date_spb2']

    state_spb3 = data_fins['state_spb3']
    date_spb3 = data_fins['date_spb3']

    return render(request, 'blog/fins.html', context={     'spb1': state_spb1[0], 'spb2': state_spb2[0], 'spb3': state_spb3[0],
                                                           'times10': my_sbp1,
                                                           'state10': state_spb1, 'times11': my_sbp2,
                                                           'state11': state_spb2, 'times12': my_sbp3,
                                                           'state12': state_spb3, })

def sibur(request):

    data_fins = all_routers_ping()

    state_spb4 = data_fins['state_spb4']
    date_spb4 = data_fins['date_spb4']

    state_spb5 = data_fins['state_spb5']
    date_spb5 = data_fins['date_spb5']

    state_spb6 = data_fins['state_spb6']
    date_spb6 = data_fins['date_spb6']

    return render(request, 'blog/sibur.html', context={     'spb4': state_spb4[0], 'spb5': state_spb5[0], 'spb6': state_spb6[0],
                                                           'times10': my_sbp4,
                                                           'state10': state_spb4, 'times11': my_sbp5,
                                                           'state11': state_spb5, 'times12': my_sbp6,
                                                           'state12': state_spb6, })

def tele_robot(request):
    
    teleofis_new = teleping()
    
    if request.method == "GET":
        
        tel_data = request.GET.get("data")
        data = decript(tel_data)
        hostname = data["hostname"]
        statusList = data["statusList"]
        logList = data["logList"]

        for item in logList:
            
            text = item["text"] ## - текст события 
            timestamp_i = item["timestamp"] # - время события
            print(text, ": ", timestamp_i)

        buffer = GetAverage(statusList)
        timestamp = buffer["timestamp"] # - время пингования 
        internetStatus = buffer["internetStatus"] # 
        vpnStatus = buffer["vpnStatus"]
        datetime = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(timestamp))

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