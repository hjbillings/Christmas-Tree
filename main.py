#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 23:22:57 2020

@author: hanabillings
"""

import os
import threading
import random
import time

mutex = threading.Lock()
tree = list(open("tree.txt").read().rstrip())

class lightColours:
        blank = '\033[0m'
        blue = '\033[94m'
        green = '\033[92m'
        red = '\033[91m'
        yellow = '\033[93m'

def lighting_colour(colour):
    if colour == 'red':
        return f"{lightColours.red}0{lightColours.blank}"
    if colour == 'green':
        return f"{lightColours.green}0{lightColours.blank}"
    if colour == 'blue':
        return f"{lightColours.blue}0{lightColours.blank}"
    if colour == 'yellow':
        return f"{lightColours.yellow}0{lightColours.blank}"

def lighting_sequence(colour, index, off = True):
    while True:
        for i in index:
            tree[i] = lighting_colour(colour) if off else '0'
        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        mutex.release()

        off = not off

        time.sleep(random.uniform(0.5, 2))


yellow = []
red = []
green = []
blue = []

for i, j in enumerate(tree):
    if j == '*':
        yellow.append(i)
        tree[i] = '*'
for i, j in enumerate(tree):
    if j == 'Y':
        yellow.append(i)
        tree[i] = '0'
    if j == 'R':
        red.append(i)
        tree[i] = '0'
    if j == 'B':
        blue.append(i)
        tree[i] = '0'
    if j == 'G':
        green.append(i)
        tree[i] = '0'

# initialise and run the threads :

yellowThread = threading.Thread(target=lighting_sequence, args=('yellow', yellow))

redThread = threading.Thread(target=lighting_sequence, args=('red', red))

greenThread = threading.Thread(target=lighting_sequence, args=('green', green))

blueThread = threading.Thread(target=lighting_sequence, args=('blue', blue))


for thread in [yellowThread, redThread, greenThread, blueThread]:
    thread.start()
for thread in [yellowThread, redThread, greenThread, blueThread]:
    thread.join()

