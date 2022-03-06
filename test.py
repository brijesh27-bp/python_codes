# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:59:12 2020

@author: user hp
"""
def find(name):
    for letter in name:
         if letter == 'a':
             print('You got right!')
         else:
             print('OOpssss')
         break 
             
find('Brijesh')