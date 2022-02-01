class Error:
    # Classe responsavel pela mensagem de erro
    def __init__(self, row, content):
        strContent = ''
        for i in content:
            strContent = strContent + i + ' '
        print('Erro de compilação! Linha <{:d}> : " {:s}"'.format(row, strContent))
        exit()