from fila import *

def valores(tamanho,item,matriz):
    fila = Fila()
    fila.criar_fila(tamanho,item)

    dist= []
    for i in range(tamanho):
        dist.append(tamanho)
    dist[item] = 0
    while not fila.fila_nao_esta_vazia():
        u = fila.sair_fila()
        for index,j in enumerate(matriz[u]):
            if j == 1 and dist[index] >= tamanho:
                dist[index] = dist[u] + 1
                fila.colocar_fila(index)
    return dist
def valores_esparsa(tamanho,item,esparsa):
    fila = Fila()
    fila.criar_fila(tamanho,item)
    dist= []
    for i in range(tamanho):
        dist.append(tamanho)
    dist[item] = 0
    while not fila.fila_nao_esta_vazia():
        u = fila.sair_fila()
        for j in range(tamanho):
            if busca_linear(esparsa,u,j) and dist[j] >= tamanho:
                dist[j] = dist[u] + 1
                fila.colocar_fila(j)
    return dist

def busca_linear(esparsa,x,y):
    linha=[]
    i=0
    while i != len(esparsa):
        linha= esparsa[i]
        if linha[0] == x and linha[1] == y:
            return True
        i+=1

def caminho(esparsa,tamanho,y,distancia_esp):
    comp=y
    print(y,'\t',distancia_esp[y])
    while comp != 0:
        for i in range(tamanho):
            if busca_linear(esparsa,i,comp) and distancia_esp[comp]-1:
                print(i,'\t',distancia_esp[i])
                comp = i

matriz = [[0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 1],
          [0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1] ]
esparsa=[]
u=0
a=[]
for i in range(len(matriz)):
    linha=[]
    linha=matriz[i]
    for j in range(len(linha)):
        if linha[j] != 0:
            esparsa.append([])
            esparsa[u].append(i)
            esparsa[u].append(j)
            u+=1
print(esparsa)
x=int(input("Digite um numero de 1 a 6: "))
x-=1
y= 6
distancia_esp=[]
distancia_esp=valores_esparsa(6,x,esparsa)
print(distancia_esp)
print("Distancia de %d para %d é %d"%(x,y,distancia_esp[1]))
caminho(esparsa,6,1,distancia_esp)
