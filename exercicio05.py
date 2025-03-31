n1 = float(input("Qual a primeira nota?"))
n2 = float(input("Qual a segunda nota?"))
n3 = float(input("Qual a terceira nota?"))
media = float(n1+n2+n3)/3
print(f"A média do aluno, é: {media}")
if media >= 7 :
    print("Aluno APROVADO!")
else:
    if media < 4:
        print(f"Aluno reprovado {media}")
    else:
        print(f"Aluno em recuperação {media}")