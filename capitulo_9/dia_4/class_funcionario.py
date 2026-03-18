

class Funcionario:

    def __init__(self, nome: str= "", idade: int= 0, salario: float= 10000):

        self.__nome = nome 
        self.__idade = idade 
        self.__salario = salario 


    @property 
    def nome(self)-> str:
        return self.__nome 


    @property 
    def idade(self)-> int:
        return self.__idade 


    @property 
    def salario(self)-> float:
        return self.__salario 


    # Definindo os nossos setters 

    @nome.setter 
    def nome(self, nv_nome: str)-> None:
        self.__nome = nv_nome

    @idade.setter 
    def idade(self, nv_idade: int)-> None:
        self.__idade = nv_idade 

    @salario.setter 
    def salario(self, nv_salario: float)-> None:
        self.__salario = nv_salario


    def __repr__(self)-> str:
        return f"Nome: {self.__nome} Salário: {self.__salario}"



def main():
    pass 

if __name__ == '__main__':
    main()