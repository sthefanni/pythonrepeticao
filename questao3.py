nome = input("Nome: ")
idade = int(input("Idade: ")
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))

while (salario<0):
    salario = float(input("Salario invalido: "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Sexo invalido: ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    civil = input("Resposta invalida")


