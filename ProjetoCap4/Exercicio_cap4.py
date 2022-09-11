import numpy as np

# Exércicio 1
print('\033[1m' + 'Exercício 1' + '\033[0m')

array1 = np.linspace(0, 1, 21)
print('Array 1: ', '\n' , array1)

# Exércicio 2
print('\n\033[1m' + 'Exercício 2' + '\033[0m')

array2 = np.arange(0, 51, 2)
array3 = np.arange(100, 49, -2)
arrayTogether = np.concatenate((array2, array3))

print('Array 2: ','\n', array2)
print('Array 3: ','\n', array3)
print('Array 2 e 3 ordenados: ','\n', sorted(arrayTogether))


# Exércicio 3
print('\n\033[1m' + 'Exercício 3' + '\033[0m')

print('Array 2 + Array 3 invertidos: ','\n', np.flip(sorted(arrayTogether))) #Flip só funciona para estruturas já ordenadas


# Exércicio 4
print('\n\033[1m' + 'Exercício 4' + '\033[0m')

matriz1 = np.array([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]])

dimension1 = matriz1.shape


print('Matriz', dimension1[0],'x',dimension1[1],':')
print(matriz1)

matriz2 = matriz1.reshape(1,12)
print('Matriz transformada em 1-D =', matriz2)


# Exércicio 5
print('\n\033[1m' + 'Exercício 5' + '\033[0m')

matriz3 = np.array([[0,1,2,3,4],
                    [5,6,7,8,9],
                    [10,11,12,13,14],
                    [15,16,17,18,19],
                    [20,21,22,23,24]])

dimension2 = matriz3.shape

print(matriz3,'\n')

if((dimension2[0] * dimension2[1])%2 == 0):

    print('A matriz com dimensões', dimension2[0], 'x', dimension2[1],'pode se tornar um vetor com um número par de elementos porque',
          dimension2[0] * dimension2[1], 'que é um número par!')

else:
    print('A matriz com dimensões', dimension2[0],'x',dimension2[1] , 'pode se tornar um vetor com um número ímpar de elementos porque',
          dimension2[0] * dimension2[1], 'que é um número ímpar!')