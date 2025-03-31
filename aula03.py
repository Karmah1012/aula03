nome = input("Qual é o seu nome?")
print (f"Meu nome é: {nome}")
idade = int(input("Qual a sua idade?"))
print (f"Minha idade é: {idade}")
salario = float(input("Quanto você ganha?"))
print (f"Meu salário é: {salario}")
print (f"Eu me chamo {nome}, tenho {idade} anos e recebo {salario} de salário")
aumento = float(input("Quanto o seu salário aumentou?"))
valor_acrescimo = salario*(aumento/100)
print (valor_acrescimo)
salario_do_mes = valor_acrescimo + salario
print (f"O salário do mês é: {salario_do_mes}")


