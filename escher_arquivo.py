from arquivos_obi import read_OBI_files

for input, sol, file_input, file_output in read_OBI_files("\escher"):
    tamanho = int(input[0])
    sequencia = input[1].split(" ")
    sequencia = [int(x) for x in sequencia]

    gabarito = sol[0]

    saida = None
    sequencia_reversa = sequencia.copy()
    sequencia_reversa.reverse()

    numero_escher = sequencia[0] + sequencia_reversa[0]
    for i, j in zip(sequencia, sequencia_reversa):
        if (i + j) != numero_escher:
            saida = "N"
            break
        else:
            saida = "S"

    if saida != gabarito:
        print("Erro para", sequencia)
        print("Saida gerada:", saida)
        print("Gabarito:", gabarito)
        print(file_input, file_output)
