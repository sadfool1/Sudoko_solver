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
        
        #for row in range(len(self.board)):
        #    self.board[row] = self.board.row
        #    for col in range(len(self.board)):
        #        self.board.col = self.board[row][col]
    
        for i in range(len(self.board)):
            print (self.row)
            
        self.difficulty = None
        
    
    def row(self,board, row):
        
        for row in range(len(self.board)):
            self.board[row] = self.board.row
            
        
        
        
board_creation()
"""   
if __name__ == '__main__':
    try:
        board_creation() #run the class
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    
        
 """       
        