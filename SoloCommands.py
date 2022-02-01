class SoloCommands:
    def __init__(self):
        pass

    # Procedimento quando a palavra é aceita.    
    def accept(self, queue):
        strQueue = '[ '
        # Transforma em uma só string para printar a palavra.
        for i in queue:
            strQueue = strQueue + i + ' '
        strQueue = strQueue + ']'
        
        print(strQueue)
        print('Palavra aceita! :)')
        print('Fim do programa')
        exit()
    
    # Procedimento quando a palavra é rejeitada.
    def reject(self):
        print('Palavra rejeitada! :(')
        print('Fim do programa')
        exit()
    
    # Função para leitura do primeiro elemento da fila de palavra.
    def readContent(self, queue):
        symbol = queue[0]
        queue = queue[1:]
        # Retorna a Fila sem o primeiro elemento, retornando o primeiro da fila que foi lido e a fila atual.
        return queue, symbol