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
        
        self.column_checker()
        
    
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
    def column_checker(self):
        """
        INPUT: BOARD
        OUTPUT: BOARD. Main function is to fascilate the board column
        ==> constantly checking if the column is
        """
        for i in range(9):
            temp = set(self.col(i))
            
            length_temp = len(temp)
    
            while length_temp < 9:
                
                self.fix_column(i)
                
                length_temp = len(set(self.col(i))) #update the value of length 
                
                if length_temp < 9:
                    continue
                else:
                    break
                
        """
        for i in range(len(self.board)):
            print (self.board[i])
        """
        
        new_copy = board
        
        for i in range(9):
            
            
            
    def fix_column(self, col):
        
        """
        INPUT: BOARD & target column
        OUTPUT: FIXED BOARD & playable game
        """
        
        counter = 0
        for i in range(9):
            counter = counter + 1
            
            for j in range(8):
                if counter < 9:
                    if self.column_similarity(i, j) == None:
                        
                        #this is to show that there is NO similarity, then we just skip it
                        
                        continue
                        
    
                    elif self.column_similarity(i, j)[2] == False:
                        
                        temporary_row = self.board[i]
    
                        
                        for TARGET in range(len(temporary_row)):
                            if temporary_row[TARGET] == temporary_row[j]:
                                random_number = rn.randint(j+1, 8)
                                temp = temporary_row[random_number]
                                temporary_row[random_number] = temporary_row[TARGET]
                                temporary_row[TARGET] = temp
    
                    else:
                        continue 
                else:
                    if self.column_similarity(i, j) == None:
                        continue
                        
    
                    elif self.column_similarity(i, j)[2] == False:
                        
                        temporary_row = self.board[i]
    
                        
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
    
   
        