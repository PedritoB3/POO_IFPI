#2. Melhore a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual, altura_cela e
#calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela e calibrar_pneus para
#permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0). Execução: Criar pelo menos 2 objetos,
#imprimir seus estados iniciais, executar os métodos e imprimir seus estados finais.
class bicicleta:
    def __init__(self,peso,altura,veloc_atual,veloc_max,cor,aro,altura_cela,altura_cela_max,calibragem_pneus,calibragem_max):
        self.peso = peso
        self.altura_bicicleta = altura
        self.veloc_atual = veloc_atual
        self.veloc_max = veloc_max
        self.cor = cor
        self.aro = aro
        self.altura_cela = altura_cela
        self.altura_cela_max = altura_cela_max
        self.calibragem_pneus = calibragem_pneus
        self.calibragem_max = calibragem_max

    def pedalar(self):

        print(f"A sua velocidade atual é de {self.veloc_atual} km, deseja aumentar ou diminiuir, ou não?")
        resposta = input()
        if resposta == "aumentar":
            self.veloc_atual += int(input("Digite a velocidade: "))

        elif resposta == "diminuir":
            self.veloc_atual -= int(input("Digite a velocidade"))

        elif resposta == "não":
            pass

        if self.veloc_atual == 0 :
            print("Você está parado")

        elif self.veloc_atual < self.veloc_max:
            print("Sua velocidade atual está normal")

        elif self.veloc_atual >= self.veloc_max:
            print("Sua velocidade está acima da velocidade maxima!!!")


    def frear(self):
        if self.veloc_atual <= 0:
            print("Mas voce já está parado, para que frear.")

        else:
            print(f"Sua velocidade é de {self.veloc_atual},você deseja frear? sim ou não")
            resposta = input()


            if resposta == "sim":
                self.veloc_atual -= int(input("Digite o quanto voce quer frear: "))
                print(f"Agora sua velocidade é de {self.veloc_atual} km")
            elif resposta == "não":
                pass

    def regular_cela(self):
        if self.veloc_atual <= 0:
            print("Deseja regular sua cela? sim ou não")
            resposta = input()

            if resposta == "sim":
                self.altura_cela = int(input("Regule a cela: "))
            elif resposta == "Não":
                pass

            if self.altura_cela <= self.altura_cela_max:
                print("Altura da cela regulada dentro dos limites")
            elif self.altura_cela > self.altura_cela_max:
                print("Altura da cela está acima dos limites")


        if self.veloc_atual > 0:
            print("Voce está em movimento, não é possivel regular")

    def calibrar_pneus(self):
        if self.veloc_atual <= 0:
            print("Deseja calibrar os seus pneus? sim ou não")
            resposta = input()

            if resposta == "sim":
                self.calibragem_pneus = int(input("Calibre os penus: "))

            elif resposta == "Não":
                pass

            if self.calibragem_pneus <= self.calibragem_max:
                print("Pneus calibrados dentro dos limetes")
            elif self.calibragem_pneus > self.calibragem_max:
                print("Pneus calibrados dentro dos limites")


        if self.veloc_atual > 0:
            print("Voce está em movimento, não é possivel calibrar")

print("BICICLETA 1:")
Bicicleta1 = bicicleta(13,110,0,100,"preta",26,5,10,20,50)
Bicicleta1.pedalar()
Bicicleta1.frear()
Bicicleta1.regular_cela()
Bicicleta1.calibrar_pneus()

print("BICICLETA 2:")
Bicicleta2 = bicicleta(20,130,30,120,"branca",30,7,15,30,60)
Bicicleta2.pedalar()
Bicicleta2.frear()
Bicicleta2.regular_cela()
Bicicleta2.calibrar_pneus()