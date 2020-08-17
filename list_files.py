"""
CP1404 2020 - Practical 3
Student Name: Amy Robinson
Program - List Files
"""

import os

print("The files and folders in {} are: ".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
