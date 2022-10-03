import numpy as np

#NUMEROS ALEATORIOS (random)

np.random.seed(10) # Semente Aleatória

#1.Dentro de um intervalo
arr = np.random.randint(1,20,10) #1-Inicio / 2-Fim / 3- Quantidade de numeros aleatórios
print(arr)

#Extraindo os elementos unicos com UNIQUE

#print(np.unique(arr))
#print(np.unique(arr, return_counts=True))

#2.Usando distribuição de probabilidade

#np.random.seed(10)
#np.random.normal()
#np.random.uniform()
#np.random.weibull()


#Matriz de Valores

mtz = np.arange(1, 10, 1).reshape(3,3)
print()

#print(mtz)
#print()
#print(mtz.sum(axis=0)[0]) #soma coluna 1
#print(mtz.sum(axis=1)[0]) #soma linha 1

#Broadcasting

#print(mtz*10) # Capacidade de multiplicar ou fazer qualquer operação um Escalar com um Numpy Array
#print()
#print(mtz/10)


#Condicionais do Numpy
print(mtz%2==1)
print()
print(mtz[mtz%2==1])

#Analise textual com o Numpy (Char)

arr = ['Thiago','Thalita','Gabriel','Gustavo']
print(arr[np.char.find(arr,'o') > 0])






