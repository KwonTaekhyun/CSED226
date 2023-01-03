import numpy as np
import pandas as pd

# Problem 1


def factorial(n):
    # BEGIN_YOUR_CODE
    if n < 0:
        return 0

    zeroNum = 0

    while n // 5 != 0:
        zeroNum += (n // 5)
        n //= 5

    return zeroNum
    # END_YOUR_CODE

# Problem 2


def wordCount(filename):
    # BEGIN_YOUR_CODE
    f = open(filename, 'r', encoding='CP949')
    fileLines = f.readlines()
    f.close()

    wordsNum = {}
    word = ''
    for line in fileLines:
        if line == '\n':
            continue
        else:
            for char in line:
                if char == '\n':
                    if word == '':
                        break
                    else:
                        if word in wordsNum.keys():
                            wordsNum[word] += 1
                        else:
                            wordsNum[word] = 1
                        word = ''
                    break
                elif char == ' ':
                    if word in wordsNum.keys():
                        wordsNum[word] += 1
                    else:
                        wordsNum[word] = 1
                    word = ''
                else:
                    word += char
            if word != '':
                if word in wordsNum.keys():
                    wordsNum[word] += 1
                else:
                    wordsNum[word] = 1

    return wordsNum
    # END_YOUR_CODE

# Problem 3


class car:
    def __init__(self, args):
        brand, model, price = args
        self.brand = brand
        self.model = model
        self.price = price


def averagePrice(args):
    # BEGIN_YOUR_CODE (our solution is 10 lines of code, but don't worry if you deviate from this)
    carList, brand = args

    carDict = {}
    for carInfo in carList:
        if carInfo.brand in carDict.keys():
            carDict[carInfo.brand] += [carInfo.price]
        else:
            carDict[carInfo.brand] = [carInfo.price]

    if brand in carDict.keys():
        return sum(carDict[brand]) / len(carDict[brand])
    else:
        return 0
    # END_YOUR_CODE

# Problem 4


def distance(arr1, arr2):
    # BEGIN_YOUR_CODE
    return round(np.sum((arr1 - arr2) ** 2) ** 0.5, 1)
    # END_YOUR_CODE

# Problem 5


def pokemon(original_file, modified_file):
    # BEGIN_YOUR_CODE
    origindf = pd.read_csv(original_file)
    df = origindf.dropna().drop(['Legendary', 'Sp. Atk', 'Sp. Def'], axis=1)
    type1Filter = ['Grass', 'Fire', 'Water', 'Normal']
    df = df[df['Type 1'].isin(type1Filter)]
    df = df[df['Total'] > 200]
    df = df.assign(Power=lambda x: x['Attack'].apply(
        lambda y: 'strong' if y > 80 else 'weak'))
    # END_YOUR_CODE
    df.to_csv(modified_file, index=False)

# Problem 6.a


def emp_table(dep, emp1, emp2):
    # BEGIN_YOUR_CODE (our solution is 7 lines of code, but don't worry if you deviate from this)
    depdf = pd.read_csv(dep)
    df = pd.concat([pd.read_csv(emp1), pd.read_csv(emp2)])
    df = df.drop(['employee_id'], axis=1)
    df['department_name'] = df['department_id'].map(
        depdf.set_index('department_id')['department_name'])
    df = df.drop(['department_id'], axis=1)
    df = df.sort_values('salary')
    # END_YOUR_CODE
    return df

# Problem 6.b


def lowest_avg(dep, emp1, emp2):
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    depdf = pd.read_csv(dep)
    df = ((pd.concat([pd.read_csv(emp1), pd.read_csv(emp2)])).groupby(
        ['department_id']).mean()).sort_values('salary')
    return (depdf.loc[depdf['department_id'] == df.index[0]].iloc[0])['department_name']
    # END_YOUR_CODE
