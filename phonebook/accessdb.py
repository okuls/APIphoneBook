import sqlite3


# Поиск контакта в БД.
def find_contact(name):
    connect = sqlite3.connect('dbase1')                     # подключение к базе данных
    cursor = connect.cursor()                               # курсор для создания SQL-инструкций
    query = "SELECT * FROM contacts WHERE name = ? "        # SQL-инструкция (запрос)
    cursor.execute(query, [name])                           # выполнение SQL-инструкции
    colnames = [desc[0] for desc in cursor.description]     # извлечение названий полей(столбцов) таблицы
    rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]  # объедение полей и строк в словарь
    connect.close()                                         # заркыть соедение с БД
    if rowdicts:
        return rowdicts[0]                                  # вернуть найденный контакт
    else:
        return {}                                           # или пустой словарь


# Добавление контакта в БД.
def add_contact(name, phone):
    connect = sqlite3.connect('dbase1')                     # подключение к базе данных
    cursor = connect.cursor()                               # курсор для создания SQL-инструкций
    query = "INSERT INTO contacts values (?, ?)"            # SQL-инструкция (запрос)
    cursor.execute(query, (name, phone))                    # выполнение SQL-инструкции
    connect.commit()                                        # сохранение изменений в базе данных
    connect.close()                                         # заркыть соедение с БД
    message = "Контакт успешно добавлен!"                   # хорошая новость
    return message                                          # вернуть сообщение
