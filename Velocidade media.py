#O programa deve calcular a vm de um veículo.
#Velocidade média = distância final - distancia inicial/tempo final - tempo inicial

print("-------------------Início da execução-------------------")

def velocidadeMedia (distFinal, distInicial, tempoFinal, tempoInicial):
    return (distFinal - distInicial)/(tempoFinal - tempoInicial)
dF = float(input("Insira a Distância final do veículo: "))
dI = float(input("Insira a Distância inicial do veículo: "))
tF = float(input("Insira o tempo final do veículo: "))
tI = float(input("Insira o tempo inicial do veículo: "))

print("A sua velocidade média foi: ", velocidadeMedia(dF, dI, tF, tI))
print("-------------------Final da execução-------------------")