# !/bin/python3

'''
Python3 script to add one year to the Created date of the all the files in the argument directory.
Usage: python3 main.py <directory>
'''

import os
import sys
import time
from subprocess import call


def add_year(file):
    '''
    Adds one year to the Created date of the argument file
    '''
    # Get the file's creation date
    stat = os.stat(file)
    created = stat.st_birthtime

    # Add one year to the creation date
    created += 31536000

    # Format the date to MM/DD/YYYY
    date = time.strftime('%m/%d/%Y', time.localtime(created))
    t = time.strftime('%H:%M:%S', time.localtime(created))

    # Example: command = 'SetFile -d ' + '"05/06/2019 ' + '22:44:33"' + file
    # Log date
    command = 'SetFile -d ' + '"' + date + ' ' + t + '"' + ' ' + file
    call(command, shell=True)


def add_year_to_all_files():
    '''
    Adds one year to the Created date of all files in the argument directory
    '''
    # Get the directory
    directory = sys.argv[1]

    # Get all files in the directory
    files = os.listdir(directory)

    # Add one year to the Created date of each file
    for file in files:
        add_year(file)


if __name__ == '__main__':
    add_year_to_all_files()
