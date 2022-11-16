import pymysql

connection = pymysql.connect(host='localhost',
                         user='root',
                         password='Ramesh@1999',
                         database='demo2',
                         cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
		 sql = "SELECT * FROM student"
		 cursor.execute(sql)
         result=cursor.fetchone()
         print(result)