import mysql.connector
from mysql.connector import Error

host_name = " mysql.j1007852.myjino.ru"
user_name = "j1007852"
user_password = "qhKQ9wrT23"
db = "j1007852_maif"

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host=host_name, user=user_name, database=db, password=user_password)
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)



conn = connect()
cursor = conn.cursor()

fil ="SELECT * FROM  `tbl_eat_for_simplex`  WHERE  `id`= 2"
cursor.execute(fil)
result = cursor.fetchall()
print(result)
