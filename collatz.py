#problema: qual é o maior caminho (gamma) tal que gamma(0) (0 é o primeiro n) com n pertence [1,500] até o ciclo  (4,2,1)?
#obs: max(gamma) pode ser maior que 500
#pare chegando no 1

import numpy as np

def collatz(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
    
def caminho_collatz_burro(n):
    t=[]
    while n!=1:
        t.append(n)
        n=collatz(n)
    t.append(1.0)
    return t
        
def tamanho_caminho_collatz_burro(n):
    return len(caminho_collatz_burro(n))

def maior_caminho_collatz_dicio(m):
    n=np.arange(2,m+1,1)
    tamanho=dict() #d(n)=numero de caminhos de n ate 1
    tamanho[1]=1
    for i in n:
        if i in tamanho.keys():
            #print(i)
            continue
        else:
            cont=0
            aux=i
            lista_aux=[]
            while aux not in tamanho.keys():
                aux=collatz(aux)
                cont=int(cont+1)
                
                lista_aux.append(int(aux))
               
            cont=int(cont+tamanho[aux])
            tamanho[i]=cont
            #print(i,tamanho[i])
            for k in np.arange(1,len(lista_aux)):
                tamanho[lista_aux[k]]=int(cont -k-1)
                #print(lista_aux[k],tamanho[lista_aux[k]])

    print(max(tamanho, key=tamanho.get))
    
maior_caminho_collatz_dicio(500000)
