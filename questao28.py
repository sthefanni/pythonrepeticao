q = input("Digite a quantidade de CD's : ")
cds = []
n = 1

for i in range(q):
    print("CD número ", n)
    valor_cd = cds.append(float(input("Digite o valor do CD: ")))
    n += 1

media = sum(cds) / len(cds)
print("A media para cada CD é: ", media)