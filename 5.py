# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.*

# Пример:
# 2*x² + 4*x + 5 = 0 
# 5*x² + 2*x + 43 = 0
# Результат: 7*x^2 + 6*x + 48 = 0


from itertools import *
import os
os.system("cls")


file1 = 'Answer.txt'
file2 = 'NotAnswer.txt'


def read_pol(file):  
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(pol):  
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol


pol1 = read_pol(file1)
pol2 = read_pol(file2)
print('Исходные полиномы:')
print(pol1)
print(pol2)
pol1_coef = list(map(int, convert_pol(pol1)))
pol2_coef = list(map(int, convert_pol(pol2)))

def get_polynomial(k, ratios):  
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')

sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
sum_coef = sum_coef[::-1]
sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
print('Итоговый результат сложения полиномов:\n', sum_pol)
with open('Result.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol)