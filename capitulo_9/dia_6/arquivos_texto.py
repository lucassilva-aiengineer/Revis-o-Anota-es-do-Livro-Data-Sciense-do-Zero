from faker import Faker


def acessando_arquivos_texto():

    def txt_escrita():
        faker = Faker('pt_BR')

        nomes = [faker.name() for _ in range(100)]
        with open('capitulo_9\\dia_6\\arquivos.txt', 'w', encoding= 'utf-8') as arquivo: 

            for nome in nomes:
                arquivo.write(f"{nome}\n")


    # txt_escrita() 

    def txt_leitura():

        """
            Lendo um arquivo.
        """
acessando_arquivos_texto()