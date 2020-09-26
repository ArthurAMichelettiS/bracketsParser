# Arthur Augusto Micheletti de Souza
# 081180004


# Entrada pelo input do console



txt = input()

pares = {"<": ">", "{": "}", "[": "]", "(": ")"}

pilha = []

valido = False

for c in txt:
    if pares.keys().__contains__(c):
        pilha.append(c)
    elif len(pilha) != 0:
        if pares[pilha.pop()] != c:
            break
    else:
        break
else:
    if len(pilha) == 0:
        valido = True

print("Válido" if valido else "Inválido")

