import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print('El nombre de tu ordenador es {}'.format(hostname))
print('Tu IP es {}'.format(ip))

