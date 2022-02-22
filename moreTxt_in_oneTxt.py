import csv
import glob

files = glob.glob('*.txt')
print(files)
for file in files:
    f = open(file, 'r')
    gg = f.read()
    open('result.txt', 'a').write(gg)
    f.close()
