from arquivos_obi import read_OBI_files

for input, sol, file_input, file_output in read_OBI_files("\caixas"):
    caixas = [int(i) for i in input]
    gabarito = int(sol[0])

    saida = None
    if caixas[0] == caixas[1] == caixas[2]:
        saida = 3
    else:
        maior_caixa_indice = caixas.index(max(caixas))
        if caixas[maior_caixa_indice] > sum(caixas) - caixas[maior_caixa_indice]:
            saida = 1
        elif caixas[0] == caixas[1] or caixas[0] == caixas[2] or caixas[1] == caixas[2]:
            saida = 2
        else:
            saida = 1

    if saida != gabarito:
        print("Erro para", caixas)
        print("Saida gerada:", saida)
        print("Gabarito:", gabarito)
        print(file_input, file_output)
