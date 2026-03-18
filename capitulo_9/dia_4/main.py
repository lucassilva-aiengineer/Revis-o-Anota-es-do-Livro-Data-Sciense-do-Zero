import csv
from class_funcionario import Funcionario
from typing import List
import time 



def criar_arquivo(csv_nome)-> None:

    """
        Varificamos se o arquivo existe caso contrário 
        criamos um, e retornamos um arquivo ao fim da veri
        ficação.

    """
    try:
        arquivo = open(csv_nome, 'r')

    except FileNotFoundError as message:
        print(message)

        print("Criando arquivo...")
        time.sleep(2)

        arquivo = open("capitulo_9\\dia_4\\lista_funcionarios.txt", 'w')
        print("Arquivo criado...")
        time.sleep(2)


    # Retornamos o arquivo criado ou o arquivo que apenas abrimos. 
    # return arquivo 

    # Com a execução desta função teremos certeza da existencia
    # de um arquivo. 

def adicionar_funcionarios(csv_nome, pessoas)-> None:

    """
        Vamos colher alguns nome e adicionar ao arquivo. 
    """ 

    with open(csv_nome, 'a') as arquivo: 
        csv_write = csv.writer(arquivo, delimiter= ',')
        for pessoa in pessoas: 
            csv_write.writerow([pessoa.nome, pessoa.idade, f"{pessoa.salario}\n"])


    print("Pessoas adicionados com sucesso!")
    time.sleep(2)


def ler_csv(csv_nome)-> None:

    with open(csv_nome, 'r') as arquivo:
        # primeiro leremos como um csv normal depois como dicionário 
        # reader_csv = csv.DictReader(arquivo, delimiter= '')

        reader = csv.reader(arquivo)

        for valor in list(reader):
            # nome = row[0]
            # idade = row[1]
            # salario = row[2]

            # print(f"Nome: {valor[0]} Idade: {valor[1]} Salario: {valor[2]}")

            print(valor)

def main():

    NOME_ARQUIVO = "capitulo_9\\dia_4\\lista_funcionarios.txt"
    criar_arquivo(NOME_ARQUIVO)

    print("By Lucas Silva.")
    time.sleep(1)

    print("\n")
    time.sleep(0.4)

    print("\n")
    time.sleep(0.4)

    print("\n")
    time.sleep(0.4)




    print("Bem vindo ao administrador de RH!")
    time.sleep(1)

    while True:

        print("Para adicionar pessoas digite 1.")
        print("Para ver as pessoas existentes digite 2.")
        print("Para encerrar operação digite 3.")

        opcao = int(input("Indique a sua opção: "))

        if opcao == 1:

            funcionarios: List[Funcionario] = []

            nome = input("Indique o nome deste funcionário: ")
            idade = int(input("Indique a idade deste funcionário: "))
            salario = float(input("Indique o salário deste funcionário: "))

            funcionario = Funcionario(nome, idade, salario)
            funcionarios.append(funcionario)

            adicionar_funcionarios(NOME_ARQUIVO, funcionarios)

        elif opcao == 2:
            ler_csv(NOME_ARQUIVO)

        elif opcao == 3:

            print("Saindo...")
            time.sleep(1)

            break 

        else:

            print("Opção inválida!")
            time.sleep(1)

            print("Tentando novamente...")
            time.sleep(1)


if __name__ == '__main__':
    main()

