# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 10:17:59 2022

@author: user hp
"""
def old_macdonald(name):
    
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'oopsss'