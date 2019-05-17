from django.db import models
import xlwt
import datetime
from datetime import datetime as dateone


def write_exel(iesk, beel, mrsk, sib):
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    style1 = xlwt.XFStyle()
    style1.num_format_str = 'DD-MM-YYYY'

    wb = xlwt.Workbook()
    ws = wb.add_sheet('IESK')
    wbee = wb.add_sheet('Beeline')
    w_mrsk = wb.add_sheet('MRSK_SZ')
    w_sibur = wb.add_sheet('SIBUR')

    n = 2
    a1 = 2 
    a2 = 2
    a3 = 2
    a4 = 2
    a5 = 2 
    a6 = 2
    a7 = 2
    a8 = 2

    ws.write(0, 1, 'Данные за период: ', style0)

    ws.write(0, 0, 'Пост №1 Опора типа П 203/56 кВ', style0)
    ws.write(1, 0, 'mark_3', style1)
    ws.write(2, 0, 'mark_4', style1)
    ws.write(3, 0, 'mark_5', style1)

    ws.write(5, 0, 'Пост №2 Опора типа П 203/60 кВ', style0)
    ws.write(6, 0, 'mark_6', style1)
    ws.write(7, 0, 'mark_7', style1)
    ws.write(8, 0, 'mark_8', style1)

    ws.write(10, 0, 'Пост №3 Опора КРУЭ Б 220 кВ', style0)
    ws.write(11, 0, 'mark_1', style1)
    ws.write(12, 0, 'mark_2', style1)
    ws.write(13, 0, 'mark_9', style1)

    ws.write(1, 1, 'mark_1', style1)  
    ws.write(1, 2, 'mark_2', style1)
    ws.write(1, 3, 'mark_3', style1)        
    ws.write(1, 4, 'mark_4', style1)                 
    ws.write(1, 5, 'mark_5', style1)        
    ws.write(1, 6, 'mark_6', style1)
    ws.write(1, 7, 'mark_7', style1)          
    ws.write(1, 8, 'mark_8', style1)
    ws.write(1, 9, 'mark_9', style1)
    
    for item in iesk[0]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")        
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(n, 1, item, style1)
        n += 1 

    for item in iesk[1]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")  
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("authpriv.notice dropbear Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a1, 2, item, style1)
        a1 += 1  

    for item in iesk[2]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a2, 3, item, style1)
        a2 += 1  

    for item in iesk[3]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание") 
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a3, 4, item, style1)
        a3 += 1  

    for item in iesk[4]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание") 
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a4, 5, item, style1)
        a4 += 1 
    
    for item in iesk[5]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание") 
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a5, 6, item, style1)
        a5 += 1 

    for item in iesk[6]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a6, 7, item, style1)
        a6 += 1 

    for item in iesk[7]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание") 
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a7, 8, item, style1)
        a7 += 1

    for item in iesk[8]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        ws.write(a8, 9, item, style1)
        a8 += 1

    #### beeline
    n1 = 2
    wbee.write(0, 1, 'Роутер', style0)
    wbee.write(1, 1, 'mark_014', style1)
    wbee.write(0, 0, 'Билайн (г. Москва)', style0)

    for item in beel:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")        
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        wbee.write(n1, 1, item, style1)
        n1 += 1 
        
    ############### MPCK
    w_mrsk.write(0, 0, 'МРСК СЗ', style0)

    w_mrsk.write(0, 1, 'Пост №1 Опора №108 Линия №129', style0)
    w_mrsk.write(1, 1, 'spb_001', style1)
    
    w_mrsk.write(0, 2, 'Пост №2 Опора №31 Линия №129', style0)
    w_mrsk.write(1, 2, 'spb_002', style1)
    
    w_mrsk.write(0, 3, 'Пост №3 Опора №247', style0)
    w_mrsk.write(1, 3, 'MRSKSZ_002', style1)

    n2 = 2
    n3 = 2
    n4 = 2
    
    for item in mrsk[0]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")        
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        w_mrsk.write(n2, 1, item, style1)
        n2 += 1 

    for item in mrsk[1]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")  
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        w_mrsk.write(n3, 2, item, style1)
        n3 += 1  

    for item in mrsk[2]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        w_mrsk.write(n4, 3, item, style1)
        n4 += 1
        
    ########### SIBUR
    w_sibur.write(0, 0, 'СИБУР', style0)

    w_sibur.write(0, 1, 'Панель 0.4 кВ ТП-55', style0)
    w_sibur.write(1, 1, 'spb_004', style1)
    
    w_sibur.write(0, 2, 'Трафнсформатор ТМЗ', style0)
    w_sibur.write(1, 2, 'spb_005', style1)
    
    w_sibur.write(0, 3, 'Ячейка КСО', style0)
    w_sibur.write(1, 3, 'spb_006', style1)

    n5 = 2
    n6 = 2
    n7 = 2
    
    for item in sib[0]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")        
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        w_sibur.write(n5, 1, item, style1)
        n5 += 1 

    for item in sib[1]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")  
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")
        w_sibur.write(n6, 2, item, style1)
        n6 += 1  

    for item in sib[2]:
        if ("voltage supply" in item):
            continue
        if ("switching to backup power" in item):
            item = item.replace("user.notice root: power supply error: switching to backup power", "Переход на резервное питание")
        if ("main supply restored" in item):
            item = item.replace("user.notice root: power supply error: main supply restored", "Переход на основное питание")
        if ("Password auth succeeded for 'root' from" in item):
            item = item.replace("Password auth succeeded for 'root' from", "Подключение пользователя как root с ip:")
        if ("authpriv.notice dropbear" in item):
            item = item.replace("authpriv.notice dropbear", "")    
        w_sibur.write(n7, 3, item, style1)
        n7 += 1
    import os
    print("lox", os.getcwd())
    wb.save('/home/pluto/file/teleofismonitor/blogengine/static/files/telemonitor.xls')



