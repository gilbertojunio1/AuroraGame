import textorpg

textorpg.historia()
textorpg.caminho()
escolha = input ("Qual sua escolha? ")
if escolha == "a":
    textorpg.castelo()
escolha = input("Qual sua escolha?")
if escolha=="a":
    textorpg.finalA()
elif escolha!="a": 
    textorpg.finalB()
