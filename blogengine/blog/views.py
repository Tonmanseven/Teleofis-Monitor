import subprocess
import os
import datetime, time, json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, StreamingHttpResponse
# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3, base64, zlib
from blog.models import Teleofis
from .forms import UserForm, SensForm

now = datetime.datetime.now()

# Объядиняем столбцы времени и дат в один список
def date_Time_edit(list_1, list_2):
    my_data = list(list_1)
    my_time = list_2
    
    l = len(list_2)
    j = 0
    new_time = []

    while j< l:
        new_time.append("{}".format(my_time[j]))
        j += 1

    line = len(list_1)
    i = 0
    arr3 = []

    while i < line:
        arr3.append(my_data[i] +  " " + new_time[i])   
        i+= 1  

    return arr3

######## data from luna server ########
 #### IESK ####
def easy_stastion_3():
    conn = sqlite3.connect('routers.sqlite3')

    with conn:
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()
        # Открываем таблицу, если ее нет то Создаем таблицу
        cursor.execute('SELECT State, Time, date FROM mark9_state ORDER BY id DESC LIMIT 24')
        state_mark_9 = cursor.fetchall()  ## выбирается последняя запись
        state9 = []
        time_state9 = []
        date_now9 =[]

        for row in state_mark_9:
            state9.append(row[0])
            time_state9.append(row[1])
            date_now9.append(row[2])


        cursor.execute('SELECT State, Time, date FROM mark2_state ORDER BY id DESC LIMIT 24')
        state_mark_2 = cursor.fetchall()  ## выбирается последняя запись
        state2 = []
        time_state2 = []
        date_now2 =[]

        for row in state_mark_2:
            state2.append(row[0])
            time_state2.append(row[1])
            date_now2.append(row[2])

        cursor.execute('SELECT State, Time, date FROM mark1_state ORDER BY id DESC LIMIT 24')
        state_mark_1 = cursor.fetchall()  ## выбирается последняя запись
        #rint(state_mark_1)
        state1 = []
        time_state1 = []
        date_now1 = []

        for row in state_mark_1:
            state1.append(row[0])
            time_state1.append(row[1])
            date_now1.append(row[2])

        ####################################### Опора 2 №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

        cursor.execute('SELECT State, Time, date FROM mark3_state ORDER BY id DESC LIMIT 24')
        state_mark_3 = cursor.fetchall()  ## выбирается последняя запись
        state3 = []
        time_state3 = []
        date_now3 = []

        for row in state_mark_3:
            state3.append(row[0])
            time_state3.append(row[1])
            date_now3.append(row[2])

        cursor.execute('SELECT State, Time, date FROM mark4_state ORDER BY id DESC LIMIT 24')
        state_mark_4 = cursor.fetchall()  ## выбирается последняя запись
        state4 = []
        time_state4 = []
        date_now4 = []

        for row in state_mark_4:
            state4.append(row[0])
            time_state4.append(row[1])
            date_now4.append(row[2])

        cursor.execute('SELECT State, Time, date FROM mark5_state ORDER BY id DESC LIMIT 24')
        state_mark_5 = cursor.fetchall()  ## выбирается последняя запись
        state5 = []
        time_state5 = []
        date_now5 = []

        for row in state_mark_5:
            state5.append(row[0])
            time_state5.append(row[1])
            date_now5.append(row[2])

    ####################################### Опора 1 №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

        cursor.execute('SELECT State, Time, date FROM mark6_state ORDER BY id DESC LIMIT 24')
        state_mark_6 = cursor.fetchall()  ## выбирается последняя запись
        state6 = []
        time_state6 = []
        date_now6 = []

        for row in state_mark_6:
            state6.append(row[0])
            time_state6.append(row[1])
            date_now6.append(row[2])

        cursor.execute('SELECT State, Time, date FROM mark7_state ORDER BY id DESC LIMIT 24')
        state_mark_7 = cursor.fetchall()  ## выбирается последняя запись
        state7 = []
        time_state7 = []
        date_now7 = []

        for row in state_mark_7:
            state7.append(row[0])
            time_state7.append(row[1])
            date_now7.append(row[2])

        cursor.execute('SELECT State, Time, date FROM mark8_state ORDER BY id DESC LIMIT 24')
        state_mark_8 = cursor.fetchall()  ## выбирается последняя запись
        state8 = []
        time_state8 = []
        date_now8 = []

        for row in state_mark_8:
            state8.append(row[0])
            time_state8.append(row[1])  
            date_now8.append(row[2])

    opora_all = {

            ########### IESK ############
        'state_mark_1': state1,
        'time_mark_1': time_state1,
        'date_mark_1': date_now1,
        'state_mark_2': state2,
        'time_mark_2': time_state2,
        'date_mark_2': date_now2,
        'state_mark_9': state9,
        'time_mark_9': time_state9,
        'date_mark_9': date_now9,
        
        'state_mark_3': state3,
        'time_mark_3': time_state3,
        'date_mark_3': date_now3,
        'state_mark_4': state4,
        'time_mark_4': time_state4,
        'date_mark_4': date_now4,
        'state_mark_5': state5,
        'time_mark_5': time_state5,
        'date_mark_5': date_now5,

        'state_mark_6': state6,
        'time_mark_6': time_state6,
        'date_mark_6': date_now6,
        'state_mark_7': state7,
        'time_mark_7': time_state7,
        'date_mark_7': date_now7,
        'state_mark_8': state8,
        'time_mark_8': time_state8,
        'date_mark_8': date_now8,
           
    }                

    cursor.close()
    conn.close()
    # частота выполнений 3600
    return opora_all 

