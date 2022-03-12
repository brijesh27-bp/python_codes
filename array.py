# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:39:20 2022

@author: user hp
"""
def has_33(nums):
    
    for digit in nums:
        
        if nums[digit] == 3 :
            return True
        else:
            return False
    