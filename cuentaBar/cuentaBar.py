class Bar():

    #precio

    menu = {

        'Vino': 3000,
        'Cerveza': 2800,
        'Bebidas 1/2': 1500,
        'Pollo': 4500,
        'Carne': 7500,
        'Ensalada': 2800,
        'Postre': 2400

    }

    def __init__(self):
        self.total = 0
        self.objetos = []

    def add(self, objetos):
        self.objetos.append(objetos)
        self.total += self.menu[objetos]

    def print_factura(self, impuesto,servicio):
        impuesto = (impuesto/100)*self.total  
        servicio = (servicio/100)*self.total  
        total = self.total + impuesto + servicio

        for objeto in self.objetos:
            print(f'{objeto:10}: ${self.menu[objeto]}')
        
        print('\nTotal: {}'.format(self.total))
        print('IVA: {}'.format(impuesto))
        print('Propina: {}'.format(servicio))
        print(f'\n{"Total":10}:${total:.2f}') 


mesa1 = Bar()
mesa1