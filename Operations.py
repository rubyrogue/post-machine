from Error import Error
from SoloCommands import SoloCommands
from MoreOperations import MoreOperations

class Operations:
    def __init__(self, queue, vetorArq):
        self.queue = queue  # Fila de entrada.
        self.symbol = '#'   # Simbolo atribuido no final da palavra.
        self.vetorArq = vetorArq   # Vetor com o conteudo do arquivo.
        self.queue.append(self.symbol)

        strQueue = '[ '
        for j in self.queue:
            strQueue = strQueue + j + ' '
        strQueue = strQueue + ']'
        print(strQueue)

        i = -1
        soloCommands = ['aceita', 'rejeita', 'read']

        self.symbol = queue[0]

        while True:
            i += 1

            # Verifica se o caracter lido não seja um comentario ou o arquivo vazio.
            if self.vetorArq[i].conteudoLinha != [] and self.vetorArq[i].conteudoLinha[0] != ';':      
                
                # Caso a linha do arquivo possua apenas uma string.
                if len(self.vetorArq[i].conteudoLinha) == 1:
                    if self.vetorArq[i].conteudoLinha[0] in soloCommands:
                        soloC = SoloCommands()

                        #Confere qual é comando, por ter apenas uma posição neste vetor.
                        if self.vetorArq[i].conteudoLinha[0] == 'aceita':
                            soloC.accept(self.queue)
                        elif self.vetorArq[i].conteudoLinha[0] == 'rejeita':
                            soloC.reject()
                        elif self.vetorArq[i].conteudoLinha[0] == 'read':
                            if self.queue != []:
                                self.queue, self.symbol = soloC.readContent(self.queue)
                            else:
                                error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)
                        else:
                            error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)

                # Caso a linha do arquivo possua duas string, referente ao solto de linha do codigo.            
                elif len(self.vetorArq[i].conteudoLinha) == 2:
                    if self.vetorArq[i].conteudoLinha[0] == 'jump':
                        moreOp = MoreOperations()
                        i = moreOp.jump(self.vetorArq[i].conteudoLinha[1])
                    else:
                        error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)

                # Caso a linha do arquivo possua três string, referente à atribuição.            
                elif len(self.vetorArq[i].conteudoLinha) == 3:
                    if self.vetorArq[i].conteudoLinha[0] == 'X' and self.vetorArq[i].conteudoLinha[1] == '<-':
                        moreOp = MoreOperations()
                        if self.vetorArq[i].conteudoLinha[2] == 'symbol':
                            self.queue.append(moreOp.atrib(self.symbol))
                        elif self.vetorArq[i].conteudoLinha[2] != "'#'" and self.vetorArq[i].conteudoLinha[2] != '#':
                            self.queue.append(moreOp.atrib(self.vetorArq[i].conteudoLinha[2]))
                        else:
                            error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)
                        print(self.queue)
                    else:
                        error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)
                   
                # Caso a linha do arquivo possua 4 string, referente a uma condicional.            
                elif len(self.vetorArq[i].conteudoLinha) == 4:
                    if self.vetorArq[i].conteudoLinha[0] == 'if':
                        try:
                            if self.vetorArq[i].conteudoLinha[1].replace("'", '') == self.queue[0]:
                                if self.vetorArq[i].conteudoLinha[2] == 'jump':
                                    moreOp = MoreOperations()
                                    i = moreOp.jump(self.vetorArq[i].conteudoLinha[3])
                                else:
                                    error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)
                        except IOError:
                            error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)
                    else:
                        error = Error(self.vetorArq[i].numeroLinha, self.vetorArq[i].conteudoLinha)
