n = (input("Quantidade de temperaturas a inserir: ")
temperaturas = []
n1 = 1
for i in range(n):
    print("Temperatura n° ", n1)
    temperatura = temperaturas.append(float(input("insira a temperatura: ")))
    n1 += 1

print("Maior temperatura = ", max(temperaturas))
print("Menor temperatura = ", min(temperaturas))
print("Média = ", round(sum(temperaturas) / len(temperaturas), 2))