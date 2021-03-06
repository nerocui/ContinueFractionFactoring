# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:02:59 2018

@author: Nero
"""

from fractions import Fraction
import math
import sys



alpha_ = []
P_ = []
Q_ = []
a_ = []
c_ = []
pi_ = []
qi_ = []
first_ = []
second_ = []
two = 2
two_ = 0
num = 0
result_pi = []
result = []

n = 157942
print('n: ', n)

P0 = 0
Q0 = 1

def printResult():
    for f in first_:
        if f in second_ or first_.count(f) > 1:
            if first_.index(f) != second_.index(f):
                del second_[first_.index(f)]
                del first_[first_.index(f)]
    for i in range(len(first_)):
        print('First factor: ', first_[i])
        print('Second factor: ', second_[i])
        


while(math.fmod(n,2) == 0):
    if int(n/2) != 1 and int(n/2) not in first_:
        first_.append(two)
        second_.append(int(n/2))
    two = two*2
    n = int(n/2)
    two_ += 1
        
if n==1:
    printResult()
    sys.exit()
        


alpha = math.sqrt(n)
a = math.floor(alpha)

alpha_.append(alpha)
P_.append(P0)
Q_.append(Q0)
a_.append(a)

P = P0
Q = Q0



        
        

while(1):
    P_next = a*Q - P
    Q_next = (n-math.pow(P_next, 2))/Q
    alpha = (P_next + math.sqrt(n))/Q_next
    a = math.floor(alpha)
    if alpha in alpha_:
        break;
    else:
        P = P_next
        Q = Q_next
        alpha_.append(alpha)
        P_.append(P)
        Q_.append(Q)
        a_.append(a)

def getC(array):
    if len(array) == 0:
        return 0
    else:
        return Fraction(1, array[0] + getC(array[1:]))

print('a:')
print(a_)


for i in range(len(a_)):
    c_.append(Fraction(a_[0]+getC(a_[1:i])))




def is_square(number):
    if (math.sqrt(number)-int(math.sqrt(number))):
        return False
    else:
        return True



for c in c_:
    pi_.append(c.numerator)
    qi_.append(c.denominator)
    num = c.numerator ** 2 - n*(c.denominator ** 2)
    if num > 0 and num != 0 and is_square(num):
        result.append(int(math.sqrt(num)))
        result_pi.append(c.numerator)
    

print('pi:')
print(pi_)
print('qi:')
print(qi_)
print('\n')

temp_first_ = []
temp_second_ = []

for i in range(len(result)):
    first = math.gcd(result_pi[i] - result[i], n)
    second = math.gcd(result_pi[i] + result[i], n)
    if first != 1 and second != 1:
        temp_first_.append(first)
        temp_second_.append(second)


for t in range(two_):
    for i in range(len(temp_first_)):
        first_.append(int(temp_first_[i] * math.pow(2,t)))
        second_.append(int(temp_second_[i]*math.pow(2, two_ - t)))


printResult()
        



























        