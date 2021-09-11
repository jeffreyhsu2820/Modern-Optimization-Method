#!/usr/bin/env python
# coding: utf-8

# In[172]:


import random

def objective_function(x):
    return -x**5+5*x*3+20*x-5

# x is a vector
def maximum(x, objective_function):
    value={}
    for v in x:
        if objective_function(v):
            value[v]=objective_function(v)
    return list(value.keys())[list(value.values()).index(max(value.values()))]

# x the position before iteration
# V the velocities before iteration
# P the local best position 
# Pg the global best position
def velocities(swarm_size, x,V, w,c1,c2,r1,r2,Pg,P):
    V_new=[]
    for i in range(swarm_size):
        V_new.append(w*V[i]+c1*r1*(P[i]-x[i])+c2*r2*(Pg-x[i]))
    return V_new

def main(swarm_size, x, V0, w, c1, c2, r1, r2, objective_function, velocities, maximum):
    i=0
    V=V0
    P=[objective_function(i) for i in x]
    Pg=maximum(P, objective_function)
    while i<20:
        v=velocities(swarm_size, x,V, w,c1,c2,r1,r2,Pg,P)
        new_x=[v[p]+x[p] for p in range(swarm_size)]
        for n in range(swarm_size):                               # if the new point x is not in the range we first defined, we will random choose a point in the range
            if new_x[n] >Range[1] or new_x[n]<Range[0]:             
                new_x[n]=random.randrange(Range[0],Range[1]+1)
        if len(set(new_x))==1:
            return new_x, objective_function(new_x[0])
        for p in range(swarm_size):
            if objective_function(new_x[p])>objective_function(x[p]):
                P[p]=new_x[p]
        Pg=maximum(P, objective_function)
        x=new_x
        i+=1
        print(i)
    return x, [objective_function(i) for i in x]

swarm_size=4
Range=[-4,4]
c1,c2,w=1,1,1
r1,r2=0.12, 0.81                         # random.random(),random.random()  
V0=[0,0,0,0]                             # the initial velocities
x=[-2, 0, 1, 3]                          # the given initial position for question 2

main(swarm_size, x, V0, w, c1, c2, r1, r2, objective_function, velocities, maximum)

