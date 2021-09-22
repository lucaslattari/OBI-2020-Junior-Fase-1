tamanho = int(input())
sequencia = input().split(" ")
sequencia = [int(x) for x in sequencia]
sequencia_reversa = sequencia.copy()
sequencia_reversa.reverse()

numero_escher = sequencia[0] + sequencia_reversa[0]
for i, j in zip(sequencia, sequencia_reversa):
  if (i + j) != numero_escher:
    print("N")
    break
else:
  print("S")
