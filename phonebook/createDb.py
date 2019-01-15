import sqlite3

connect = sqlite3.connect('dbase1')                                 # подключение к БД или создание новой
cursor = connect.cursor()                                           # курсор для создания SQL-инструкций
tblcmd = 'CREATE TABLE contacts (name char(30),  phone int(12))'    # SQL-инструкция: Создание таблицы в БД
cursor.execute(tblcmd)                                              # применение SQL-инструкции
connect.commit()                                                    # сохранение изменений в базе данных
connect.close()                                                     # заркыть соедение с БД




