__author__ = "Andrés Camilo Maya Rosero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "andres.mayar@campusucc.edu.co"

from Cuenta_ahorros import CuentaAhorros 
from Cuenta_corriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario: 
    # Aqui inicia la declaracion de la clase

    '''#-------------------------------------
    # Atributos
    -----------------------------------------#'''

    __nombre = ""
    __cedula = ""

    '''#---------------------------------------------
    Asociacion
    ---------------------------------------------#'''

    __cuentaAhorros = CuentaAhorros()
    __cuentaCorriente = CuentaCorriente()
    __cdt = CDT()

    __mesActual = 0

    #------------------------------------------------
    #Metodo
    #------------------------------------------------

    __method__ = "ConsignarCuentaCorriente"
    __params__ = "Monto"
    __returns__ = "Nada"
    __description__ = "Este metodo permite consignar un monto a la cuenta corriente"

    def ConsignarCuentasCorriente(self, monto):
        #self.__cuentaCorriente.saldo = self.cuentaCorriente.saldo + monto #modo no recomendable
        self.__cuentaCorriente.ConsignarValor(monto)

    __method__ = "CalcularSaldoTotal"
    __params__ = "Ninguno"
    __returns__ = "SaldoTotal"
    __description__ = "Este metodo suma el saldo de todas las cuentas"

    def CalcularSaldoTotal(self):
        #forma1
        total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        return total
    
    __method__ = "PasarAhorrosACorriente"
    __params__ = "Ninguno"
    __returns__ = "Ninguno"
    __description__ = "Este metodo transfiere el saldo de Ahorros a Corriente"

    def PasarAhorrosACorriente(self):
        saldoTemporal = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.ConsignarValor(saldoTemporal)
    
    __method__ = "Ahorrar"
    __params__ = "Ninguno"
    __returns__ = "Ninguno"
    __description__ = "Este metodo transfiere el saldo de Corriente a Ahorros"

    def Ahorrar(self, monto):
        self.__cuentaCorriente.RetirarValor(monto)
        self.__cuentaAhorros.ConsignarValor(monto)

    __method__ = "RetirarAhorro"
    __params__ = "Monto"
    __returns__ = "Nada"
    __description__ = "Retirar valor de la cuenta de ahorros"

    def RetirrarAhorro(self, monto):
        self.__cuentaAhorros.RetirarValor(monto)
        
    __method__ = "DarSaldoCorriente"
    __params__ = "Ninguno"
    __returns__ = "Saldo de la cuenta Corriente"
    __description__ = "Este método retorna el saldo que hay en la cuenta corriente"

    def DarSaldoCorriente(self):
        return self.__cuentaCorriente.DarSaldo()
    
    __method__ = "RetirarTodo"
    __params__ = "Monto"
    __returns__ = "cantidad retirada"
    __description__ = "Este método retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros"

    def RetirarTodo(self):
        total = self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.DarSaldo())
        self.__cuentaCorriente.RetirarValor(self.__cuentaCorriente.DarSaldo())
        return "Usted acaba de retirar " + total
    
    __method__ = "DuplicarAhorro"
    __params__ = "Ninguno"
    __returns__ = "Nada"
    __description__ = "Este método duplica la cantidad de ahorros que hay en la cuenta de ahorros"

    def DuplicarAhorro(self):
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorros.DarSaldo())
