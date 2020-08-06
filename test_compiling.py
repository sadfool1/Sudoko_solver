#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:26:25 2020

@author: jameselijah
"""

import numpy as np
import random as rn
import math
import sys
import traceback


class board_creation:
    
    def __init__ (self, board, difficulty):
        
        self.board = [
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
        
        self.difficulty = None
        column_checker(self.board)
        
    def get_col(self, board, col):
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
        OUTPUT: BOARD. Main function is to fascilate the board column
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
                
        for i in range(len(board)):
            print (board[i])
            
            
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
                        
                        #this is to show that there is NO similarity, then we just skip it
                        
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
    
                    
    
    

            
if __name__ == '__main__':
    try:
        board_creation() #run the class
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    
        
        
        