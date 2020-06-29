#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:12:32 2020

@author: jameselijah
"""

import numpy as np
import random as rn
import math


board = [[1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9]]

def get_col(board, col):
    column = []
    for i in range(9):
        row = board[i]
        temp = board[i][col]
        column.append(temp)
    return column

def get_row(board):
    for i in range(9):
        row = board[i]
    return column
        
def column_checker(board):
    for i in range(9):
        temp = set(get_col(board,i))
        while len(temp) < 9:
            fix_column(board)
        else:
            #print (board)
            print('hi')
        
def fix_column(board):
    try:
        counter = 0
        for i in range(9):
            counter =+ 1
            for j in range(9):
                if counter < 9:
                    if board[i][j] == board[i+1][j]:
                        randomizer = random.choice([x for x in range(0, 9) if x != j]) #randomize the list cell
                        
                        temp = board[i][randomizer] #integer for the randomized list cell
                        board[i][randomizer] = board[i][j]
                        board[i][j] = temp
                    else:
                        continue 
                elif counter == 9:
                    board[9][j] == board[i+1][j]
                    
                    
    except IndexError as e:
        print (board)
        raise e
        
column_checker(board)
#column = 5
#col = column - 1
#print (get_col(board,col))
    