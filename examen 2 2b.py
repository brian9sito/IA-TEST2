# -*- coding: utf-8 -*-
"""
@author: BriaN
"""

import random

poblacion =([[random.randint(0,1) for x in range(6)] for i in range(4)])
scpadres=[]
print('Poblacion', "\n")
print(poblacion)


def funcionEval() :
    global poblacion 
    valores = []
    print('valores')
    for i in range(4) :
        crvalor=0
        
        for j in range(5,0,-1) :
            crvalor += poblacion[i][j]*(2**(5-j))
        crvalor = crvalor if poblacion[i][0]==1 else crvalor
        print(crvalor)
        valores.append((crvalor**3) +(crvalor**2) + crvalor)
   
    print('F(x) = x^(3)+x^(2)+ x ')   
    valores, poblacion  = zip(*sorted(zip(valores, poblacion) , reverse = True))
  

def seleccion():
    global scpadres
    scpadres=poblacion[0:2]
    
    print('mejor individuo')
    print(scpadres)
    
    

def cruce() :
    global scpadres
    
    pcruce = random.randint(0,5)
    scpadres =scpadres + tuple([(scpadres[0][0:pcruce +1] +scpadres[1][pcruce+1:6])])
    scpadres =scpadres+ tuple([(scpadres[1][0:pcruce +1] +scpadres[0][pcruce+1:6])])
    
    print(scpadres)
    


def mutacion() :
    global poblacion, scpadres
    muta = random.randint(0,49)
    if muta == 20 :
        x=random.randint(0,3)
        y = random.randint(0,5)
        scpadres[x][y] = 1-scpadres[x][y]
    poblacion  = scpadres
    print(poblacion,"\n")
     
for i in range(3) :
    funcionEval()
    seleccion() 
    print('Cruce')
    cruce()
    print('Mutación')
    mutacion()
    
    