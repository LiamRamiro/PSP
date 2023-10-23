class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
        pass
    def get_titular(self):
        return getattr(self, 'titular')
    
    def set_titular(self, titular):
        return setattr(self, 'titular', titular)
    
    def get_cantidad(self):
        return getattr(self, 'cantidad')
    
    def set_cantidad(self, cantidad):
        return setattr(self, 'cantidad', cantidad)
    
    def to_string(self):
        return str(self)
    
    def ingresar(self, ingreso):
        if ingreso >= 0:
            self.set_cantidad(self.get_cantidad() + ingreso)
    
    def retirar(self, retirada):
        if retirada < 0:
            return False
        if self.get_cantidad() - retirada <= 0:
            self.set_cantidad(0)
        else:
            self.set_cantidad(self.get_cantidad()-retirada)
        return True

cuenta1 = Cuenta('Liam')
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.ingresar(-1000)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.ingresar(1000)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.retirar(100)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.retirar(1000)
print(cuenta1.get_titular(), cuenta1.get_cantidad())

cuenta1 = Cuenta('Liam',1000)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.ingresar(-1000)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.ingresar(1000)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.retirar(100)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.retirar(1000)
print(cuenta1.get_titular(), cuenta1.get_cantidad())