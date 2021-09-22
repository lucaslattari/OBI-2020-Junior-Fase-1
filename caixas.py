caixas = []

caixas.append(int(input()))
caixas.append(int(input()))
caixas.append(int(input()))

if caixas[0] == caixas[1] == caixas[2]:
  print("3")
else:
  maior_caixa_indice = caixas.index(max(caixas))
  if caixas[maior_caixa_indice] > sum(caixas) - caixas[maior_caixa_indice]:
    print("1")
  elif caixas[0] == caixas[1] or caixas[0] == caixas[2] or caixas[1] == caixas[2]:
    print("2")
  else:
    print("1")
