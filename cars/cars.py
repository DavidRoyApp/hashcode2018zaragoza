#!/usr/bin/python
# -*- coding: utf-8 -*-

inFilename = "./a_example.in"
outFilename = "./output.txt"
ncar = 0
t=0
pos=(1,2)
R = 0 #nº de filas
C = #nº de columnas
F = #nº de coches
N = #nº de riders
B = #bonus por empezaren t_min
T = #nº de pasos
ridesInput = []
rides = []

def main():
    readInput(inFilename)
    #writeOutput(outFilename)


def readInput(filename):
    # leer fichero de entrada

    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    # línea 1
    R, C, F, N, B, T = map(int, lines[0].split())
    ridesInput = [list(map(int, line.split(' '))) for line in lines]
    ridesInput = ridesInput[1:len(lines)]
    for(ride in ridesInput):
        newRide = Ride()
        newRide.source = (ride[0], ride[2])
        newRide.target = (ride[1], ride[3])
        newRide.distance = distance(newRide.origen, newRide.destino)
        newRide.tstart_max = ride[5] - newRide.distance
        newRide.t_min = ride[4]
        newRide.car = -1
        rides.append(newRide)
    
    print(rides)


def distance(tuple1, tuple2):
    return abs(tuple1[0] - tuple2[0]) + abs(tuple1[1] - tuple2[1])
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
    id = 0 # id del ride
    distance = 0 # 
    t_min = 0 # cuando es lo más pronto que puede empezar
    tstart_max = 0 # cuando es lo más tarde que puede empezar
    source = ()
    target = ()
    car = 0 # coche que tiene asignado. 0 si no lo tiene asignado




# esto siempre al final
if __name__ == '__main__':
    main()
