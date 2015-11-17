# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:18:26 2015

@author: max
"""
import math

#ex 8.1: gives the nth number of fibonanci suite
 


def fibo(n):
      if n <= 2:
          return 1
      return fibonanci(1,1,n,2):

def fibonanci(previous,last,n,compteur):
    
    if compteur == n:
        return last
    else:
        new_last = previous + last
        previous = last
        compteur +=1
        return fibonanci(previous, new_last, n, compteur)
        
#ex 5.1
 
      
def bitnumbers (N,M,i,j):
    
    N1 = N - decimalpart(N*math.pow(10,-j))*math.pow(10,j)
    
    N2 = N - decimalpart(N*math.pow(10,-i))*math.pow(10,i)
    
    N3 = N +N1 -N2
    return N3 + M*math.pow(10,i)
        

def decimalpart(N):
    N1 = N%1
    return N1


# ex 8.7: dimes exercice


def number_cases(n):

    n25 = ((n/25)%25)
    
    #for each number of quarter there is the possibility 
    #of repressenting it with one piece 5 and 2 of 10
    
    n10 = (((n-n25*25)/10)%10)
    #for each number of dimes there is the possibility 
    #of repressenting it with 2 piece of 5
    
    
    n5 =(((n- n25*25 - n10*10)/5)%5)
    #for each number of nickels there is the possibility 
    #of repressenting it with 5 piece of 1
    
    
    number_of_representation = 1*max(n5*2,1)*max(n10*2*2,1)*max(n25*(2*2+2),1)
    return number_of_representation
        
        




    
