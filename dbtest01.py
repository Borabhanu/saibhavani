import pymysql

db = pymysql.connect(host= 'localhost',
                         user = 'root',
                         password = 'Ramesh@1999',
                         database = 'demo1',
                         cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Data base version : %s" % data)