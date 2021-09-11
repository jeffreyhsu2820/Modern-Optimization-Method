#!/usr/bin/env python
# coding: utf-8

import numpy as np
from numpy.random import randint
from random import gauss, randrange, random, choices, sample  #產生隨機數在[0,1)
import random
import copy


# ## 1.Deciding the initial population pool
#產生有一個基因序列有幾個數字
def individual(number_of_genes, upper_limit, lower_limit):
    individual=[]
    for x in range(number_of_genes):
        individual.append(round(random.random()*(upper_limit-lower_limit)+lower_limit,0)) #round()四捨五入    
    return [int(x)for x in individual]


# ### *The population designed right here can't be switched in the following process


#決定一開始要有幾個population
def population(constraint, equation, num_of_individuals, number_of_genes, upper_limit, lower_limit):
    p=[]
    while len(p) <num_of_individuals:
        tmp=individual(number_of_genes, upper_limit, lower_limit)
        while equation.dot(np.array(tmp).T)<=constraint:
            if tmp not in p:
                p.append(tmp)
                break
            tmp=individual(number_of_genes, upper_limit, lower_limit)
    return p


# ## 2.Caculate the fitness value for each individual


def fitness_value(population):
    return np.array(population).dot(points.T)



def weight_calculation(population):
    weight=[]
    k=fitness_value(population)
    for x in k:
        weight.append(x/k.sum())
    return weight, max(weight), int(np.argwhere(weight==max(weight))[0])


# ## 3. Reproducing operator 
#選最大fitness value的人 剩下的從剩下的pool挑
def selection(population, num_of_selection):
    _, max_score, where=weight_calculation(population)
    pop=population.copy()
    out=[]
    out.append(population[int(where)])
    pop.pop(int(where))
    out+=random.sample(pop, k=num_of_selection-1)
    return out


# ## 4. Mutation operator
#針對做crossover的其中一個string做
def mutation(tmp):
    num=randint(0,number_of_genes-1)
    if tmp[num]==0:
        tmp[num]=1
    else:
        tmp[num]=0
    return tmp


# ## 5. Crossover and mutation process
def crossover_then_mutation(population):
    pop=copy.deepcopy(population)
    tmp=selection(population,2)
    tmp[0][round(number_of_genes/2):], tmp[1][round(number_of_genes/2):]=    tmp[1][round(number_of_genes/2):], tmp[0][round(number_of_genes/2):]
    tmp[0]=mutation(tmp[0])
    for x in tmp:
        if equation.dot(np.array(x).T)<=constraint:
            if [int(y) for y in x] not in pop:   #想要讓pool裡的人distinct
                pop.append(x)
    return pop


# ## 6. Combine all the operator above and set the termination condition
def main(constraint, equation, num_of_individuals, number_of_genes, upper_limit, lower_limit, max_num_generation): 
    pop=population(constraint, equation, num_of_individuals, number_of_genes, upper_limit, lower_limit)
    i=0
    while i <max_num_generation:
        c_score=fitness_value(pop)
        old_max_score=int(max(c_score))
        pop=crossover_then_mutation(pop)
        pop=selection(pop,num_of_individuals)
        i+=1
    tweight=equation.dot(np.array(pop[int(np.argwhere(c_score==max(c_score))[0])]).T)
    return pop[int(np.argwhere(c_score==max(c_score))[0])],max(c_score), tweight

# ## 7. Run it!!
number_of_genes=6
upper_limit=1
lower_limit=0
constraint=30
num_of_individuals=4
# Inputs of the equation.
equation = np.array([15,3,2,5,9,20])
points=np.array([15,7,10,5,8,17])
max_num_generation=200

main(constraint, equation, num_of_individuals, number_of_genes, upper_limit, lower_limit, max_num_generation)

