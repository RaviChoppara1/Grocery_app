import mysql.connector

__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Sanvi@2016',
                                  host='127.0.0.1',
                                  database='grocery_store')

    return __cnx