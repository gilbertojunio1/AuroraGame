import textorpg

textorpg.historia()
textorpg.caminho()
escolha = input ("Qual sua escolha?\n⩥ ")
if escolha == "1":
    textorpg.castelo()
if escolha == "2":
    textorpg.vilas()
    escolha = input("Qual sua escolha?\n⩥ ")
if escolha == "a" or escolha == "b":
    textorpg.orc()
    escolha = input("Qual sua escolha?\n⩥ ")
if escolha == "3":
    textorpg.castelo()
escolha = input("Qual sua escolha?\n⩥ ")    
if escolha == "8":
    textorpg.final8()
if escolha == "9": 
    textorpg.final9()
