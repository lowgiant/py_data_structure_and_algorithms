# -*- coding: utf-8 -*- 

import os 
import sys
import shutil

def change_file_ext():
    if len(sys.argv) <2:
        print("Usage: python {0} filename.old_ext 'nex_ext".format(sys.argv[0]))
        sys.exit()
    name = os.path.splitext(sys.argv[1])[0] +"." +sys.argv[2]

    print(name)

    try:
        shutil.copyfile(sys.argv[1],name)
    except OSError as err:
        print(err)


change_def = change_file_ext()

print(change_def)