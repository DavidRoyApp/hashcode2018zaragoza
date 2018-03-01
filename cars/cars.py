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

    global R #nº de filas
    global C #nº de columnas
    global F #nº de coches
    global N #nº de riders
    global B #bonus por empezaren t_min
    global T #nº de pasos

    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    # línea 1
    R, C, F, N, B, T = map(int, lines[0].split())
    rides = [list(map(int, line.split(' '))) for line in lines]
    rides = rides[1:len(lines)]
    print(rides)

    #iterar hasta T pasos   

def writeOutput(filename):
    for row in range(0, R):
        for col in range(0, C):
            print pizza[row][col],
        print

def algoritmoPrincipal():
    global t

    for car in range(0,F): #para cada coche
        while t <= T: #mientras haya tiempo
            filtrados= filtrarRides()
            ordenados= ordenarRides(filtrados)
            #coger el 1º del array ordenados
            c= ordenados[0]
            #actualizar variables
            pos=c.destino
            t= t+ (diferencia entre c.origen y t) + c.distancia

def filtrarRides():
    #variables
    # d= diferencia entre origen del ride y pos (la posición del coche)

    #filtrar
    # que no tengan coche asignado
    # que t_min <= d + t && d+t <= t_max

    #devolver array


def ordenarRides(rides):
    #ordenar por distancia desc

    #devolver array


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
