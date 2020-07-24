#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:24:42 2020

@author: jameselijah
"""
import random as rn

for j in range (9):
    randomizer = rn.choice([x for x in range(0, 9) if x != j])

print (randomizer)