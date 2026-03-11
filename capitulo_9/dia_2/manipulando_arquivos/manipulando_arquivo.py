from faker import Faker
import random 
from typing import List 
# Criando e manipulando arquivos. 

def criar_arquivo_pessoas(file_name: str, pessoas_criar: int= 0)-> None:

    # pessoas_criar = input 

    faker = Faker('pt_BR')

    # dessa forma eu abro o arquivo apenas uma vez, permitindo 
    # uma criação do arquivo sem destruição. 


    with open(file_name, 'w') as arquivo: # Criando um arquivo caso não exista


        pessoas_criadas = 0
        while pessoas_criadas < pessoas_criar:


            nome = faker.name()
            idade = random.randint(20, 80)
            bairro = faker.address()
            email = faker.email()
            telefone = faker.phone_number()


            pessoa_formatada = f"{nome}, {idade}, {bairro}, {email}, {telefone}\n"

            arquivo.write(pessoa_formatada)

            pessoas_criadas += 1

def main():

    # Alguns testes 
    # faker = Faker('pt_BR')

    # print(faker.name())

    
    criar_arquivo_pessoas("clientes.csv", 10)

if __name__ == '__main__':
    main()