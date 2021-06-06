#-*-coding:utf-8-*-
import re
import matplotlib.pyplot as plt

file_handle=open('08_31.txt',mode='r')
contents=file_handle.readlines()
aucs=[]
aucs_x=[]
aucs_y=[]
for content in contents:
    auc = re.findall('##### optimal result and model = dataset = hajj, loss file = ../history/psnrs/hajj_2008312115/model.ckpt-(.*?), auc = (.*?) ', content)
    if len(auc) == 0:
        continue
    key={"x":int(auc[0][0]),"y":float(auc[0][1])}
    aucs.append(key)
a=sorted(aucs,key=lambda keys:keys["x"])
for i in range(len(a)):
    aucs_x.append(a[i]['x'])
    aucs_y.append(a[i]["y"])
file_handle.close()

file_handle=open('../../hajj_small.txt',mode='r')
contents=file_handle.readlines()
aucs_small=[]
aucs_x_small=[]
aucs_y_small=[]
for content in contents:
    content = content.split('\n')
    pattern = re.compile(r'dataset = hajj, loss file = ../history/psnrs/hajj_2009020143/model.ckpt-(.*?), auc = (\d+(\.\d+)?)')
    auc = pattern.findall(content[0])
    if len(auc) == 0:
        continue
    key={"x":int(auc[0][0]),"y":float(auc[0][1])}
    aucs_small.append(key)
a=sorted(aucs_small,key=lambda keys:keys["x"])
for i in range(len(a)):
    aucs_x_small.append(a[i]['x'])
    aucs_y_small.append(a[i]["y"])
file_handle.close()
import random
print(aucs_y_small[580],aucs_y_small[585],aucs_y_small[587],aucs_y_small[589])


plt.title("Abnormal Behavior AUC Curve")
plt.xlabel("iterations")
plt.ylabel("Auc value")
plt.plot(aucs_x[1:-1:2], aucs_y[1:-1:2],ls='-',lw=2.2,color='blue',alpha=0.5)
plt.plot(aucs_x_small[1:-1:2], aucs_y_small[1:-1:2],ls='--',lw=2.2,c='g',alpha=0.8,label='quantity')
plt.legend(labels=['large dataset','small dataset'],loc='best')
plt.savefig('./haha.jpg')
plt.show()

