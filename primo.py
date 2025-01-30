import matplotlib.pyplot as plt

def primos_ate(n):
    primos=list(range(2,n+1))
    compostos=list(range(2,n+1))
    idx=0
    while idx<len(primos):
        p=primos[idx]
        compostos.remove(p)
        j=p+1
        while j<=n:
            if j%p==0:
                if j in primos:
                    primos.remove(j)
            j=j+1
        idx=idx+1
    return primos

def maior_fator_primo_de(n):
    for p in primos_ate(n)[::-1]:
        if n%p==0:
            return p
    

def fib(n):
    a=1
    b=0
    while (n>0):
        a,b=b,(a+b)
        n-=1
    return b


def e_primo(n):
    if (n==0) or (n==1):
         return False
    for k in list(range(2,n,1)):
            if n%k == 0:
                return False
    return True


def proporcao_fib(n):
    aux=0
    lista=[]
    while aux<n:
       lista.append(fib(n))
       

def proporcao_primos(n):
    aux=1
    lista=[]
    while aux<n:
        if e_primo(aux)==True:
            lista.append(aux)
    aux=aux+1
    return len(lista)/n


def lista_fib(n):
    lista=[]
    aux=0
    while aux<n:
        lista.append(fib(aux))
        aux=aux+1
    return lista

def lista_eficiente_fib(n):
    lista=[0,1]
    aux=0
    while aux<(n-2):
        lista.append((lista[-1]+lista[-2]))
        aux=aux+1
    return lista

#print(lista_eficiente_fib(20))
n=5
print(proporcao_primos(n))
#plt.plot(range(0,n), proporcao_primos(n),'o')
#plt.show()