######## data from fillip server ########

def fillip():
    conn = sqlite3.connect('test.sqlite3')

    with conn:
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()

        cursor.execute('SELECT State, Time, date FROM mark10_state ORDER BY id DESC LIMIT 24')
        state_mark_10 = cursor.fetchall()  ## выбирается последняя запись
        state10 = []
        time_state10 = []

        for row in state_mark_10:
            state10.append(row[0])
            time_state10.append(row[1])

        cursor.execute('SELECT State, Time, date FROM mark11_state ORDER BY id DESC LIMIT 24')
        state_mark_11 = cursor.fetchall()  ## выбирается последняя запись
        state11 = []
        time_state11 = []

        for row in state_mark_11:
            state11.append(row[0])
            time_state11.append(row[1])   

        cursor.execute('SELECT State, Time, date FROM mark12_state ORDER BY id DESC LIMIT 24')
        state_mark_12 = cursor.fetchall()  ## выбирается последняя запись
        state12 = []
        time_state12 = []

        for row in state_mark_12:
            state12.append(row[0])
            time_state12.append(row[1])    

        cursor.execute('SELECT State, Time, date FROM mark13_state ORDER BY id DESC LIMIT 24')
        state_mark_13 = cursor.fetchall()  ## выбирается последняя запись
        state13 = []
        time_state13 = []

        for row in state_mark_13:
            state13.append(row[0])
            time_state13.append(row[1])  

        cursor.execute('SELECT State, Time, date FROM mark14_state ORDER BY id DESC LIMIT 24')
        state_mark_14 = cursor.fetchall()  ## выбирается последняя запись
        state14 = []
        time_state14 = []
        date_now14 =[]

        for row in state_mark_14:
            state14.append(row[0])
            time_state14.append(row[1]) 
            date_now14.append(row[2])      

    fill_data = {

            ########### Тeстовые ############
        'state_mark_10': state10,
        'time_mark_10': time_state10,
        'state_mark_11': state11,
        'time_mark_11': time_state11,
        'state_mark_12': state12,
        'time_mark_12': time_state12, 
        'state_mark_13': state13,
        'time_mark_13': time_state13, 
            ########### Москва Билайн ############
        'state_mark_14': state14,
        'time_mark_14': time_state14,
        'date_mark_14': date_now14,
         
    }                

    cursor.close()
    conn.close()
    # частота выполнений 3600
    return fill_data   

