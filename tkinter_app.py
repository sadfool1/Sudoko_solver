#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:25:12 2020

@author: jameselijah
"""

import sys
import traceback
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randint
import random
from tkinter import *
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D #imports the 3D 
import time
from tkinter import TclError
import os

class GAME_CONTROLLER():
    
    def __init__ (self):
        
        self.root = Tk()
        self.root.grid()
        self.root.title("Sudoko")
        self.root.geometry = ("700x700")
        self.root.resizable = (True, True)
        
        self.controlframe = LabelFrame(self.root, text = "Menu")
        self.controlframe.grid(row = 1, column = 0) 

        self.sudokuframe = LabelFrame(self.root, text = "Board")
        self.sudokuframe.grid(row = 0, column = 0) 
        
        BOARD_CREATION = os.path.dirname(__file__)
        FILE_NAME = "object-oriented-sudoku.py"
        result = os.path.join(BOARD_CREATION, FILE_NAME)
        
        print (exec(result))
        
        #user_r_entry = IntVar()
        
        """for i in range(10):
            for j in range(10):
                NUMBER_ENTRY = Entry(self.sudokuframe, 
                                     textvariable = user_r_entry).grid(row = 1, 
                                                                column = 0)"""
        
        
        
if __name__ == '__main__':
    try:
        GAME_CONTROLLER() #run the class
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
