import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

sg.theme("Dark Green 3")

layout = [
    [sg.Text("Carrinho", justification='center', expand_x=True)],
    [sg.Text(key="linha_1", size=(50, 4), background_color="White", text_color = "Black"), sg.Button("Deletar", key="Deletar_1")],
    [sg.Text(key="linha_2", size=(50, 4), background_color="White", text_color = "Black"), sg.Button("Deletar", key="Deletar_2")],
    [sg.Text(key="linha_3", size=(50, 4), background_color="White", text_color = "Black"), sg.Button("Deletar", key="Deletar_3")],
    [sg.Text(key="linha_4", size=(50, 4), background_color="White", text_color = "Black"), sg.Button("Deletar", key="Deletar_4")],
    [sg.Text("Valor Total:", size=(10, 1)), sg.Text("0", key="total"), sg.Text("R$")],
    [sg.Text("Quantidade de itens:", size=(18, 1)), sg.Text("0", key="total de produtos", size=(30, 1))],
    [sg.Button("Página anterior"),sg.Text("Página:"), sg.Text("1", key="pagina"), sg.Button("Próxima Página")],
    [sg.Text()],
    [sg.Text("Inserir Produto")],
    [sg.Text("Nome do produto:", size=(15, 1)), sg.Input(key="Produto")],
    [sg.Text("Valor do produto:", size=(15, 1)), sg.Input(key="Valor")],
    [sg.Text("Quantidade do produto:"), sg.Button("-"), sg.Input(key="Quantidade", size=(10, 1), justification='center', default_text="1"), sg.Button("+")],
    [sg.Text(key="feedback")],
    [sg.Button("Adicionar item")],
    [sg.Text()]
]


##################################################################




class Carrinho:
    #Fiz aqui uma lista para que adicione nele os produtos com seus
    #respectivos valores, para serem usados no código como uma espécie 
    #de "Banco de dados".
    lista_de_compras = []


    #Essa função checa se os valores não foram preenchidos, e tira qualquer
    #espaço que o usuário possa ter deixado.
    def checar_valor_preenchido(self, nome, valor, quantidade):
        
        valor = valor.replace(" ", "")
        quantidade = quantidade.replace(" ", "")

        if valor == "" or quantidade == "" or nome == "":
            return False
        
        elif valor == "0" or quantidade == "0":
            return False
        else:
            return True



    #Essa função converte o valor e a quantidade de string para números (int e float)
    #Caso não há como converter, ou seja, está inserido errado, ele retorna False.
    #Também retorna False se os valores são nulos.
    def conversor_de_valores(self, nome, valor, quantidade):

        valor_conv = valor.replace("," , ".")
        try:
            valor_conv = round(float(valor_conv), 2)
            quantidade_conv = int(quantidade)

            if valor_conv <= 0.0 or quantidade_conv <= 0:
                return False

            valores = nome, valor_conv, quantidade_conv

            return valores
        except:
            return False



    #Fiz essa função para a conversão apenas da quantidade, já que será usada essa
    #conversão para aumentar ou diminuir a quantidade
    def conversor_de_quantidade(self, quantidade):
        quantidade = quantidade.replace(" ", "")

        
        try:
            quantidade_conv = int(quantidade)

            return quantidade_conv
        except:
            return False



    #Fiz essa função curta que adiciona os valores do produto no dictionare.
    #Observação: deve usar o conversor e o checador primeiro.
    def adicionar_item(self, valores):
        self.lista_de_compras.append(valores)


    #Essa função eu fiz pensando a longo prazo.
    #Ela remove o que quer da lista, e se não haver o que remover,
    #Ele retorna False, o que lá na frente eu quero colocar que nada acontece.
    #Caso exista, retorna o nome que deletou e quero que exiba lá na frente.
    def remover_item(self, index):
        try:
            existencia = self.lista_de_compras.pop(index)
            return existencia[0]
        except:
            return False
    

    #Essa função retorna o total de valor e o número de produtos
    def total(self):
        total = 0
        total_de_produtos = 0
        for compra in self.lista_de_compras:
            valor = compra[1] * compra[2]
            total += valor

            total_de_produtos += compra[2]


        total = round(total, 2)
        
        
        return total, total_de_produtos



carrinho = Carrinho()  


#######################################################################

    
#Logo abaixo é o programa de iniciar a janela.
window = sg.Window("Carrinho", layout)

#variável para armazenar a página
pagina = 1



