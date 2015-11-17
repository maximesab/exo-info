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
 
def to_bin(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])
      
def bitnumbers_debug (N,M,i,j):
    mask = ~0 # 111111 32 times
    print to_bin(mask)
    mask = mask << j-i+1 # 1111110000     1 32 - j-1+i times, 0 j-i+1 times
    print to_bin(mask)
    mask = ~ mask # 0000001111      0 32 - j-1+i times, 1 j-i+1 times
    print to_bin(mask)
    mask = mask << i # 0000001111000 0     32 - j-1 times, 1 j-i+1 times, 0 i times
    print to_bin(mask)
    print to_bin((N & ~mask) | (M << i))
    return (N & ~mask) | (M << i)
      
def bitnumbers (N,M,i,j):
    mask = ~0 # 111111 32 times
    mask = mask << j-i+1 # 1111110000     1 32 - j-1+i times, 0 j-i+1 times
    mask = ~ mask # 0000001111      0 32 - j-1+i times, 1 j-i+1 times
    mask = mask << i # 0000001111000 0     32 - j-1 times, 1 j-i+1 times, 0 i times
    return (N & ~mask) | (M << i)

        

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
        
        




    
