def main():

    # with open("capitulo_9/dia_3/tentativa_b/produtos.txt", 'w') as arquivo:
# "/capitulo_9/dia_3/tentativa_b"

    arquivo = open("produtos.txt", "w")

    for nome in ["Mateus", "Marcos"]:
        arquivo.write(f"{nome}\n")

    arquivo.close()

if __name__ == '__main__':
    main()