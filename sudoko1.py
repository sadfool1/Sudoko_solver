#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:12:32 2020

@author: jameselijah
"""

import numpy as np
import random as rn
import math

def create_board():
    
    row = []
    column = []
    
    temp = [1,2,3,4,5,6,7,8,9]
    
    
    
    for i in range(len(temp)):
        row.append(temp.pop(rn.randint(0,abs(8-i))))
        temp2 = [1,2,3,4,5,6,7,8,9]
        
        for j in range(len(temp2)):
            column.append(temp2.pop(rn.randint(0,abs(7-i))))
            
            
        
    print (row)
        
    
    board = {}
    
    #for i, element in enumerate(10):
    #    for j, element in enumerate(9):
       #     print (i,j)
            

    return 
    
    #return sorter(row)

create_board()