# Métodos Accesores (GET - SET) En Python | Curso Python 3 🐍 # 33
# Fuente: https://www.youtube.com/watch?v=6xoo1Ya_uQ0

class Cuenta:
    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    # Getters (métodos GET) --> Nos permiten obtener un valor
    def get_propietario(self):
        return self.__propietario
    def get_saldo(self):
        return self.__saldo
    def get_moneda(self):
        return self.__moneda
    
    # Setters [métodos SET)--> Nos permiten cambiar un valor
    def set_moneda(self, moneda):
        self.__moneda = moneda

# Programa principal
cuenta1 = Cuenta("Juan Pérez",2500,"$AR")
print(cuenta1.get_propietario())
print(cuenta1.get_moneda()) #Antes del cambio, se puso al momento de instanciar el objeto
cuenta1.set_moneda("Dólares")
print(cuenta1.get_moneda()) #Posterior al cambio
