import imp
import os
import shutil
import time
import imp
path = str(input("Enter the directory"))
days = float(input("Enter the number of days"))
days = time.time()
if os.path.exists(path):
    files = os.walk(path)
    oldTime = os.path.join(path+'/'+files)
    newTime = os.stat(path).st_ctime
    if oldTime > newTime:
        os.remove(path)
    else:
        shutil.rmtree()
else:
    print("The file doesn't exist")
