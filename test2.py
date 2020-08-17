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

        
    def __init__ (self):
        
        board = [
                [1,3,2,4,5,6,7,8,9],
                [2,1,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,6,5,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]
                ]
        self.board = board
        self.difficulty = None
        
        print (self.column_similarity(0,0))
        
        
    
    def row(self, row):
        for ROW in range(len(self.board)):
            return self.board[row]
            
    def col(self, col):
        """
        INPUT: BOARD & TARGET COLUMN
        OUTPUT: RETURN the column
        """
        column = []
        for i in range(9):
            temp = self.board[i][col]
            column.append(temp)
        return column
    
    def column_similarity (self, row, col):
        """
        want to check if that exact column has other numbers similar to it.
        POSSIBLE OUTPUT: 
            1. None --> that number has no similar numbers in that column
            2. [i, col, False] --> i, col will tell us where that exact coordinate of similarity in first encounter
        """
        my_number = self.board[row][col]
        
        for i in range (9):
            if (i,col) == (row,col):
                continue
            elif self.board[i][col] == my_number:
                return [i, col, False] 
            else:
                continue
    
board_creation()
"""   
if __name__ == '__main__':
    try:
        board_creation() #run the class
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    
        
 """       
        