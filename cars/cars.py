#!/usr/bin/python
# -*- coding: utf-8 -*-

inFilename = "./a_example.in"
outFilename = "./output.txt"
#ncar = 0
#t=0
#pos=(1,2)
rides = []

def main():
    readInput(inFilename)
    #writeOutput(outFilename)


def readInput(filename):
    # leer fichero de entrada

    global R, C, F, N, B, T

    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    # línea 1
    R, C, F, N, B, T = map(int, lines[0].split())
    rides = [list(map(int, line.split(' '))) for line in lines]
    rides = rides[1:len(lines)]
    print(rides)

    #rides que no tengan coche asignado y cumplan el requisito de que la diferencia entre origen y posicion del coche (d)
    #+ t_actual este entre tmin y tmax
    #ordenar por distancia desc y primero -> coche 1
    #actualizar variables: posicion del coche = destino + distancia, tactual +=  d + distancia
    #iterar hasta T pasos   

def writeOutput(filename):
    for row in range(0, R):
        for col in range(0, C):
            print pizza[row][col],
        print


# def doSlices():
# calcular los slices


################################################################################
class Ride:
    distance = 0
    t_min = 0 # cuando es lo más pronto que puede empezar
    t_max = 0 # cuando es lo más tarde que puede empezar
    origen = {}
    destino = {}
    coche = 0 # coche que tiene asignado. 0 si no lo tiene asignado




# esto siempre al final
if __name__ == '__main__':
    main()
