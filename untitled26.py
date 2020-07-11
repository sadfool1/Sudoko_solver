#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:14:15 2020

@author: jameselijah
"""

import numpy as np
import random as rn
import math

board = [
        [1,2,3,4,5,6,7,8,9],
        [2,1,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,6,5,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9]
        ]

def column_similarity (board, row, col):
    my_number = board[row][col]
    print (my_number)

    
    for i in range (9):
        if (i,col) == (row,col):
            continue
        elif board[i][col] == my_number:
            return [i, False]
        else:
            continue
            
print (column_similarity (board, 5, 0))
            
            