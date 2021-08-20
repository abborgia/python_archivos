import sys
import socket


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print('El nombre de tu ordenador es {}'.format(hostname))
print('Tu IP es {}'.format(ip))


listaPuertos = []

#objetivo = socket.gethostbyname(input('Inserte la direccion IP: '))
objetivo = socket.gethostbyname(ip)

print('Escaneando el Objetivo: {}'.format(objetivo))

#try:
for port in range(1,500):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    resutado = s.connect_ex((objetivo,port))
    print('\nEscanendo puerto: {}.......'.format(port))
    if resutado == 0:
        print('El puerto {} esta abierto'.format(port))
        listaPuertos.append(port)
    else:
        print('puerto {} cerrado'.format(port))
    s.close()

cantidad = str(len(listaPuertos))
print("""\n 
------------------------------------------------------------------
La cantidad de puertos abiertos son: {}

""".format(cantidad))
input("Press enter to list open ports. . . . \n")
for openPort in listaPuertos:
    print('Puerto {} abierto'.format(openPort))
print('\n')
#except:
 #   print('\n saliendo...')
 #   sys.exit(0)