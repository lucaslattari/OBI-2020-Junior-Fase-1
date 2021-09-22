moedas = int(input())
marinheiros = int(input())

#pela lógica, o capitão recebe o mesmo que 2 marinheiros, logo ele vale "por dois"
marinheiros += 2

moedas_por_marinheiro = int(moedas / marinheiros)

print(moedas_por_marinheiro + moedas_por_marinheiro)
