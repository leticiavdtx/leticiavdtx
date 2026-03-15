import random
import pandas as pd

historico = []
contador_rolagens = 0

#Programa que rola vários dados de diferentes lados e gera o contador.
def rola_dado(quantidade, lados):

    global contador_rolagens
    resultado=[]
    for i in range(quantidade):
        valor = random.randint(1, lados)
        resultado.append(valor)
        contador_rolagens += 1

    return resultado

#Exibe as estatísticas para os jogadores
def estatisticas():

    serie = pd.Series(historico)
    return serie.describe()




