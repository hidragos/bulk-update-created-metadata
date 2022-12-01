# !/bin/python3

'''
Python3 script to add one year to the Created date of the all the files in the argument directory.
Usage: python3 main.py <directory>
'''

import os
import sys
import time as timeUtil
from subprocess import call


def add_year(file):
    '''
    Adds one year to the Created date of the argument file
    '''
    # Get the file's creation date
    stat = os.stat(file)
    date_created = stat.st_birthtime

    # Add one year to the creation date
    date_updated = date_created + 31536000

    # Format the date to MM/DD/YYYY
    date = timeUtil.strftime('%m/%d/%Y', timeUtil.localtime(date_updated))
    time = timeUtil.strftime('%H:%M:%S', timeUtil.localtime(date_created))

    # Log date
    command = 'SetFile -d ' + '"' + date + \
        ' ' + time + '"' + ' ' + file
    call(command, shell=True)


def add_year_to_all_files(directory):
    '''
    Adds one year to the Created date of all files in the argument directory
    '''
    # Get the directory

    # Get all files in the directory
    files = os.listdir(directory)

    # Add one year to the Created date of each file
    for file in files:
        add_year(file)


def prompt_user():
    '''
    Prompts the user to confirm the operation
    '''
    print('This script will add one year to the Created date of all files in the argument directory.')
    print('Are you sure you want to continue? (y/n)')
    response = input()
    if response == 'y':
        return True
    else:
        return False


if __name__ == '__main__':
    is_sure = prompt_user()
    if is_sure is False:
        sys.exit()

    directory = sys.argv[1]
    add_year_to_all_files(directory=directory)
