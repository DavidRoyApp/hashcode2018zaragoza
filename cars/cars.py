#!/usr/bin/python
# -*- coding: utf-8 -*-

#inFilename = "./a_example.in"
#outFilename = "./output1.txt"

#inFilename = "./b_should_be_easy.in"
#outFilename = "./output2.txt"

#inFilename = "./c_no_hurry.in"
#outFilename = "./output3.txt"

#inFilename = "./d_metropolis.in"
#outFilename = "./output4.txt"

inFilename = "./e_high_bonus.in"
outFilename = "./output5.txt"

R = 0  # nº de filas
C = 0  # nº de columnas
F = 0  # nº de coches
N = 0  # nº de riders
B = 0  # bonus por empezaren t_min
T = 0  # nº de pasos

ridesInput = []
rides = []

ncar = 0 # nº de coche actual
tActual = 0 # el tiempo actual
posCar = (0, 0) # la posición actual del coche


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
        newRide.source = (field[0], field[1])
        newRide.target = (field[2], field[3])
        newRide.distance = distance(newRide.source, newRide.target)
        newRide.tstart_max = field[5] - newRide.distance
        newRide.t_min = field[4]
        newRide.car = -1
        rides.append(newRide)
        key += 1


def distance(tuple1, tuple2):
    return abs(tuple1[0] - tuple2[0]) + abs(tuple1[1] - tuple2[1])


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
    global tActual, posCar

    for car in range(0, F):  # para cada coche
        print("coche nº: "+ str(car))
        
        ordenados = rides
        tActual = 0  # cada coche empieza con tiempo 0
        posCar = (0, 0) #resetear posicion del coche
        while tActual < T:  # mientras haya tiempo
            filtrados = filtrarRides(ordenados)
            print("len filtrados: "+ str(len(filtrados)))
            #filtrados = filtrarRidesMalo()  # filtrar a partir del total de rides
            ordenados = ordenarRidesBonus(filtrados)  # de los filtrados, los ordenamos
            print("len ordenados: "+ str(len(ordenados)))
            # coger el 1º del array ordenados
            if(len(ordenados) > 0):
                selectedRide = ordenados[0]
                # actualizar variables
                rides[selectedRide.id].car = car
                ordenados = ordenados[1:len(ordenados)]
                posCar = selectedRide.target
                timeToSource = distance(selectedRide.source, posCar) + tActual
                tActual = selectedRide.distance + timeToSource
            else:
                tActual = T


def filtrarRidesMalo():
    ret = []
    for r in rides:
        timeToSource = distance(r.source, posCar) + tActual
        #print(timeToSource)
        #print(r.t_min)
        #print(r.tstart_max)
        #print(tActual)
        #print("\n")
        # TODO: Primer filtro puede dar problemas, no pasa nada por esperar
        if (r.car < 0 and r.t_min <= timeToSource and timeToSource <= r.tstart_max):
            ret.append(r)
    return ret


def filtrarRides(ridesList):
    ret = []
    for r in ridesList:
        timeToSource = distance(r.source, posCar) + tActual

        if (r.t_min >= timeToSource):
            r.bonus = B
            r.delay = r.t_min - timeToSource
        else:
            r.bonus = 0
            r.delay = 0

        if (r.car < 0 and timeToSource <= r.tstart_max):
            ret.append(r)
    return ret


def ordenarRides(ridesList):
    # ordenar por distancia desc
    return sorted(ridesList, key=lambda x: x.distance - distance(x.source, posCar), reverse=True)


def ordenarRidesBonus(ridesList):
    # ordenar por distancia desc
    return sorted(ridesList, key=lambda x: x.bonus - x.delay + x.distance - distance(x.source, posCar), reverse=True)


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
    bonus = 0 # bonus de puntualidad
    delay = 0 # tiempo de espera hasta t_min


# esto siempre al final
if __name__ == '__main__':
    main()
