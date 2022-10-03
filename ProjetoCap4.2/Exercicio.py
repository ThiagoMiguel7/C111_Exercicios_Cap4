import numpy as np

# Importando o csv
data = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8') #

# Exércicio 1 
print('\033[1m' + 'Exercício 1' + '\033[0m')

numMissions = np.max(data[1:, 0].astype('int32')) # Linha e coluna - Pegar tudo a partir da 1º linha até o final da coluna 0
missionStatus = data[1:, 7].copy() # Copia toda a coluna Status Mission
statusMission = np.char.endswith(missionStatus, "Success") #indica se uma string termina com determinados caracteres.
num_statusMission = np.sum(statusMission) # Indica o numero de quantas Strings terminam com "Sucess".
percent = (num_statusMission / numMissions) * 100  

print('A porcentagem de missões que deram certo é de ' + '%.2f' % percent + "%.")
print()

# Exércicio 2
print('\033[1m' + 'Exercício 2' + '\033[0m')

totalCost = np.array(data[1:, 6].astype('float32'))
numCost = len(totalCost[totalCost > 0]) # Retorna o número total da quantidade de valores maiores que zero.
sumCost = sum(totalCost[totalCost > 0]) # Retorna a soma de todos os valores.
averageCost = (sumCost/numCost)

print("Média de gastos nas missões espaciais é de $" + '%.2f' % averageCost + " mil Doláres.")
print()


# Exércicio 3
print('\033[1m' + 'Exercício 3' + '\033[0m')

location = data[1:, 2]
usa = np.char.endswith(location, 'USA') #indica se uma string termina com determinados caracteres.
num_missionsUSA = np.sum(usa) # Indica o numero de quantas Strings terminam com "USA"

print(f"Número de missões espaciais realizadas pelos EUA é {num_missionsUSA}.")
print()


# Exércicio 4
print('\033[1m' + 'Exercício 4' + '\033[0m')

missions_spaceX = data[1:, (1, 6)] # Linha e coluna - Pegar tudo a partir da 1º linha até o final da coluna 0 
                                   # e relaciona com as colunas Company e Cost.

condition = missions_spaceX[0:, 0] == "SpaceX" 
mostExpensive = np.max(totalCost[condition])

print(f'A missão mais cara realizada pela SpaceX foi de ${mostExpensive} mil Doláres.')
print()


# Exércicio 5
print('\033[1m' + 'Exercício 5' + '\033[0m')

companies = data[1:, 1] # Company
all_companies = np.unique(companies) #Pega a variedade de dados da coluna sem repetição

for cmpy in all_companies:
    aux = np.char.find(companies, cmpy) # Vai procurar dentro de Companies e ver se dentro de companies tem a iteração igual com a empresa que tá na hr
    num_missoes = np.sum(aux) + companies.size # quantidade total de aux + tamanho inteiro 
    print(f'Company: \033[1m {cmpy} \033[0m = {num_missoes} mission(s).')
