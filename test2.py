#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:24:42 2020

@author: jameselijah
"""
import random
temporary_row = [3,2,4,1,5,6,7,8,9]
j = 2 #number 4 in temporary_row


for TARGET in range(len(temporary_row)):
    if temporary_row[TARGET] == j:
        random_number = random.randint(j+1, 8)
        temp = temporary_row[random_number]
        temporary_row[random_number] = temporary_row[TARGET]
        temporary_row[TARGET] = temp

print (temporary_row)

        