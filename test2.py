#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:24:42 2020

@author: jameselijah
"""
import random as rn
j = 1 #number 4 in temporary_row

board = [
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,6,5,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9]
        ]

randomizer = rn.choice([x for x in range(0, 9) if x != j]) #randomize the list cell
temp = board[8][randomizer] #integer for the randomized list cell
board[8][randomizer] = board[8][j]
board[8][j] = temp

print (board[8])

        