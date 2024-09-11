__author__ = "Andrés Camilo Maya Rosero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "andres.mayar@campusucc.edu.co"

class CDT: 
    # Aqui inicia la declaracion de la clase

    '''#-------------------------------------
    # Atributos
    -----------------------------------------#'''

    inversion = 0
    intereses = 0
    fecha_Apertura = 00/00/0000

    __method__ = "ConsignarValor"
    __params__ = "ValorConsignacion"
    __returns__ = "Nada"
    __description__ = "Permite al empleado consignar un valor de su salario"

    def ConsignarValor(self, ValorConsignacion):
        #Aqui inicia mi metodo
        self.saldo = self.saldo-ValorConsignacion