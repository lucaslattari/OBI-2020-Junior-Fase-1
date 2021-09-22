frequencia_cardiaca_repouso = int(input())
frequencia_cardiaca_atual = int(input())
oxigenacao = int(input())

if frequencia_cardiaca_atual > 3 * frequencia_cardiaca_repouso or oxigenacao < 95:
  print("diminuir")
elif frequencia_cardiaca_atual < 2 * frequencia_cardiaca_repouso and oxigenacao > 97:
  print("aumentar")
else:
  print("manter")
