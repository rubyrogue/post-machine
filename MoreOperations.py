class MoreOperations:
    def __init__(self):
        pass
    
    # Retorna o simbolo da atribuição.
    def atrib(self, symbol):
        symbol = symbol.replace("'", "")
        return symbol

    # Realiza o salto de Linha indicado no codigo.
    def jump(self, row):
        return int(row) - 2