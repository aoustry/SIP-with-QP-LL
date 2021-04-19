# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:07:40 2021

@author: aoust
"""
import matplotlib.pyplot as plt

def plot_convergence_single(name):
    
    file = open("epsilon/"+name+".txt")
    array = []
    for line in file.readlines():
        array.append(float(line))
        
    plt.plot(array)
    plt.yscale('log')
    plt.title(name +", convergence of the feasibility error.")
    plt.xlabel("Iterations")
    plt.yscale(r'Feasibility error $\epsilon_k$')
    plt.savefig("plots/"+name+".png")
    