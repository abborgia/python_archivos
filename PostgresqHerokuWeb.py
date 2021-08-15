import psycopg2

# CONECTAR A BBDD POSTGRESQL DE HEROKU 



conn = psycopg2.connect(
    host="ec2-34-228-100-83.compute-1.amazonaws.com",
    database="dcrfc06detu7oa",
    user="vamfbppvkdnsjr",
    password="01f83edd3a83d994d62a9c41d8443b4c09c591df551d4560e41316df49d8d247")


#  create a new cursor
cur = conn.cursor()

# execute an SQL statement to get the HerokuPostgres database version
print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchone()
print(db_version)

cur.execute("""SELECT table_schema, table_name
                      FROM information_schema.tables
                      WHERE table_schema != 'pg_catalog'
                      AND table_schema != 'information_schema'
                      AND table_type='BASE TABLE'
                      ORDER BY table_schema, table_name""")

cur.execute("SELECT * FROM prueba.prueba;")

Tablaprueba = cur.fetchall()
for Tablaprueba in Tablaprueba:
    print(Tablaprueba)


cur.execute("SELECT * FROM public.tablaprueba;")


Tablaprueba = cur.fetchall()
for Tablaprueba in Tablaprueba:
    print(Tablaprueba)