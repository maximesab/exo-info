# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:18:26 2015

@author: max
"""
import math

#ex 8.1: gives the nth number of fibonanci suite

def fibo(n):
    # en iteratif:
    if n <= 2:
        return 1
    first, second = 1, 1
    for i in xrange(n-2):
        first, second = second, first + second
    return second
        
#ex 5.1
 
      
def bitnumbers (N,M,i,j):
    
    N1 = N - decimalpart(N*math.pow(10,-j))*math.pow(10,j)
    
    N2 = N - decimalpart(N*math.pow(10,-i))*math.pow(10,i)
    
    N3 = N +N1 -N2
    return N3 + M*math.pow(10,i)
        

def decimalpart(N):
    return N%1


# ex 8.7: dimes exercice

def number_cases(n, coins=[1, 5, 10, 25]):
    if len(coins) == 0:
        return 1 if n == 0 else 0
    res = 0
    bigger_coin = coins[-1]
    other_coins = coins[:-1]
    while n >= 0:
        res += number_cases(n, other_coins)
        n -= bigger_coin
    return res
        
        




    
