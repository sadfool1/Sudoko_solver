#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:12:32 2020

@author: jameselijah
"""

import numpy as np
import random as rn
import math


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

def get_col(board, col):
    column = []
    for i in range(9):
        temp = board[i][col]
        column.append(temp)
    return column

def get_row(board, row):
    return board[row]


def column_checker(board):
    for i in range(9):
        temp = set(get_col(board,i))
        
        length_temp = len(temp)

        while length_temp < 9:
            
            fix_column(board, i)
            
            length_temp = len(set(get_col(board,i))) #update the value of length 
            
            if length_temp < 9:
                continue
            else:
                break
        """
        else:
            print (board)
            break        """
            
def column_similarity (board, row, col):
    """
    want to check if that exact column has other numbers similar to it.
    OUTPUT: 
        1. None --> that number has no similar numbers in that column
        2. [i, col, False] --> i, col will tell us where that exact coordinate of similarity in first encounter
    """
    my_number = board[row][col]
    print (my_number)

    for i in range (9):
        if (i,col) == (row,col):
            continue
        elif board[i][col] == my_number:
            return [i, col, False] 
        else:
            continue
        
def fix_column(board, col):
    try:
        counter = 0
        for i in range(9):
            counter = counter + 1
            
            for j in range(9):
                if counter < 9:
                    if column_similarity(board, j, i) == None:
                        continue
                        

                    elif column_similarity(board, j, i)[2] == False:
                        
                        column_similarity(board, j, i) = (board, col, row)

                        #randomizer = rn.choice([x for x in range(0, 9) if x != j]) #randomize the list cell
                        
                        #temp = board[i][randomizer] #integer for the randomized list cell
                        
                        #board[i][randomizer] = board[i][j]
                        
                        #board[i][j] = temp

                    else:
                        continue 
                else:
                    randomizer = rn.choice([x for x in range(0, 9) if x != j]) #randomize the list cell
                    
                    temp = board[9][randomizer] #integer for the randomized list cell
                    
                    board[9][randomizer] = board[9][j]
                    
                    board[9][j] = temp
        return board
                    
    except IndexError as e:
        print (board)
        
        
        
        
column_checker(board)
#column = 5
#col = column - 1
#print (get_col(board,col))
    