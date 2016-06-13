arquivo = open('celulares.txt', 'w')
celulares = []
continua = "SIM"
print("# Programa para salvar marcas de celular.#")
print("╔════════════════════════════════╗")
print("║            ᘛMENUᘚ             ║")
print("║                                ║")
print("║          • ADICIONAR           ║")
print("║          • RENOMEAR            ║")
print("║          • DELETAR             ║")
print("║          • LISTAR              ║")
print("║                                ║")
print("║                                ║")
print("║             ZoC ☕             ║")
print("╚════════════════════════════════╝")
                 


while continua != "NÃO":
    comando = input("Qual a sua opção ? \n⌲ A=ADICIONAR \n⌲ R=RENOMEAR \n⌲ D=DELETAR \n⌲ L=LISTAR\n⇢ ")
    if (comando == "A"):
        marca = input("Marca de celular:\n⇢ ")
        celulares.append(marca)
        nomes = ' - '.join(celulares)
        print (nomes)
    elif (comando == "R"):
        antiga_marca = input("Digite a marca do celular que está na lista que deseja atualizar\n⇢ ")
        nova_marca = input("Digite a nova marca do celular\n⇢ ")
        for i,valor in enumerate(celulares):
            if (valor == antiga_marca):
                celulares[i] = nova_marca
        nomes = ' - '.join(celulares)
        print(nomes)
    elif (comando == "D"):
        deletar_marca = input("Marca que deseja deletar\n⇢ ")
        if(deletar_marca in celulares):
            celulares.remove(deletar_marca)
        nomes = ' - '.join(celulares)
        print(nomes)
    elif (comando == "L"):
        nomes = ' - '.join(celulares)
        print(nomes)
    continua = input("Deseja continuar ? Digite SIM ou NÃO\n⇢ ") 
arquivo.writelines(nomes)
arquivo.close()
