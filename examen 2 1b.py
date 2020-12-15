# -*- coding: utf-8 -*-
"""
@author: BriaN
"""

import pandas as pd
import numpy as np

def optimo(matriz_costos):
    # Declara e inicializa candidatos, estado y tour
    candidatos = list(range(len(matriz_costos)))
    candidatos.remove(0)
    estado = 0
    tour = [estado]
    # Ciclo de busqueda termina cuando no hay más candidatos
    while True:
        if len(candidatos) == 0:
            tour.append(0)
            break
        # Selecciona el candidato con el menor costo
        estado = min(candidatos, key=(lambda j: matriz_costos[estado][j] if estado >= j else matriz_costos[j][estado]))
        # Agrega el estado al tour y lo remueve de la lista de candidatos
        tour.append(estado), candidatos.remove(estado)
    return tour

def recorrido(tour, matriz_costos):
    ##devuelve el menor camino
    costo = sum(matriz_costos[tour[i]][tour[i+1]] 
        if tour[i] >= tour[i+1]
        else matriz_costos[tour[i+1]][tour[i]]
        for i in tour[:-1])
    return costo

def main():
    df = pd.read_csv("cv.csv")
    print(df)
    #Convirtiendo el df a matriz
    df=df.drop("cv",axis=1)
    matriz = np.array(df)
    tour = optimo(matriz)
    print("Tour:", tour)
    print("Costo: ", recorrido(tour, matriz)) 

if __name__ == '__main__':
    main()
    