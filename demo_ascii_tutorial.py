#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:58:46 2020

@author: steve276
"""

fin = open( "DemoASCIIFile.txt", "r")
lines = fin.readlines()
fin.close()
Data = [0]*len(lines)
for lidx in range(len(lines)):
    Data[lidx] = lines[lidx].split("\t")
    Data[lidx] = lines[lidx].strip().split("\t")
    Data[lidx][0] = int(Data[lidx][0])
    Data[lidx][5] = int(Data[lidx][5])     
    Data[lidx][3:5] = map(float,Data[lidx][3:5])



fin = open( "2008Male00006.txt", "r")
lines = fin.readlines()
fin.close()
Data = [0]*len(lines)
for lidx in range(len(lines)):              # range(len(lines)) -> range(0,16)
#    Data[lidx] = lines[lidx].split(",")
    Data[lidx] = lines[lidx].strip().split(",")   # not " \, "
#    Data[lidx][3] = int(Data[lidx][3])
#    Data[lidx][4:6] = map(float,Data[lidx][4:6])
#    Data[lidx][4:6] = map(float,Data[lidx][4:6])
#   Data[lidx][8:15] = map(float,Data[lidx][8:15])
    
for lidz in range([1,5,6:8])):
#      Data[lidx][3] = int(Data[lidx][3])
      Data[1][4:6] = list(map(float,Data[1][4:6]))
#      Data[lidx][8:15] = map(float,Data[lidx][8:15])  
    
    
    
fin = open( "sample.txt", "r")
lines = fin.readlines()
fin.close()
Data = [0]*len(lines)
for lidx in range(len(lines)):
    Data[lidx] = lines[lidx].strip().split(",")    
    
fin = open( "2008Male00006.txt", "r")
lines = fin.readlines()
fin.close()
Data = [0]*len(lines)
for lidx in range(len(lines)):              # range(len(lines)) -> range(0,16)
#    Data[lidx] = lines[lidx].split(",")
    Data[lidx] = lines[lidx].strip().split(",")   # not " \, "
#    Data[lidx][3] = int(Data[lidx][3])
#    Data[lidx][4:6] = map(float,Data[lidx][4:6])
#    Data[lidx][4:6] = map(float,Data[lidx][4:6])
#   Data[lidx][8:15] = map(float,Data[lidx][8:15])
    
for lidx in range(1,len(Data[1:15])):    #this works for one line (line 2)
#      Data[lidx][3] = int(Data[lidx][3])
    Data[2][3] = int(Data[lidx][3])
    Data[2][4:6] = list(map(float,Data[2][4:6]))
    Data[2][8:15] = list(map(float,Data[2][8:15])) 
    
    
    
    
fin = open( "2008Male00006.txt", "r")
lines = fin.readlines()
fin.close()
Data = [0]*len(lines)
for lidx in range(len(lines)):              # range(len(lines)) -> range(0,16)
    Data[lidx] = lines[lidx].strip().split(",")   # not " \, "


for lidx in range(1,len(lines[1:16])):    #this works for all data lines
    Data[lidx][3] = int(Data[lidx][3])
    Data[lidx][4:6] = map(float,Data[lidx][4:6])
    Data[lidx][8:15] = map(float,Data[lidx][8:15])
    
#print(type(Data[6][6]))
#print(type(Data[6][4]))
#print(type(Data[6][3]))
    
#bad way to make tuples of headers and data
zipData = zip(Data[0],Data[1],Data[2],Data[3],    # creates list of tuples
          Data[4],Data[5],Data[6],Data[7],
          Data[8],Data[9],Data[10],Data[11],
          Data[12],Data[13],Data[14])

#list(zipData)

zipData = list(zipData)     #still a list of tuples

#lol = [list(ele) for ele in zipData]  #makes list of lists from list of tuples
#lol2 = [tuple(ele) for ele in zipData] # makes list of tuples again

Dict1 = {ele[0]: ele[1:] for ele in zipData}

#Dict1              # prints dictionary

##for key, value in Dict1.items():
#    print(key, ':' ,value)
#or
#for key in Dict1:
#    print(key, ':' ,Dict1[key]) 
    
Dict1.update({'End State' : tuple(Data[15])})
Dict1.update({'Distance' : tuple(['pass'])})

#Dict1.get(' X')

#dictionary created, moving on to create additional data

import statistics
import math

x_avg = statistics.mean(Dict1.get(' X'))
y_avg = statistics.mean(Dict1.get(' Y'))
energy_avg = statistics.mean(Dict1.get('Energy Level'))

def distance(x1,y1,x2,y2):
    dx = (x2-x1)**2
    dy = (y2-y1)**2
    sumdxdy = dx + dy
    result = math.sqrt(sumdxdy)
    return result

print(x_avg)
print(y_avg)
print(energy_avg)
print(distance(1,0,4,0))

#writing to a new file

#o = open("Georges_life.txt", "x") # make new file
#o.close()

o = open("Georges_life.txt", "a")   # a for ammend, w for write over, x for new

o.write('Raccoon name: George\nAverage location: 591189.034454322, 4504604.085012093\nDistance traveled: <sum of distances>\nAverage energy level: 563.6214285714285\nRaccoon end state: George number 6 died from starvation\n')
#heading, change to add values from file(I think by file it can be original george file)
o.close()

list(zip(*(zipData)))   # unzips list of tuples (of same data type) created from Data
#but we're only to include certain keys from dictionary so this is no good

table_body = list(zip(*((Dict1.get('Day')),(Dict1.get('Time')),(Dict1.get(' X')),
           (Dict1.get(' Y')),(Dict1.get(' Asleep')),(Dict1.get('Behavior Mode')))))
#does not include headers
#to include: Date, Time, X and Y coordinates, the Asleep flag, the behavior mode, and the distance traveled (in that order).


[*Dict1.keys()]   #returns list of keys in the dictionary (list of headers)
#but i want certain keys

#o.write(" ".join(Dict1.keys()))
#writes all keys, but only a some are needed

key_list = [*Dict1.keys()]      #returns relevant list of keys in the dictionary
del key_list[0]
del key_list[2]
del key_list[6:14]

#print(key_list)

o = open("Georges_life.txt", "a")
o.write("\n")
o.write(str(key_list))
o.write("\n")
o.write(str(table_body))

o.close()


    
    