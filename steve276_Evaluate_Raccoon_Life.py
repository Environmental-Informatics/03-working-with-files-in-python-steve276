#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:58:46 2020
Miriam Stevens
@author: steve276

ABE65100 - Lab 03 - Source Code

This program extracts data from "2008Male00006.txt", adds the data to a 
dictionary, and writes a summary of the information to a new .txt file. Kind of.

"""

fin = open( "2008Male00006.txt", "r")
lines = fin.readlines()
fin.close()
Data = [0]*len(lines)
for lidx in range(len(lines)):              
    Data[lidx] = lines[lidx].strip().split(",")   

#converts appropriate data from strings to int or float
for lidx in range(1,len(lines[1:16])):    #range excludes first and last lines
    Data[lidx][3] = int(Data[lidx][3])
    Data[lidx][4:6] = map(float,Data[lidx][4:6])
    Data[lidx][8:15] = map(float,Data[lidx][8:15])
    
#checks whether numbers are converted correctly
#print(type(Data[6][6]))
#print(type(Data[6][4]))
#print(type(Data[6][3]))
    
#converts lists of lists to lists of tuples, unideally
zipData = zip(Data[0],Data[1],Data[2],Data[3],    
          Data[4],Data[5],Data[6],Data[7],
          Data[8],Data[9],Data[10],Data[11],
          Data[12],Data[13],Data[14])

#zipData = list(zipData)     #still a list of tuples
#lol = [list(ele) for ele in zipData]  #makes list of lists from list of tuples
#lol2 = [tuple(ele) for ele in zipData] # makes list of tuples again

Dict1 = {ele[0]: ele[1:] for ele in zipData}  #writes data to a dictionary

#adds last line from original file to dictionary and adds Distance key
Dict1.update({'End State' : tuple(Data[15])})    
Dict1.update({'Distance' : tuple(['pass'])})


import statistics
import math

#computes respetive averages of X and Y values
x_avg = statistics.mean(Dict1.get(' X'))
y_avg = statistics.mean(Dict1.get(' Y'))

energy_avg = statistics.mean(Dict1.get('Energy Level'))  #raccoon's average energy

def distance(x1,y1,x2,y2):
    """Computes distance between two points"""
    dx = (x2-x1)**2
    dy = (y2-y1)**2
    sumdxdy = dx + dy
    result = math.sqrt(sumdxdy)
    return result

#check averages and distance function
#print(x_avg)
#print(y_avg)
#print(energy_avg)
#print(distance(1,0,4,0))
    
#writing to a new file
o = open("Georges_life.txt", "x") # make new file
o.close()

#appending the new file
o = open("Georges_life.txt", "a")
o.write('Raccoon name: George\nAverage location: 591189.034454322, 4504604.085012093\nDistance traveled: <sum of distances>\nAverage energy level: 563.6214285714285\nRaccoon end state: George number 6 died from starvation\n')
o.close()

list(zip(*(zipData)))   # unzips list of tuples (of same data type) created from Data
#but we're only to include certain keys from dictionary so this is no good

table_body = list(zip(*((Dict1.get('Day')),(Dict1.get('Time')),(Dict1.get(' X')),
           (Dict1.get(' Y')),(Dict1.get(' Asleep')),(Dict1.get('Behavior Mode')))))
#does not include headers
#to include: Date, Time, X and Y coordinates, the Asleep flag, the behavior mode, and the distance traveled (in that order).

([*Dict1.keys()])   #returns list of all keys in the dictionary

key_list = [*Dict1.keys()]      #returns list of required dictionary keys 
del key_list[0]
del key_list[2]
del key_list[6:14]

#o.write(" ".join(Dict1.keys()))
#writes all keys, but only a some are needed

#appends the table of selected data to the new .txt file
o = open("Georges_life.txt", "a")
o.write("\n")
o.write(str(key_list))
o.write("\n")
o.write(str(table_body))

o.close()



