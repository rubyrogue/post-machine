from Operations import Operations

class Main:
    def __init__(self):
        self.numeroLinha = None  # Numero da linha do arquivo
        self.conteudoLinha = None  # Conteudo da linha do arquivo

if __name__ == "__main__":
    # Passa como parametro o arquivo e a palavra
    nomeArq = input("Digite o nome do arquivo: ")
    seqEstado = input("Digite a palavra: ")
    ext = nomeArq.split('.')

    # Confere se a extensão do arquivo é MP
    if len(ext) == 2 and ext[1] == 'mp':
        try:
            # Leitura do arquivo
            arq = open(nomeArq, 'r')
        except IOError:
            print('Erro! Arquivo não existente')
            exit()
            
        vetorArq = []
        nLinha = 1
        # Pega cada string digitada no arquivo e passa para um vetor
        for linha in arq:
            m = Main()
            m.numeroLinha = nLinha
            m.conteudoLinha = linha.split()
            vetorArq.append(m)
            nLinha += 1

        # Pega cada caracter digitado como palavra e passa para um vetor
        VetorSeqEstado = ''
        for i in range(len(seqEstado)):
            VetorSeqEstado += seqEstado[i] + ' '
        VetorSeqEstado = VetorSeqEstado.split()

        # Inicio da maquina de post, verificando as operações.
        op = Operations(VetorSeqEstado, vetorArq)
    else:
        print("Extensão de arquivo inválida!")