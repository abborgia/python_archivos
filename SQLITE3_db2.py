import sqlite3
print(sqlite3.version)

print(sqlite3.sqlite_version)

conn = sqlite3.connect("5\db.sqlite3")
c = conn.cursor()

c.execute("select * from clientes")
clientes = c.fetchall()
for clientes in clientes:
    print(clientes)