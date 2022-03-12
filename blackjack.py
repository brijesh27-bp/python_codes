# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:21:11 2022

@author: user hp
"""
def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    
    elif sum((a,b,c)) > 21 and 11 in (a,b,c):
        return (sum((a,b,c))-10)
    
    else :
        
        return 'BUST'
            