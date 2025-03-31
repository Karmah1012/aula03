time1 = input("Qual o time 1?")
time2 = input("Qual é o time 2?")
gols1 = int(input(f"Quantos gols fez o {time1}?"))
gols2 = int(input(f"Quantos gols fez o {time2}?"))
if gols1 > gols2:
    print(f"{time1} venceu a partida! ")
else:
    print(f"{time2} venceu a partida! ")