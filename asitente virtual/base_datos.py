from multiprocessing import connection
import sqlite3

def create_connection():
    connection = sqlite3.connect("cerebro.db")
    return connection

def get_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM preguntas_y_respuestas")
    return cursor.fetchall()


bot_list = list()
def get_preguntas_y_respuestas():
    rows = get_table()
    for row in rows:
        bot_list.extend(list(row))
    return bot_list