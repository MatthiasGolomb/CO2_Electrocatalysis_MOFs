#!/usr/bin/env python

from ase.io import read
import os
import sys

for folder in os.listdir('./'):
    if os.path.isdir('./{folder}'.format(folder=folder)):
            with open('./{folder}/aims_craynov21.out'.format(folder=folder), 'r') as f:
                lines = f.readlines()
    #            print(lines[-2])
                if 'Have a nice day' in lines[-2] or 'Have a nice day' in lines[-3]:
                    print('Success ', folder)
    #                struct_result = read('./temp/{folder}/{subfolder}/aims_craynov21.out'.format(folder=folder, subfolder=subfolder))
    #                print(folder, struct_result.get_total_energy(), '{subfolder}'.format(subfolder=subfolder))
                else:
                    print('Fail ', folder)

