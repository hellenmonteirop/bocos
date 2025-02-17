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

n=3
gra=erdos_renyi(n, p = 0.5, xlim = (0,10), ylim = (0,10))
print(gra)

def os_vertices_sao(G):
    print(f'Os vertices são:',G.keys())

def as_arestas_sao(G):
    print(f'As arestas são:')
    for i in list(G.keys()):
        for j in G[i]:
            print(G[j])
            #j = G[i].pop()

        

as_arestas_sao(gra)

#def esta_conectado(v1,v2,G):

    
    #return True/false