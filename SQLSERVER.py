import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
#-------
server = 'DESKTOP-5R0RQPB' 
database = 'PythonDB' 
username = 'sa' 
password = '1582' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

sql="create table usuarios2 (id int not null primary key, nombre varchar(50), apellido varchar(50), correo varchar(50));"
#cursor.execute(sql)

if cursor.execute(sql): print("ok")
else: print("Error")

info=cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
detalle=cursor.fetchall()
for detalle in detalle:
    print(detalle)

cnxn.commit()
cnxn.close()