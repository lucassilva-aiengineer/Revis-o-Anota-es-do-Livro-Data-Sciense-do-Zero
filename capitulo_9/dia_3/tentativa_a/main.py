from typing import List, Union, Dict
import time 



def menu(): 

    NOME_ARQUIVO = "capitulo_9\\dia_3\\tentativa_a\\estoque_produtos.txt"

    produtos: List[Dict[str, Union[str, int]]] = []

    print("Bem vindo ao estoque do Supermecado.\n")

    while True:

        print("Para adicionar produtos digite 1.")
        print("Para ver o estoque digite 2.")
        print("Para acessar os produtos em falta digite 3.")
        print("Para sair digite 4.")

        opcao = int(input("Indique a sua opção: "))

        if opcao == 1:
            print("Adicionando produtos...")
            time.sleep(2)

            nome = input("Indique o nome do produto: ")
            quantidade = int(input("Indique a quantidade adicionada: "))

            produto =  {"nome": nome, 
                        "quantidade": quantidade}

            produtos.append(produto)

            print("Produto adicionado com sucesso.")
            time.sleep(2)


        elif opcao == 2: 
            print("Vendo estoque...")
            time.sleep(2)

            exibir_produtos(NOME_ARQUIVO)

        elif opcao == 3:

            pass 

        elif opcao == 4:
            print("Saindo...")
            time.sleep(2)

            adicionar_produtos(NOME_ARQUIVO, produtos)
            print("Produtos salvos...")
            time.sleep(2)

            break


def adicionar_produtos(nome_arquivo, produtos):


    with open(nome_arquivo, 'a') as arquivo:

        for produto in produtos:
            arquivo.write(f"{produtos["nome"]}, {produtos["quantidade"]}\n")


def exibir_produtos(nome_arquivo):

    produtos: List[Dict[str, Union[str, int]]] = []

    with open(nome_arquivo, 'r') as arquivo:

        for linha in arquivo:
            linha = linha.replace("\n")
            lista_palavras = linha.split(",")

            produto = {"nome": lista_palavras[0], "quantidade": float(lista_palavras[1])}
            produtos.append(produto)

    for produtos in produtos:
        print(f"Nome: {produtos["nome"]} Qntd: {produtos["quantidade"]}")


def main():

    # try: 
    #     arquivo = open("capitulo_9\\dia_3\\estoque_produtos.txt")

    # except FileNotFoundError as message:
    #     print(message)

    #     # Criando arquivo. 
    #     arquivo = open("capitulo_9\\dia_3\\estoque_produtos.txt", "w") 
    #     arquivo.close()

    menu()

    






if __name__ == '__main__':
    main()