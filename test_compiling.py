#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:26:25 2020

@author: jameselijah
"""

import numpy as np
import random as rn
import math


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
        
        
        
        
        
        