# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:24:39 2021

@author: aoust
"""
import os

#Call application 1

for i in range(1,10):
    name = "PSD_random"+str(i)
    os.system("python3 Application1_reformulation.py "+name)
    name = "notPSD_random"+str(i)
    os.system("python3 Application1_reformulation.py "+name)

#Call application 2
list_graphs = ["jean","myciel4","myciel5","myciel6","myciel7","queen5_5","queen6_6","queen7_7","queen8_8","queen8_12","queen9_9"]

for graph in list_graphs:
    nameDimacs = graph+".col"
    name = graph+"_det1"
    os.system("python3 Application2_reformulation.py "+nameDimacs+" "+name)
    name = graph+"_random1"
    os.system("python3 Application2_reformulation.py "+nameDimacs+" "+name)
