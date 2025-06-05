#coding=utf-8
import os, sys, platform

# Define a flag or use a file to track whether the update has been done
update_flag = "update_done.txt"

if not os.path.exists(update_flag):
    print('\033[1;32mPRINCE THE NOOBER')
    os.system('rm -rf Sarfraz.so')
    os.system('clear')
    print('\033[1;32mDOWNLOADING SSB\n')
    os.system('clear')

    try:
        if sys.argv[1] == 'update':
            os.system('rm -rf Sarfraz.so')
    except:
        pass

    bit = platform.architecture()[0]

    if bit == '64bit':
        if not os.path.isfile('Sarfraz.so'):
            os.system('curl -L https://github.com/SSB-143/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 
            os.system('clear')
            print('\n\033[1;34mCracking \033[1;33mSSB \033[1;31mSequrity.......\n\n\n')
            print('\033[1;32mDONE ENJOY :)')

    # Create the update flag file to indicate that the update has been done
    open(update_flag, 'w').close()

import Sarfraz
Sarfraz.random_number2()
