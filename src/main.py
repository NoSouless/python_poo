from frota import *

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

if __name__ == "__main__":

    kms = 0

    print('Cadastre o 1º carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    #kms = float(input('Digite com quantos Kms: '))


    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor = False)

    print('Cadastre o 2º carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    carro2 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor=False)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600:
        try:
            op = 0
            while op not in (1, 2, 3):
                op = int(input('Qual carro? [1-2] '))

            operar_carro(carro1 if op == 1 else carro2)

            print('Infos atuais dos carros')
            print(carro1)
            print(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    if carro1.motor_on == True:
        carro1.desligar()
    if carro2.motor_on == True:
        carro2.desligar()
    print(carro1)
    print(carro2)

    print("O carro" + ('1' if carro1.odometro >= 600 else '2') + ' chegou ao destino primeiro')
