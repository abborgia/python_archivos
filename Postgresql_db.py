import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="prueba1",
    user="postgres",
    password="1582")

c = conn.cursor()
c.execute("select * from alumnos")

alumnos = c.fetchall()
for alumnos in alumnos:
    print(alumnos)

