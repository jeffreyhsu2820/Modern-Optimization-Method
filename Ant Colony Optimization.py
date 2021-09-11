#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np

# x是一個 value
def objective_function(x):
    return x**5-5*(x**3)-20*x+5

def the_permissible_values(R,v):
    return [i for i in np.arange(R[0],R[1]+v,v)]

# roulette_wheel_selection operator
def roulette_select(candidate, pheromone, num):
    total_pheromone = sum(pheromone)
    rel_pheromone = [f/total_pheromone for f in pheromone]
    probs = [sum(rel_pheromone[:i+1]) for i in range(len(rel_pheromone))]
    new_population = []
    value_index=[]
    for _ in range(num):
        r = random.random()
        for (i, individual) in enumerate(candidate):
            if r <= probs[i]:
                new_population.append(individual)
                value_index.append(i)
                break
    return new_population, value_index

def best_worst(evaluate_value):
    best=min(evaluate_value)
    count=0
    for i in range(len(evaluate_value)):
        if evaluate_value[i] == best:
            count+=1
            best_index=i
    worst=max(evaluate_value)
    return best, best_index, worst, count

# general form
def main(R, N, n, v, t, p, objective_function, the_permissible_values, best_worst, iteration_max):
    initial=the_permissible_values(R,v)
    pheromone=[ 1 for _ in range(len(initial))]        # set the initial pheromone value
    loop=0
    while loop<2:
        loop+=1
        new, index=roulette_select(initial,pheromone, N)
        xbest, xbest_index, xworst, count = best_worst([objective_function(i) for i in new])
        if len(set(new))==1:
            break
        for i in range(len(initial)):
            pheromone[i]=(1-p)*pheromone[i]
        pheromone[index[xbest_index]]+=(t*count*abs(xbest))/abs(xworst)                
    return xbest, initial[index[xbest_index]]

R=[0,3]                   # the range of x
N=4                       # number of paritcles
n=1                       # design variable
v=0.5                     # the permissible discrete value
t=2                       # the scaling parameter in pheromone
p=0                       # the decay pheromone factor
iteration_max=20          # maximum loop


main(R, N, n, v, t, p, objective_function, the_permissible_values, best_worst, iteration_max)

