from io import open
import os
import subprocess

file = open("ejemplo.dla", "r")
fileact = file.read()

print(fileact)
file.close()

fname = "fCodeCache1.py"

if not os.path.exists(fname):
    tfile = open(fname, "w")
    tfile.write(" print('Hola mundo') ")

    subprocess.call(["python", fname])
else:
    file_number = int(fname[10:11])
    num = file_number + 1
    fname = "fCodeCache" + str(num) + ".py"
    tfile = open(fname, "w")
    tfile.write(" print('Hola mundo') ")

    subprocess.call(["python", fname])

tfile.close()
