import os
import shutil
import time

def remove():
    pathname = input("Enter the path of the folder which is to be cleaned :")
    os.path.exists(pathname)
    os.walk(pathname)
    os.path.join(pathname)
    ctime = os.stat(pathname).st_ctime
    os.remove(pathname)

remove()
print("done")