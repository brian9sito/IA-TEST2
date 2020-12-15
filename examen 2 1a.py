# -*- coding: utf-8 -*-
"""
@author: BriaN
"""

import pandas as pd
import numpy as np
import random
import deap as de

#guardando en la variable df el Comma-Separated Values csv
df = pd.read_csv("cv.csv")
print(df)

#Convirtiendo el df a una matrizl
df=df.drop("cv",axis=1)
matrizl = np.array(df)

cant_lugares = len(matrizl)

de.creator.create("FitnessMin", de.base.Fitness, weights=(-1.0,))
de.creator.create("Individual", list, fitness=de.creator.FitnessMin)
toolbox = de.base.Toolbox()

toolbox.register("indices", random.sample, range(cant_lugares), cant_lugares)
toolbox.register("individual", de.tools.initIterate, de.creator.Individual, toolbox.indices)
toolbox.register("population", de.tools.initRepeat, list, toolbox.individual)
ind = toolbox.individual() # creamos un individuo aleatorio

def evalD(individual):
    """ Función objetivo, calcula la distancia que recorre el viajante"""
    # distancia entre el último elemento y el primero
    distancia = matrizl[individual[-1]][individual[0]]
    # distancia entre el resto de ciudades
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distancia += matrizl[gene1][gene2]
    return distancia,

toolbox.register("evaluate", evalD)
toolbox.register("mate", de.tools.cxOrdered)
toolbox.register("mutate", de.tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", de.tools.selTournament, tournsize=cant_lugares)    
    
def main():
    random.seed(64) # ajuste de la semilla del generador de números aleatorios
    pop = toolbox.population(n=200) # creamos la población inicial 
    hof = de.tools.HallOfFame(1) 
    stats = de.tools.Statistics(lambda ind: ind.fitness.values) 
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    log = de.tools.Logbook()     
    pop, log = de.algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats, halloffame=hof, verbose=False)
    return pop, hof, log

if __name__ == "__main__":
    pop, hof, log = main()
    print(log)
    print("Mejor recorrido: %f" %hof[0].fitness.values)
    print("Camino recorrido:",hof[0])

