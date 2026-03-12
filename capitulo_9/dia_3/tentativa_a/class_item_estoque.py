# Criando uma arquivo que acumula dados, algo como um estoque 
# de mercado ou uma planilha de compras. 

class ItemEstoque: 

    def __init__(self, nome: str= "", quantidade: int= 0):

        self.__nome = nome 
        self.__quantidade = quantidade 


    @property 
    def nome(self)-> str:
        return self.__nome 

    @property 
    def quantidade(self)-> int:
        return self.__quantidade 

    @nome.setter 
    def nome(self, nv_nome: str)-> None:
        self.__nome = nv_nome 

    @quantidade.setter 
    def quantidade(self, nv_quantidade: int)-> None:
        self.__quantidade = nv_quantidade 


def main():


    """
        Testando a criação do objeto 
    """

    item = ItemEstoque('Arroz', 10)
    print(item.quantidade)

    item.quantidade = 5 

    print(item.quantidade)

if __name__ == '__main__':
    main()