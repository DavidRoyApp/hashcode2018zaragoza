#!/usr/bin/python
# -*- coding: utf-8 -*-

inFilename = "./a_example.in"
outFilename = "./output.txt"
rides = []

def main():
    readInput(inFilename)
    #writeOutput(outFilename)


def readInput(filename):
    # leer fichero de entrada

    global R, C, L, H, pizza

    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    # línea 1
    R, C, F, N, B, T = map(int, lines[0].split())
    rides = [list(map(int, line.split(' '))) for line in lines]
    rides = rides[1:len(lines)]
    print(rides)


def writeOutput(filename):
    for row in range(0, R):
        for col in range(0, C):
            print pizza[row][col],
        print


# def doSlices():
# calcular los slices


################################################################################
class Slice:
    rowIni = 0
    colIni= 0
    rowFin = 0
    colFin= 0




# esto siempre al final
if __name__ == '__main__':
    main()
