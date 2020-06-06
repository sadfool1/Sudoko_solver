#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:24:42 2020

@author: jameselijah
"""

def create_board():
    
    row = []
    
    temp = [1,2,3,4,5,6,7,8,9]
    
    
    for i in temp:
        print (i)
        row.append(temp.pop(rn.randint(0,abs(8-i))))
        
    print (row)
        
create_board()