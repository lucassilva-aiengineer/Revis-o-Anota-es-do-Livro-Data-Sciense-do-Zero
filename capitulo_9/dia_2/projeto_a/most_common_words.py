from collections import Counter
import sys  

# ENCONTRANDO AS PALAVRAS MAIS COMUNS 


try: 

    # A quantidade de linhas
    numero_palavras = int(sys.argv[1])

except:
    print("Utilize: most_common.py indique_numero_palavras")
    sys.exit(1) # Efetua o fim prematuro da execução. 


counter =   Counter(palavra.lower() for linha in sys.stdin 
                                    for palavra in linha.strip().split()
                                    if palavra) # A palavra não pode ser um espaço. 

def imprimir():
    for palavra in counter:

        print(f"""palavra: {palavra}
    contagem: {counter[palavra]}""")


def ordenando():

    return sorted(counter.items(), 
                    key= lambda tupla: tupla[1], 
                    reverse= True)



def teste():

    dados_ordenados = ordenando() 

    for palavra, contagem in dados_ordenados[: 5]:
        print(f"""Palavra: {palavra}
Contagem: {contagem}""")


# teste() 

for palavra, contagem in counter.most_common(numero_palavras):
    sys.stdout.write(str(contagem))
    sys.stdout.write("\t")
    sys.stdout.write(palavra)
    sys.stdout.write("\n")

