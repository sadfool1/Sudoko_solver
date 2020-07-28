#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:12:32 2020

@author: jameselijah
"""

import numpy as np
import random as rn
import math

#INITITLIAZE BOARD
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
    """
    INPUT: BOARD & TARGET COLUMN
    OUTPUT: RETURN the column
    """
    column = []
    for i in range(9):
        temp = board[i][col]
        column.append(temp)
    return column


def column_checker(board):
    """
    INPUT: BOARD
    OUTPUT: NONE, but main function is to fascilate the board column
    ==> constantly checking if the column is
    """
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

            
def column_similarity (board, row, col):
    """
    want to check if that exact column has other numbers similar to it.
    POSSIBLE OUTPUT: 
        1. None --> that number has no similar numbers in that column
        2. [i, col, False] --> i, col will tell us where that exact coordinate of similarity in first encounter
    """
    my_number = board[row][col]
    
    for i in range (9):
        if (i,col) == (row,col):
            continue
        elif board[i][col] == my_number:
            return [i, col, False] 
        else:
            continue
        
def fix_column(board, col):
    
    """
    INPUT: BOARD & target column
    OUTPUT: FIXED BOARD & playable game
    """
    
    counter = 0
    for i in range(9):
        counter = counter + 1
        
        for j in range(8):
            if counter < 9:
                if column_similarity(board, i, j) == None:
                    continue
                    

                elif column_similarity(board, i, j)[2] == False:
                    
                    temporary_row = board[i]

                    
                    for TARGET in range(len(temporary_row)):
                        if temporary_row[TARGET] == temporary_row[j]:
                            random_number = rn.randint(j+1, 8)
                            temp = temporary_row[random_number]
                            temporary_row[random_number] = temporary_row[TARGET]
                            temporary_row[TARGET] = temp

                else:
                    continue 
            else:
                if column_similarity(board, i, j) == None:
                    continue
                    

                elif column_similarity(board, i, j)[2] == False:
                    
                    temporary_row = board[i]

                    
                    for TARGET in range(len(temporary_row)):
                        if temporary_row[TARGET] == temporary_row[j]:
                            random_number = rn.randint(j+1, 8)
                            temp = temporary_row[random_number]
                            temporary_row[random_number] = temporary_row[TARGET]
                            temporary_row[TARGET] = temp

                
    return board

        
        
        
        
column_checker(board)
#column = 5
#col = column - 1
#print (get_col(board,col))
    