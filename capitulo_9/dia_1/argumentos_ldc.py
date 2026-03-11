import sys 
from typing import List, Union, Optional 
import time

# Dia 1.


# Recebendo argumentos na linha de comando. 



# lista_argumentos = sys.argv


def dizer_oi(lista_argumentos: List[str]):

    # nome = lista_argumentos[1]
    return f"Oi, {lista_argumentos[1]}!"


def adicionar_nomes():

    lista_nomes = sys.argv 

    with open("capitulo_9/lista_nomes_a.txt", "a") as file:
        for nome in lista_nomes[1:]: 
            file.write(f"{nome}\n")



def main():


    def main_a():
        try:
            argumentos = sys.argv 
            print(dizer_oi(argumentos))

        except IndexError as message: 
            print(message)
            time.sleep(1)
            print("E necessário indicar ao menos um nome!")


        else:
            print("Código executado com sucesso...") 
            time.sleep(1) 

        finally: 
            print("Iteração concluída!")
            time.sleep(1)

    adicionar_nomes()


if __name__ == '__main__':
    main()