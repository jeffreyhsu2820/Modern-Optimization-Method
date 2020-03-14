#!/usr/bin/env python
# coding: utf-8

# In[348]:


import random
import statistics
import math
import copy


# In[349]:


def target_function(x):   #we change maximize into minimize problem
    return 1/(1+500*x[0]+300*x[1]+200*x[2]+math.sqrt(22500*(x[0]**2)+ 10000*(x[1]**2)+ 2500*(x[2]**2)))


# In[350]:


def constraint(x):
    y1=4*x[0]+ 4*x[1]+ 8*x[2]-1720+1.645*(math.sqrt(16*(x[0]**2)+(x[1]**2)+ 9*(x[2]**2)+ 29584))
    y2=4*x[1]+ 16*x[2]-1680+1.645*math.sqrt(4*(x[1]**2)+ 16*(x[2]**2)+ 112896)
    y3=8*x[0]+ 12*x[1]-1840+1.645*math.sqrt(4*(x[0]**2)+ 4*(x[1]**2)+ 76176)
    return y1, y2, y3


# In[351]:


def design_pool(population,var_num, scope, constraint):
    initial=[]
    termination=False
    while termination==False:
        p=[int(scope*random.random()) for _ in range(var_num)]
        if len([x for x in list(constraint(p)) if x<=0])==var_num:  #要確認有沒有符合constraint的條件，三條都要對
            initial.append(p)
        if len(initial)==population:
            termination=True
    return initial


# In[352]:


def new_point_generator(R, point,constraint,var_num):
        #產生新的點，透過初始設定的區間
    terminate=False                                  #產生初始的點
    while terminate==False:
        p=[]
        for i in point:
            stop=False
            while stop==False:
                x=int(random.uniform(i+R[0],i+R[1]))
                if x>=0:
                    p.append(x)
                    break
        if len([x for x in list(constraint(p)) if x<=0])==var_num:
            new_point=p
            terminate=True
    delta_t=target_function(new_point)-target_function(point)  #first point的溫度
    return new_point, delta_t    #產生新的點以及新的點與前一個點的能量差


# In[353]:


def accept_the_point_or_not(new_point, point, boltzmann_constant, delta_temperature, f_bar):
    if delta_temperature>=0:
        prob=math.exp(-delta_temperature/(boltzmann_constant*f_bar))
        r=random.random()
        if prob>r:
            out=new_point
        else:
            out=point
    else:
        out=new_point
    return out


# In[354]:


def main(population,var_num,target_function,constraint,scope,R,boltzmann_constant,c,iteration,converge_criteria):
    f_bar=statistics.mean([target_function(i) for i in design_pool(population,var_num, scope, constraint)]) #T 初始溫度
    terminate=False                                  #產生初始的點
    while terminate==False:
        p=[int(scope*random.random()) for _ in range(var_num)]
        if len([x for x in list(constraint(p)) if x<=0])==var_num:
            point=p
            terminate=True
    count=0
    p=0                  #整個cycle的次數
    i=0                  #iteration次數累積
    termination=False
    while termination==False:
        old_point=point
        newpoint, delta_temperature=new_point_generator(R, old_point,constraint, var_num) #產生(新的點,差距)
        point=accept_the_point_or_not(newpoint, point, boltzmann_constant, delta_temperature, f_bar) #要接受新的點還是用舊的
        i=i+1
        if i>=iteration:
            p=p+1
            i=1
            f_bar=f_bar-(c*f_bar)   #降溫
            if point==old_point:
                count+=1
                if count>=converge_criteria: #檢查有沒有到達穩定狀態=>超過converge_criteria次都是舊的點
                    termination=True
            elif point!=old_point:
                count=0
    return point, (1/target_function(point))-1


# In[ ]:


k1,k2=1,1             #將風險跟利潤看唯一樣重要
population=6          #初始pool的個數
var_num=3             #有幾個變數
# target_function=    向上面定的一樣
# constraint=         向上面定的一樣
scope=430             #變數值的範圍可以從0到幾
R=[-6,6]              #設定尋找的範圍
boltzmann_constant=1  #設定波茲曼常數
c=0.5                 #設定temperaturereductionfactor
iteration=2           #要跌代幾次
converge_criteria=500 #連續幾次都是同一個point


# In[364]:


main(6,3,target_function, constraint, 430, [-6,6], 1, 0.5, 2, 1000)

