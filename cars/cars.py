#!/usr/bin/python
# -*- coding: utf-8 -*-

inFilename = "./a_example.in"
outFilename = "./output.txt"
ncar = 0
tActual = 0
posCar = (0, 0)
R = 0  # nº de filas
C = 0  # nº de columnas
F = 0  # nº de coches
N = 0  # nº de riders
B = 0  # bonus por empezaren t_min
T = 0  # nº de pasos
ridesInput = []
rides = []


def main():
    readInput(inFilename)
    algoritmoPrincipal()
    writeOutput(outFilename)


def readInput(filename):
    # leer fichero de entrada
    global R, C, F, N, B, T
    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    # línea 1
    R, C, F, N, B, T = map(int, lines[0].split())
    ridesInput = [list(map(int, line.split(' '))) for line in lines]
    ridesInput = ridesInput[1:len(lines)]
    key = 0
    for field in ridesInput:
        newRide = Ride()
        newRide.id = key
        newRide.source = (field[0], field[2])
        newRide.target = (field[1], field[3])
        newRide.distance = distance(newRide.source, newRide.target)
        newRide.tstart_max = field[5] - newRide.distance
        newRide.t_min = field[4]
        newRide.car = -1
        rides.append(newRide)
        key += 1


def distance(tuple1, tuple2):
    return abs(tuple1[0] - tuple2[0]) + abs(tuple1[1] - tuple2[1])
    # iterar hasta T pasos


def writeOutput(filename):
    file = open(filename,"w") 
  
    for row in range(0, F):  # para cada coche
        encontrado = 0
        asignados= []
        # buscar en rides todos los que tengan ride.car == row e imprimir ride.id
        for ri in rides:
            if (ri.car == row):
                encontrado += 1
                asignados.append(ri.id)
        
        file.write(str(encontrado) + ' ')
        for i in asignados:
            file.write(str(i) + ' ')
        file.write('\n')
    file.close()
    


def algoritmoPrincipal():
    # filtrados = rides
    for car in range(0, F):  # para cada coche
        tActual = 0  # cada coche empieza con tiempo 0
        posCar = (0, 0) #resetear posicion del coche
        while tActual < T:  # mientras haya tiempo
            # filtrados = filtrarRides(filtrados)
            filtrados = filtrarRidesMalo()  # filtrar a partir del total de rides
            ordenados = ordenarRides(filtrados)  # de los filtrados, los ordenamos
            # coger el 1º del array ordenados
            if(len(ordenados) > 0):
                selectedRide = ordenados[0]
                # actualizar variables
                rides[selectedRide.id].car = car
                posCar = selectedRide.target
                timeToSource = distance(selectedRide.source, posCar) + tActual
                tActual = selectedRide.distance + timeToSource
            else:
                tActual = T


def filtrarRidesMalo():
    ret = []
    for r in rides:
        timeToSource = distance(r.source, posCar) + tActual
        # TODO: Primer filtro puede dar problemas, no pasa nada por esperar
        if (r.car < 0 and r.t_min <= timeToSource and timeToSource <= r.tstart_max):
            ret.append(r)
    return ret


def filtrarRides(ridesList):
    ret = []
    for r in ridesList:
        timeToSource = distance(r.source, posCar) + tActual
        # TODO: Primer filtro puede dar problemas, no pasa nada por esperar
        if (r.car < 0 and r.t_min <= timeToSource and timeToSource <= r.tstart_max):
            ret.append(r)
    return ret


def ordenarRides(ridesList):
    # ordenar por distancia desc
    return sorted(ridesList, key=lambda x: x.distance, reverse=True)


# def doSlices():
# calcular los slices


################################################################################
class Ride:
    id = 0  # id del ride
    distance = 0  #
    t_min = 0  # cuando es lo más pronto que puede empezar
    tstart_max = 0  # cuando es lo más tarde que puede empezar
    source = ()
    target = ()
    car = 0  # coche que tiene asignado. 0 si no lo tiene asignado


# esto siempre al final
if __name__ == '__main__':
    main()
