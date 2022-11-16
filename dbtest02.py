import pymysql

db = pymysql.connect(host= 'localhost',
                         user = 'root',
                         password = 'Ramesh@1999',
                         database = 'demo2',
                         cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query='INSERT INTO student VALUES("John","Dell",24,"0812CS141028")'
try:

	      cursor.execute(query)
	      db.commit()
except:
	      db.rollback()
db.close()