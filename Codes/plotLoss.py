import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.font_manager import FontProperties
import csv

'''读取csv文件'''
def readcsv(files):
    csvfile = open(files, 'r')
    plots = csv.reader(csvfile, delimiter=',')
    x = []
    y = []
    z = []
    for row in plots:
        y.append(int(row[1]))
        x.append((row[0]))
        z.append((row[2]))
    return x, y, z


plt.figure()

x, y,z = readcsv("g_loss.csv")
print(x[0:10])
print(y[0:10])
print(z[0:10])
plt.plot(y[1:-1],z[1:-1], 'g', label='Without BN')
plt.show()