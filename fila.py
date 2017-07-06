class Fila:

    def __init__(self):
        self.fila= []
    def criar_fila(self,tamanho,item):
        self.fila.append(item)
    def fila_nao_esta_vazia(self):
        return (len(self.fila) == 0 )
    def colocar_fila(self, x):
        self.fila.append(x)
    def sair_fila(self):
        return self.fila.pop(0)
