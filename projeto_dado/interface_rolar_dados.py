from tkinter import *
from tkinter import ttk
import projeto_dado.rolar_dados as rolar_dados


interface = Tk()
interface.title("Rolagem de dados")
interface.geometry("700x400")
interface.wm_maxsize(width = 1000,height=500)




def rolar():
    #leitura dos valores em tkinter
    quantidade = int(entrada_qtd.get())
    lados = int(combo_dado.get())

    resultados = rolar_dados.rola_dado(quantidade, lados)

    resultado_texto.delete("1.0", END)
    #mostra resultados aos usuários
    for valor in resultados:
        resultado_texto.insert(END, f"Rolagem: {valor}\n")

    if rolar_dados.contador_rolagens % 20 == 0:
        resultado_texto.insert(END, "\nEstatísticas:\n")
        resultado_texto.insert(END, str(rolar_dados.estatisticas()))


#Cria entrada para inserir dados
Label(interface, text="Quantidade de dados").pack()

entrada_qtd = Entry(interface)
entrada_qtd.pack()

Label(interface, text="Tipo de dado").pack()

combo_dado = ttk.Combobox(interface)
combo_dado["values"] = (4,6,8,10,12,20,100)
combo_dado.pack()

#Botao de rolagem
Button(interface, text="Rolar", command=rolar).pack()

#Exposição do resultado
resultado_texto = Text(interface, height=10)
resultado_texto.pack()

interface.mainloop()