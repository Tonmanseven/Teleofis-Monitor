import subprocess
import os
import datetime, time
# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('routers.sqlite3')
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()
id_now = 1
while True:

 ####################################### Опора 3 №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

    ############### Mark 1 ###########

    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark1_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:

        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [50]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark1_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark1_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    
    # ############### Mark 2 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark2_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [42]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark2_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark2_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    # ############### Mark 9 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark9_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [62]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark9_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark9_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()


    ####################################### Опора 2 №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
    
    ############### Mark 3 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark3_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [22]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark3_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark3_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    
    # ############### Mark 4 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark4_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [34]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark4_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark4_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    # ############### Mark 5 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark5_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [26]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark5_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark5_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()    

    ####################################### Опора 1 №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
    
    ############### Mark 6 ###########
    
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark6_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [30]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark6_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark6_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    
    # ############### Mark 7 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark7_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [46]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark7_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark7_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()

    # ############### Mark 8 ###########
    # Открываем таблицу, если ее нет то Создаем таблицу
    cursor.execute('CREATE TABLE IF NOT EXISTS mark8_state(State INTEGER , Time timestamp, '
                   'id INTEGER, date timestamp )')

    with open(os.devnull, "wb") as limbo:
        now = datetime.datetime.now()
        wonow = now.strftime("%H.%M")
        date_now = now.strftime("%Y.%m.%d")

        ping_yes = [1, wonow, id_now, date_now]
        ping_no = [0, wonow, id_now, date_now]

        num = [38]
        for n in num:
            
            ip = "10.8.0.{}".format(n)
            result = subprocess.Popen(["ping", "-c", "1", "-t", "2", "-W", "4", ip], stdout=subprocess.PIPE).wait()
            if result:
                cursor.execute('INSERT INTO mark8_state VALUES(?, ?, ?, ?)', ping_no)
            else:
                cursor.execute('INSERT INTO mark8_state VALUES(?, ?, ?, ?)', ping_yes)
    
        conn.commit()
    id_now += 1
    # частота обновлений данных (раз в 15 min)
    time.sleep(1800)

