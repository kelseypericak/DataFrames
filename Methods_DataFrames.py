# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:16:28 2019

@author: kpericak

Cosmetics example: Marc Jacobs lip makeup on Sephora, extracted from site Aug '19

"""

#Different ways to create a dataframe for data analysis 

##Import modules
import pandas as pd 
from tabulate import tabulate

##Method 1: List
print ('Method 1: List input')

listInput = [['Marc Jacobs Beauty', 'Le Marc Lip Crème Lipstick', 42, 'stick', 'single', 34],  
         ['Marc Jacobs Beauty', 'New Nudes Sheer Gel Lipstick', 42, 'stick', 'single', 9],  
         ['Marc Jacobs Beauty', 'Le Marc Lip Frost', 42, 'stick', 'single', 9], 
         ['Marc Jacobs Beauty', 'Le marc Liquid Lip Crayon', 34, 'crayon', 'single', 9],                 
         ['Marc Jacobs Beauty', 'Make Your Le Marc 3 Piece Mini Liquid Lip Crayon Set', 33,
          'crayon', 'set', 1],                 
         ['Marc Jacobs Beauty', 'Kiss Pop Lipstick', 35, 'stick', 'single', 8],                 
         ['Marc Jacobs Beauty', 'Somewhere, Anywhere - Le Marc Liquid Lip Crayon Collection',
          78, 'crayon', 'set', 1],                 
         ['Marc Jacobs Beauty', 'Le Marc Liquid Lip Crème', 38, 'gloss', 'single', 5],                 
         ['Marc Jacobs Beauty', 'The Sex Kitten Limited-Edition Set', 26, 'gloss','set', 1],
         ['Marc Jacobs Beauty', 'Le Marc Jajobs Lip Crème Lipstick in True', 42, 'stick', 
          'single', 1],
         ['Marc Jacobs Beauty', 'Fashion Collection Le Marc Lip Crème', 38, 'stick', 'single', 1],
         ['Marc Jacobs Beauty', 'Collector\'s Edition Le Marc Lip Créme Lipstick - Blacquer', 40, 
          'stick', 'single', 1],
         ]    

headers = ['Brand', 'Name', 'Price', 'Type', 'Item', 'ColourOptions']

print('\nThe list we are inputting looks like this, with the followings headers: ' + str(headers) + '.\n')
print(listInput)

df_fromList = pd.DataFrame(list(listInput))     #create dataframe
df_fromList.columns = headers
pd.set_option('max_colwidth', 800)              #set a max width if the Name is not showing fully

print('\nThe dataframe will look like this using pd.DataFrame(list(listInput)): \n')
print(tabulate(df_fromList, df_fromList.head(), showindex = False)) #print the table using tabulate

df = df_fromList #main dataframe to use to create different data structures in future exmpales



##Method 2: Dictionary
print ('\nMethod 2: Dictionary input')

dictionary = df.to_dict()   #assume this was your initial input
                            #putting a dataframe to a dictionary

print('\nThe dictionary we are using looks like this: \n')
print(dictionary)

df_fromDict = pd.DataFrame(dictionary)
print('\nA dataframe can become a dictionary by writing df.to_dict(). The dataframe will look like this using pd.DataFrame(dictionary): \n')
print(tabulate(df_fromDict, headers = 'keys', showindex = False)) #use the keys for the headers



##Method 3: Unioned lists
print ('\nMethod 3: Unioned list input')

union_list = [] #converting a dataframe into many lists
columns = list(df) #list of the column names
for column in columns:
    union_list.append(df[column].tolist())  #assume this was your initial input

print('\nThe union of lists looks like this: \n')
print(union_list)                           #assume this is initial input

zipped_list = list(zip(*union_list))

df_fromUnionZip = pd.DataFrame(list(zipped_list)) 
headers = ['Brand', 'Name', 'Price', 'Type', 'Item', 'ColourOptions']
print('\nThe dataframe will look like this using pd.DataFrame(list(zipped_list)) after\
 manipulating the data structure: \n')
print(tabulate(df_fromUnionZip, headers, showindex = False)) #Print the table using tabulate


##Method 4: SQL

print ('\nMethod 4: SQL query input')

print('\nWrite the query and assign it to a name then read the query and place it into a \
table. No output will be printed for this method so please refer to the code only.')
query = '''SELECT * FROM DB.TABLE_A;'''
table = pd.read_sql_query(query, conn) #make sure to set up your connection to a database first
df = pd.DataFrame(table) 


    
    


    

    
    



    


    



