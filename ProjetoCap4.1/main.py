import numpy as np
'''
#CRIANDO UM NUMPY ARRAY

mtz = np.array([   # Usar esse formato para fazer matriz
    [1, 2, 3],     # colchete para identificar a lista
    [4, 5, 6],
    [7, 8, 9]
])

print(mtz)
print(type(mtz)) # para ver o tipo da variavel

'''

'''
mtz = np.arange(1, 10, 1).reshape(3,3).reshape(9) # De 1 até 10 pulando de 1 em 1.
                                                 # Reshape = Transformar um linha em matriz 3X3
print(mtz)
print(type(mtz))

'''

arr1 = np.arange(1, 10, 1)
arr2 = np.arange(5, 14, 1)

print(arr1)
print(arr2)
print(arr1 + arr2)
print(arr1 * arr2)
print(np.concatenate([arr1, arr2]))
print(np.intersect1d(arr1, arr2))


arr3 = np.concatenate([arr1, arr2]).reshape(3,6)

print(arr3.ndim) #Pegar dimenssão
print(arr3.shape) #Formato
print(arr3.size) #numero de elementos






