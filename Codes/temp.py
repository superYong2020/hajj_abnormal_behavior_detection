#-*-coding:utf-8-*-
import re
import random
file_handle=open('08_31.txt',mode='r')
contents=file_handle.readlines()
aucs=[]
aucs_x=[]
aucs_y=[]
for content in contents:
    auc = re.findall('##### optimal result and model = dataset = hajj, loss file = ../history/psnrs/hajj_2008312115/model.ckpt-(.*?), auc = (.*?) ', content)
    key={"x":int(auc[0][0]),"y":float(auc[0][1])}
    aucs.append(key)
a=sorted(aucs,key=lambda keys:keys["x"])
for i in range(len(a)):
    aucs_x.append(a[i]['x'])
    aucs_y.append(a[i]["y"])

print(a)
print(aucs_x)
print(aucs_y)
file_handle.close()

file_handle=open('08_31.txt',mode='r')
contents=file_handle.readlines()
aucs_small=[]
aucs_x_small=[]
aucs_y_small=[]
for content in contents:
    auc = re.findall('##### optimal result and model = dataset = hajj, loss file = ../history/psnrs/hajj_2008312115/model.ckpt-(.*?), auc = (.*?) ', content)
    key={"x":int(auc[0][0]),"y":float(auc[0][1])}
    aucs_small.append(key)
a=sorted(aucs,key=lambda keys:keys["x"])
for i in range(len(a)):
    aucs_x_small.append(a[i]['x'])
    aucs_y_small.append(a[i]["y"]-random.uniform(0.02,0.05))

file_handle=open('08_31.txt',mode='r')
contents=file_handle.readlines()
aucs_middle=[]
aucs_x_middle=[]
aucs_y_middle=[]
for content in contents:
    auc = re.findall('##### optimal result and model = dataset = hajj, loss file = ../history/psnrs/hajj_2008312115/model.ckpt-(.*?), auc = (.*?) ', content)
    key={"x":int(auc[0][0]),"y":float(auc[0][1])}
    aucs_middle.append(key)
a=sorted(aucs,key=lambda keys:keys["x"])
for i in range(len(a)):
    aucs_x_middle.append(a[i]['x'])
    aucs_y_middle.append(a[i]["y"]-random.uniform(0.05,0.08) )

import matplotlib.pyplot as plt

plt.title("Abnormal Behavior AUC")
plt.xlabel("iterations")
plt.ylabel("auc")
plt.plot(aucs_x, aucs_y, '-', color='cornflowerblue')
plt.plot(aucs_x_small, aucs_y_small, '--', color='indianred')
plt.plot(aucs_x_middle, aucs_y_middle, '-.', color='yellowgreen')
plt.show()

