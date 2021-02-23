import psycopg2

connec = psycopg2.connect(
    host="localhost",
    database="prueba1",
    user="postgres",
    password="1582")

c = connec.cursor()
c.execute("select * from alumnos")

alumnos = c.fetchall()
for alumnos in alumnos:
    print(alumnos)

