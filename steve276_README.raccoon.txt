"""
Created on Fri Feb  7 10:02:14 2020
MiriamStevens
@author: steve276

ABE65100 - Lab 03 - Metadata File

This is the metadata file for the script, "steve276_Evaluate_Raccoon_Life.py".

"""

inputs:
    dataset: "2008Male00006.txt"

output:
    dataset: "Georges_life.txt"



Python was used to read data on a raccoon's activity from the .txt file
 "2008Male00006.txt".


The script processes the data as follows:

 - Parses the .txt data into a list of lists and converts numbers to correct
   object types (int and float).
   
 - Zips the lists of different data types into a list of tuples, with each 
   tuple containing the same type of data. The last line of data is excluded.
   
 - A dictionary is created using the first tuple as keys and the remaining
   tuples as values. The keys and values are tied based on their index in the
   tuple. The original last line of data is appended.
   
 - An average of the raccoon's positional coordinates is computed from values 
   in the dictionary.
 
 - A new text file called "Georges_life.txt" is written. It contains a header 
   block of summary statistics on the raccoon's life and selected data from the
   dictionary created in the script.

