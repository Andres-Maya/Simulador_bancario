__author__ = "Andrés Camilo Maya Rosero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "andres.mayar@campusucc.edu.co"

class CuentaCorriente: 
    # Aqui inicia la declaracion de la clase

    '''#-------------------------------------
    # Atributos
    -----------------------------------------#'''

    __monto = 0
    __saldo = 0

    #----------------------------------------
    #Metodos
    #-----------------------------------------

    __method__ = "ConsignarValor"
    __params__ = "Monto"
    __returns__ = "Nada"
    __description__ = "Permite consignar un monto a la cuenta"

    def ConsignarValor(self, monto):
        self.__saldo = self.__saldo + monto

    __method__ = "DarSaldo"
    __params__ = "Ninguno"
    __returns__ = "Saldo"
    __description__ = "Este metodo retorna el saldo"

    def DarSaldo(self):
        return self.__saldo
    
    __method__ = "RetirarValor"
    __params__ = "Monto"
    __returns__ = "Nada"
    __description__ = "Este metodo retira un monto a la cuenta"

    def RetirarValor(self, monto):
        self.__saldo = self.__saldo - monto