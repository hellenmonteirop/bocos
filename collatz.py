#problema: qual é o maior caminho (gamma) tal que gamma(0) (0 é o primeiro n) com n pertence [1,500] até o ciclo  (4,2,1)?
#obs: max(gamma) pode ser maior que 500
#pare chegando no 1

import numpy as np

def collatz(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
    
#def distancia_collatz(n,tamanho):



m=14
n=np.arange(2,m+1,1)
tamanho=dict() #d(n)=numero de caminhos de n ate 1
tamanho[1]=1
aux=0
for i in n:
    if i in tamanho.keys():
        continue
    else:
        while aux!=1:
            
    n=collatz(n)
    aux=aux+1
print(f'caminho de',m,'ate 1 e',aux)
