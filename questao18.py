lista = []
count = 0

quant = input("quantidade de numeros inseridos: ")
while quant != count:
    numero = lista.append(float(input("insira um número: ")))
    count += 1

print("lista: ", lista, " maior: ", max(lista), " menor: ", min(lista))
print(" soma: ", max(lista) + min(lista))