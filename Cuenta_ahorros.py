__author__ = "Andrés Camilo Maya Rosero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "andres.mayar@campusucc.edu.co"

class CuentaAhorros: 
    # Aqui inicia la declaracion de la clase

    '''#-------------------------------------
    # Atributos
    -----------------------------------------#'''

    __saldo = 0
    __intereses = 0

    __method__ = "ConsignarValor"
    __params__ = "ValorConsignacion"
    __returns__ = "Nada"
    __description__ = "Permite al empleado consignar un valor de su salario"

    def ConsignarValor(self, ValorConsignacion):
        #Aqui inicia mi metodo
        self.saldo = self.saldo-ValorConsignacion

    __method__ = "RetirarValor"
    __params__ = "Valor"
    __returns__ = "ValorRetiro"
    __description__ = "Permite al empleado retirar un valor de su salario"

    def RetirarValor(self, Valor):
        #Aqui inicia mi metodo
        self.saldo = self.saldo-Valor

    __method__ = "DarInteres"
    __params__ = "Ninguno"
    __returns__ = "ValorInteres"
    __description__ = "Permite al empleado consultar los intereses"

    def DarInteres(self):
        #Aqui inicia mi metodo