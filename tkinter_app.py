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

class GAME_CONTROLLER():
    
    def __init__ (self):
        
        self.root = Tk()
        self.root.grid()
        self.root.title("Sudoko")
        self.root.geometry = ("700x700")
        self.root.resizable = (True, True)
        
        
if __name__ == '__main__':
    try:
        GAME_CONTROLLER() #run the class
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
