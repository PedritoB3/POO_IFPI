class aplicativo_jogo:
    nome = None #nome do jogo
    status = False #aberto ou fechado
    internet = False #Ligado ou desligado
    player = None #Se é online ou offline
    

    def status_jogo(self):
        if (self.status):
            print(f"O {self.nome} está aberto")
        else:
            print(f"O {self.nome} está fechado")

    def internet_dispositivo(self):
        if (self.status):
            if (self.internet):
                print(f"A internet está ligada")
            else:
                print(f"A internet está desligada")

    def player_jogo(self):
        if (self.status):
            if self.player == "Online":
                if self.internet:
                    print("Se tem internet e o jogo é online, pode jogar")
                else:
                    print("Se não tem internet e o jogo é online, não pode jogar")
            if self.player == "Offline":
                if self.internet:
                    print("Se tem internet e o jogo é offline, pode jogar")
                else:
                    print("Se não tem internet e o jogo é offline, pode jogar, não precisa de internet mesmo")




meu_jogo = aplicativo_jogo()

meu_jogo.nome = "Fightcade"
meu_jogo.status = True
meu_jogo.internet = False
meu_jogo.player = "Offline"


meu_jogo.status_jogo()
meu_jogo.internet_dispositivo()
meu_jogo.player_jogo()