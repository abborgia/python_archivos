import pymysql

connection=pymysql.connect(host='localhost',
                            user='root',
                            password='1582',
                            db='users'
                            )

cursor = connection.cursor()

sql = "insert into users (nombre,apellido,correo) values ('Eduardo','serey','abb@abb.com')"

cursor.execute(sql)

connection.commit()
connection.close()