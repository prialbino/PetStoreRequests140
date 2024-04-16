import csv  # biblioteca que sabe como ler e escrever de um arquivo csv

def ler_csv(arquivo_csv):
    dados_csv = []       # cria uma lista em branco
    try:                 # tratamento de erro;tentar   
        with open(arquivo_csv, newline='') as massa:  # informa nome e apelido massa. Newline seria o caracter de final de linha
            tabela = csv.reader(massa, delimiter=',') # informa que o separador dos campos da massa e uma virgula
            next(tabela)   # serve para pular a linha de cabecalho
            for linha in tabela:   # para cada linha na tabela
                dados_csv.append(linha)   # guardando os dados separados para uso
        return dados_csv        # devolver os dados para serem usados no teste
    except FileNotFoundError:    # trata erro de arq nao encontrado
        print(f'Arquivo nao encontrado:{arquivo_csv}')  # msg de erro arq nao encontrado
    except Exception as fail:     # qq erro nao previsto
        print(f'Falha imprevista:{fail}')