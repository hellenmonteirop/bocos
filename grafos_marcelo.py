#1) escolha como representar um grafo
#2) dado um grafo, listar as componentes conexas
#3) dado um grafo conexo (sem componentes desconexas) e dois vertices nele, achar um caminho (o menor?) entre eles 
import random
def erdos_renyi(n, p = 0.5, xlim = (0,10), ylim = (0,10)): #by marcelo carneiro
    G = dict()
    for idx in range(n):
        x,y = random.randint(xlim[0], xlim[1]), random.randint(ylim[0], ylim[1])
        G[(x,y)] = []
    
    keys = list(G.keys())

    for idx1 in range(len(keys)):
        for idx2 in range(idx1, len(keys)):
            if idx1 == idx2:
                continue
            else:
                coin = (random.uniform(0,1) > p)
                if coin:
                    G[keys[idx1]]+=[keys[idx2]]
                    G[keys[idx2]]+=[keys[idx1]]
    return G

def os_vertices_sao(G):
    print(f'Os vertices são:',G.keys())

def as_arestas_sao(G): 
    print('Existem arestas entre os vertices:')
    arestas=[]
    for i in list(G.keys()): #para todos os i-vertices do grafo
        while G[i]: #enquanto tiver arestas no i-ésimo vértice
            j = G[i].pop() #tira o ultimo vertice do grafo e deixa ele na variavel j
            if j in G and i in G[j]:#se o vertice j esta no grafo 
                #e o vertice i esta na lista de vertices do j então 
                # remove o i-esimo vertice da lista de arestas do j-esimo vertice
                #para evitar a dupla aparição
                G[j].remove(i) 
            #print(i,j) 
            arestas.append((i,j))
    return arestas

n=4
gra=erdos_renyi(n, p = 0.5, xlim = (0,10), ylim = (0,10))
print(gra)
are=as_arestas_sao(gra)
print(are)
#def esta_conectado(v1,v2,G):

    
    #return True/false