def spb_state():

    conn = sqlite3.connect('fins.sqlite3')

    with conn:
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()
    # spb1
        cursor.execute('SELECT State, Time, date FROM spb1_state ORDER BY id DESC LIMIT 24')
        spb1_state = cursor.fetchall()  ## выбирается последняя запись
        state_spb1 = []
        time_state_sbp1 = []
        date_spb1 =[]

        for row in spb1_state:
            state_spb1.append(row[0])
            time_state_sbp1.append(row[1])
            date_spb1.append(row[2])

    # spb2
        cursor.execute('SELECT State, Time, date FROM spb2_state ORDER BY id DESC LIMIT 24')
        spb2_state = cursor.fetchall()  ## выбирается последняя запись
        state_spb2 = []
        time_state_sbp2 = []
        date_spb2 =[]

        for row in spb2_state:
            state_spb2.append(row[0])
            time_state_sbp2.append(row[1])
            date_spb2.append(row[2])

    # spb3
        cursor.execute('SELECT State, Time, date FROM spb3_state ORDER BY id DESC LIMIT 24')
        spb3_state = cursor.fetchall()  ## выбирается последняя запись
        state_spb3 = []
        time_state_sbp3 = []
        date_spb3 =[]

        for row in spb3_state:
            state_spb3.append(row[0])
            time_state_sbp3.append(row[1])
            date_spb3.append(row[2])  

    # spb4
        cursor.execute('SELECT State, Time, date FROM spb4_state ORDER BY id DESC LIMIT 24')
        spb4_state = cursor.fetchall()  ## выбирается последняя запись
        state_spb4 = []
        time_state_sbp4 = []
        date_spb4 =[]

        for row in spb4_state:
            state_spb4.append(row[0])
            time_state_sbp4.append(row[1])
            date_spb4.append(row[2])                
    # spb5
        cursor.execute('SELECT State, Time, date FROM spb5_state ORDER BY id DESC LIMIT 24')
        spb5_state = cursor.fetchall()  ## выбирается последняя запись
        state_spb5 = []
        time_state_sbp5 = []
        date_spb5 =[]

        for row in spb5_state:
            state_spb5.append(row[0])
            time_state_sbp5.append(row[1])
            date_spb5.append(row[2])
    # spb6
        cursor.execute('SELECT State, Time, date FROM spb6_state ORDER BY id DESC LIMIT 24')
        spb6_state = cursor.fetchall()  ## выбирается последняя запись
        state_spb6 = []
        time_state_sbp6 = []
        date_spb6 =[]

        for row in spb6_state:
            state_spb6.append(row[0])
            time_state_sbp6.append(row[1])
            date_spb6.append(row[2])

    spb_data = {

        #### МРСК СЗ ####
        'state_spb1': state_spb1,
        'time_state_sbp1': time_state_sbp1,
        'date_spb1': date_spb1,

        'state_spb2': state_spb2,
        'time_state_sbp2': time_state_sbp2,
        'date_spb2': date_spb2,

        'state_spb3': state_spb3,
        'time_state_sbp3': time_state_sbp3,
        'date_spb3': date_spb3,
        #### СИБУР ####
        'state_spb4': state_spb4,
        'time_state_sbp4': time_state_sbp4,
        'date_spb4': date_spb4,

        'state_spb5': state_spb5,
        'time_state_sbp5': time_state_sbp5,
        'date_spb5': date_spb5,

        'state_spb6': state_spb6,
        'time_state_sbp6': time_state_sbp6,
        'date_spb6': date_spb6,

    }                

    cursor.close()
    conn.close()
    # частота выполнений 3600
    return spb_data   

######################################################################################################

def posts(request):
    return render(request, 'blog/iesk.html')    
            # Create your views here
def posts_list(request):
    return render(request, 'blog/index.html') 

def station_1(request):

    data_opora_3 = easy_stastion_3()

    state1 = data_opora_3['state_mark_1']
    time1 = data_opora_3['time_mark_1']
    date1 = data_opora_3['date_mark_1']
    state2 = data_opora_3['state_mark_2']
    time2 = data_opora_3['time_mark_2']
    date2 = data_opora_3['date_mark_2']
    state9 = data_opora_3['state_mark_9']
    time9 = data_opora_3['time_mark_9']
    date9 = data_opora_3['date_mark_9']

    my_datetime1 = date_Time_edit(date1, time1)
    my_datetime2 = date_Time_edit(date2, time2)
    my_datetime9 = date_Time_edit(date9, time9)

    return render(request, 'blog/station_3.html', context={'mark009': state9[0], 'mark002': state2[0],
                                                           'mark001': state1[0], 'times1': my_datetime1,                                                  
                                                            'state1': state1, 'times2': my_datetime2,
                                                            'state2': state2, 'times9': my_datetime9,
                                                            'state9': state9,
                                                           })


