class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro : 0.0
    __motor_on : False
    __tanque: float
    consumo_medio: float


    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque: float,
                            consumo: float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor
        self.__tanque = tanque
        self.consumo_medio = consumo

    def ligar(self):
        if not self.__motor_on and self.__tanque > 0:
            self.__motor_on = True
        elif self.__motor_on:
            raise Exception("Erro: Motor já ligado!")
        else:
            raise Exception("Erro: Sem Gasolina!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on and self.__tanque > 0:
            km = velocidade * tempo
            litros = km/self.consumo_medio

            if self.__tanque >= litros:
                self.__tanque = litros
            else:
                km = self.__tanque * self.consumo_medio
                self.__tanque = 0
                self.__motor_on = False
            self.__odometro += km
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}\n'
                f'tanque {self.__tanque}, consumo {self.consumo_medio}'
                )
        return info

    def getTanque(self):
        return self.__tanque

    def getOdometro(self):
        return self.__odometro

    def getMotor(self):
        return self.__motor_on

'''
    def __repr__(self):
        return (f'Carro (modelo="{self.modelo}", marca="{self.marca}", '
                f'cor="{self.cor}", odometro={self.__odometro}',
                f'motor_on={self.__motor_on})'
                )
'''





