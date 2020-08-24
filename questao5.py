pA=int(input("População A: "))
while pA<0:
    pA=int(input("Numero invalido: "))
taxaA=float(input("Taxa de crescimento A: "))

pB=int(input("População B: "))
while pB<0:
    pB=int(input("Numero invalido: "))
taxaB=float(input("Taxa de crescimento B: "))

ano=0
while pA < pB:
    ano += 1
    pA = int((1 + (taxaA/100) )* pA)
    pB = int((1 + (taxaB/100) )* pB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % pA)
    print("População B: %d\n\n" % pB)

print("Ultrapassa no ano:",ano)