def station_2(request):

    data_opora_2 = easy_stastion_3()

    state3 = data_opora_2['state_mark_3']
    time3 = data_opora_2['time_mark_3']
    date3 = data_opora_2['date_mark_3']
    state4 = data_opora_2['state_mark_4']
    time4 = data_opora_2['time_mark_4']
    date4 = data_opora_2['date_mark_4']
    state5 = data_opora_2['state_mark_5']
    time5 = data_opora_2['time_mark_5']
    date5 = data_opora_2['date_mark_5']

    my_datetime3 = date_Time_edit(date3, time3)
    my_datetime4 = date_Time_edit(date4, time4)
    my_datetime5 = date_Time_edit(date5, time5)

    return render(request, 'blog/station_2.html', context={'mark003': state3[0], 'mark004': state4[0],
                                                           'mark005': state5[0], 'times3': my_datetime3,
                                                           'state3': state3, 'times4': my_datetime4,
                                                           'state4': state4, 'times5': my_datetime5,
                                                           'state5': state5})


def station_3(request):
    data_opora = easy_stastion_3()

    state6 = data_opora['state_mark_6']
    time6 = data_opora['time_mark_6']
    date6 = data_opora['date_mark_6']
    state7 = data_opora['state_mark_7']
    time7 = data_opora['time_mark_7']
    date7 = data_opora['date_mark_7']
    state8 = data_opora['state_mark_8']
    time8 = data_opora['time_mark_8']
    date8 = data_opora['date_mark_8']

    my_datetime6 = date_Time_edit(date6, time6)
    my_datetime7 = date_Time_edit(date7, time7)
    my_datetime8 = date_Time_edit(date8, time8)

    return render(request, 'blog/station_1.html', context={'mark006': state6[0], 'mark007': state7[0],
                                                           'mark008': state8[0], 'times6': my_datetime6,
                                                           'state6': state6, 'times7': my_datetime7,
                                                           'state7': state7, 'times8': my_datetime8,
                                                           'state8': state8})

def test(request):
    useform = UserForm()
    data_opora = fillip()

    state14 = data_opora['state_mark_14']
    time14 = data_opora['time_mark_14']
    date14 = data_opora['date_mark_14']

    my_datetime = date_Time_edit(date14, time14)

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
    
    data_fins = spb_state()

    state_spb1 = data_fins['state_spb1']
    time_spb1 = data_fins['time_state_sbp1']
    date_spb1 = data_fins['date_spb1']

    state_spb2 = data_fins['state_spb2']
    time_spb2 = data_fins['time_state_sbp2']
    date_spb2 = data_fins['date_spb2']

    state_spb3 = data_fins['state_spb3']
    time_spb3 = data_fins['time_state_sbp3']
    date_spb3 = data_fins['date_spb3']

    my_sbp1 = date_Time_edit(date_spb1, time_spb1)
    my_sbp2 = date_Time_edit(date_spb2, time_spb2)
    my_sbp3 = date_Time_edit(date_spb3, time_spb3)
    
    return render(request, 'blog/fins.html', context={     'spb1': state_spb1[0], 'spb2': state_spb2[0], 'spb3': state_spb3[0],
                                                           'times10': my_sbp1,
                                                           'state10': state_spb1, 'times11': my_sbp2,
                                                           'state11': state_spb2, 'times12': my_sbp3,
                                                           'state12': state_spb3, })

def sibur(request):

    
    data_fins = spb_state()

    state_spb4 = data_fins['state_spb4']
    time_spb4 = data_fins['time_state_sbp4']
    date_spb4 = data_fins['date_spb4']

    state_spb5 = data_fins['state_spb5']
    time_spb5 = data_fins['time_state_sbp5']
    date_spb5 = data_fins['date_spb5']

    state_spb6 = data_fins['state_spb6']
    time_spb6 = data_fins['time_state_sbp6']
    date_spb6 = data_fins['date_spb6']

    my_sbp4 = date_Time_edit(date_spb4, time_spb4)
    my_sbp5 = date_Time_edit(date_spb5, time_spb5)
    my_sbp6 = date_Time_edit(date_spb6, time_spb6)
    
    return render(request, 'blog/sibur.html', context={     'spb4': state_spb4[0], 'spb5': state_spb5[0], 'spb6': state_spb6[0],
                                                           'times10': my_sbp4,
                                                           'state10': state_spb4, 'times11': my_sbp5,
                                                           'state11': state_spb5, 'times12': my_sbp6,
                                                           'state12': state_spb6, })

def tele_robot(request):
    
    teleofis_new = Teleofis()
    
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

        #teleofis_new.app = hostname
        # teleofis_new.status = status
        # teleofis_new.timestamp = new_time
        # teleofis_new.save()
               
        
        
    return render(request, 'blog/teleofis_state.html')                                                                      

def todo(namespace):
    return namespace

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