#Função que torna visível os itens na tela.
def exibir_lista(pagina):
    index_final = (4 * pagina) - 1
    index_inicial = index_final - 3 

    lista_atual = []

    for index, item in enumerate(carrinho.lista_de_compras):
        if index >= index_inicial and index <= index_final:
            lista_atual.append(item)

        
    try:
        total_1 = round(lista_atual[0][1] * lista_atual[0][2], 2)
        valor_1 = f"""Nome: {lista_atual[0][0]} 
Valor: {lista_atual[0][1]} R$ 
Quantidade: {lista_atual[0][2]}
Total: {total_1} R$"""
        window["linha_1"].update(valor_1)
    except:
        window["linha_1"].update("")

    try:
        total_2 = round(lista_atual[1][1] * lista_atual[1][2], 2)
        valor_2 = f"""Nome: {lista_atual[1][0]} 
Valor: {lista_atual[1][1]} R$
Quantidade: {lista_atual[1][2]}
Total: {total_2} R$"""
        window["linha_2"].update(valor_2)
    except:
        window["linha_2"].update("")

    try:
        total_3 = round(lista_atual[2][1] * lista_atual[2][2], 2)
        valor_3 = f"""Nome: {lista_atual[2][0]} 
Valor: {lista_atual[2][1]} R$ 
Quantidade: {lista_atual[2][2]}
Total: {total_3} R$"""
        window["linha_3"].update(valor_3)
    except:
        window["linha_3"].update("")
        
    try:
        total_4 = round(lista_atual[3][1] * lista_atual[3][2], 2)
        valor_4 = f"""Nome: {lista_atual[3][0]} 
Valor: {lista_atual[3][1]} R$
Quantidade: {lista_atual[3][2]}
Total: {total_4} R$"""
        window["linha_4"].update(valor_4)
    except:
        window["linha_4"].update("")




    
#Função para atualizar os dois totais, tanto de valor quanto de quantidade de produto
def mostrar_total():
    totais = carrinho.total()
    window["total"].update(f"{totais[0]}")
    window["total de produtos"].update(f"{totais[1]}")
        
    
#Função que exclui os itens e impede que você continue em uma página sem nenhum item.
def excluir_item(numero):
    global pagina
    index = (4 * pagina) - numero
    item_removido = carrinho.remover_item(index)
    if not item_removido:
        pass
    else:
        window["feedback"].update(f"O seguinte item foi removido: {item_removido}")
    

    pagina_teste = pagina - 1
    if pagina_teste >= len(carrinho.lista_de_compras) / 4 and pagina_teste >= 1:
        pagina -= 1

##########################################################################3        


while True:
    event, values = window.read()

    if event == WINDOW_CLOSED:
        break


###########################################################################


#Evento que acontece quando se adiciona um item.
    if event == "Adicionar item":
        nome = values["Produto"]
        valor = values["Valor"]
        quantidade = values["Quantidade"]

        valores_completos = carrinho.checar_valor_preenchido(nome, valor, quantidade)
        valores_convertidos = carrinho.conversor_de_valores(nome, valor, quantidade)

        if not valores_completos or not valores_convertidos:
            window["feedback"].update("Valores preenchidos incorretamente.")
        else:
            window["feedback"].update("Produto adicionado")
            carrinho.adicionar_item(valores_convertidos)
            window["Produto"].update("")
            window["Valor"].update("")
            window["Quantidade"].update("1")
        
        


#Evento que acontece quando se pressiona o botão de adicionar quantidade
    if event == "+":
        valor = values["Quantidade"]
        quantidade_convertida = carrinho.conversor_de_quantidade(valor)

        if not quantidade_convertida:
            window["feedback"].update("Não foi possível adicionar quantidade.") 
        else:
            quantidade_convertida += 1
            window["Quantidade"].update(str(quantidade_convertida))
            window["feedback"].update("") 


#Evento que acontece quando se pressiona o botão de diminuir quantidade.
    if event == "-":
        valor = values["Quantidade"]
        quantidade_convertida = carrinho.conversor_de_quantidade(valor)

        if not quantidade_convertida:
            window["feedback"].update("Não foi possível remover quantidade.") 
        elif quantidade_convertida == 1:
            window["feedback"].update("")
            pass 
        else:
            quantidade_convertida -= 1
            window["Quantidade"].update(str(quantidade_convertida))
            window["feedback"].update("") 


#Eventos que acontecem para mudar de página.
    if event == "Próxima Página":
        pagina_teste = ((pagina + 1) * 4) - 3
        quantidade_de_itens = len(carrinho.lista_de_compras)
        
        if quantidade_de_itens < pagina_teste:
            pass
        else:
            pagina += 1

    if event == "Página anterior":
        if pagina < 2:
            pass
        else:
            pagina -= 1
            
            

#O que acontece quando se pressiona deletar.
    
    if event == "Deletar_1":
        excluir_item(4)

    if event == "Deletar_2":
        excluir_item(3)

    if event == "Deletar_3":
        excluir_item(2)

    if event == "Deletar_4":
        excluir_item(1)
    
    mostrar_total()
    exibir_lista(pagina)
    window["pagina"].update(str(pagina))

    #Esse é meu primeiro projeto "grande" e eu estou muito feliz em tê-lo feito.