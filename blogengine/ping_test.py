import subprocess
import os
import datetime, time
# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('test.sqlite3')
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()
id_now = 1
while True:

 ####################################### Test №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

    ############### Mark 10 ###########

    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark10_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:

        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [110]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark10_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark10_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    
    # ############### Mark 11 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark11_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [114]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark11_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark11_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    # ############### Mark 12 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark12_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [118]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark12_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark12_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    
    ############### Mark 13 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark13_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [122]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark13_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark13_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    
    # ############### Mark 14 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark14_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [126]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark14_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark14_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    id_now += 1
    # частота обновлений данных (раз в 15 min)
    time.sleep(1800)

