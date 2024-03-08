class radio:

    def __init__(self,marca,tipo_radio,estado,sinal, frequencia, volume_atual ):

        self.marca_do_radio = marca

        self.tipo_radio = tipo_radio

        self.estado = estado

        self.conexao = sinal

        self.frequencia = frequencia

        self.volume = volume_atual


    def modelo_radio(self):
        print(f"O seu radio é da marca {self.marca_do_radio}")
    def tipo_de_radio(self):
        if self.tipo_radio == "transmissor":
            print("O seu radio é transmissor. ")
        elif self.tipo_radio == "emissor":
            print("O seu radio é receptor")

    def estado_radio(self):
        if self.estado:
            print("O radio está ligado")
        else:
            print("O radio está desligado, não dá para usar")

    def qualidade_sinal(self):
        if self.estado:
            if self.conexao == "bom":
                print("O sinal está bom, pode usar o radio")
            elif self.conexao == "ruim":
                print("O sinal está ruim, não dá para usar")

    def qual_frequencia(self):
        if self.estado:
            print(f"Seu radio está na frequencia {self.frequencia}")

    def verificador_volume(self):
        if self.estado:
            if self.volume >= 80:
                print("O volume do seu radio está alto")
            elif self.volume < 80:
                print("O volume do seu radio está mediano")
            elif self.volume < 60:
                print("O volume do seu radio está baixo")
            elif self.volume <= 20:
                print("O volume do seu radio está muito baixo")
            elif self.volume == 0:
                print("O volume do radio de está zerado")




meu_radio = radio("Philco","emissor",True,"bom","18khz",70)

print("RADIO 1:")
meu_radio.modelo_radio()
meu_radio.tipo_de_radio()
meu_radio.estado_radio()
meu_radio.qualidade_sinal()
meu_radio.qual_frequencia()
meu_radio.verificador_volume()

meu_radio2 = radio(marca="Motorola",tipo_radio="transmissor",estado= False, sinal="ruim",frequencia= "1khz",volume_atual=50)

print("RADIO 2:")
meu_radio2.modelo_radio()
meu_radio2.tipo_de_radio()
meu_radio2.estado_radio()
meu_radio2.qualidade_sinal()
meu_radio2.qual_frequencia()
meu_radio2.verificador_volume()






