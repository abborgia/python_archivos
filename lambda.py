def producto(a, b):
    return a * b

print(producto(10,10))

my_lambda = lambda x, y : x*y

print(my_lambda(10,2))

saludo = lambda c : "Hola {}".format(c)

print(saludo("Eduardo"))