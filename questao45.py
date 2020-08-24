gabarito = []
r = []
n = []
print("\nProfessor: ")
for i in range(10):
    print("Questão: ", i + 1)
    resposta_certa = gabarito.append(input("Digite a alternativa correta: "))
n_aluno = 1
continuar = True
while continuar != 'n':
    print("\n" * 5)
    print("Aluno n°", n_aluno, ":")
    r.clear()
    for i in range(10):
        print("Questão: ", i + 1)
        resposta_aluno = r.append(input("Escolha a alternativa: "))
    nota = 0
    for i in range(10):
        if r[i] == gabarito[i]:
            nota += 1
    n.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ")
    n_aluno += 1
print(len(n), "alunos utilizaram o sistema")
print("\nA maior nota tirada foi: ", max(n))
print("A menor nota tirada foi: ", min(n))
print("A media de notas da turma foi de:", sum(n) / len(n))
print(no)