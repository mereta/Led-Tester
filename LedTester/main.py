#!/bin/python

import argparse
import urllib.request
import re


def countLights(N, a2d):
    count = 0
    for i in range(N):
        for j in range(N):
            if a2d[i][j] == 1:
                count += 1

    return count


def turnOn(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 +1):
        for j in range(y1, y2 +1):
            a2d[i][j] = 1
   # for a in a2d:
    #    print(a)
    #print('\n')

    return


def turnOff(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 +1):
        for j in range(y1, y2 +1):
            a2d[i][j] = 0
    #for a in a2d:
      #  print(a)
   # print('\n')
    return


def switch(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 +1):
        for j in range(y1, y2 +1):
            if a2d[i][j] == 0:
                a2d[i][j] = 1
            elif a2d[i][j] == 1:
                a2d[i][j] = 0
  #  for a in a2d:
     #   print(a)
   # print('\n')
    return


def split(line):

    newCommand = line
    #newCommand = newCommand.replace(" ", ",")
    newCommand = newCommand.replace("through", "")
    newCommand = newCommand.replace("\n", ",")
    if line.startswith(" "):
        newCommand = newCommand.strip()
    if newCommand.endswith(" "):
        #newCommand = newCommand.replace(" ", "\n")
        newCommand = newCommand.strip()
    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""
    cmd = ""
    #splitval = []
    #print (line)
    #if newCommand.startswith(" " or "\t"):
        #newCommand = newCommand.replace(" " or "\t", "")
    if newCommand.startswith('turn on'):
        cmd = "turn on"
        newCommand= newCommand.replace("turn on", "")
    if newCommand.startswith('turn off'):
        cmd = "turn off"
        newCommand=  newCommand.replace("turn off", "")
    if newCommand.startswith('switch'):
        cmd = "switch"
        newCommand = newCommand.replace("switch", "")

    if cmd != "":
        newCommand = newCommand.replace(",", " ")
        val = [int(s) for s in newCommand.split() if s.isdigit()]

        x1 = val[0]
        x2 = val[2]
        y1 = val[1]
        y2 = val[3]

    return cmd, x1, x2, y1, y2


def sanitize(x1, x2, y1, y2, N):

    if int(x1) < 0:
        x1 = 0
    if int(x2) < 0:
        x2 = 0
    if int(y1) < 0:
        y1 = 0
    if int(y2) < 0:
        y2 = 0

    if int(x1) >= N:
        x1 = N - 1
    if int(x2) >= N:
        x2 = N - 1
    if int(y1) >= N:
        y1 = N - 1
    if int(y2) >= N:
        y2 = N - 1

    return x1, x2, y1, y2


def main() -> object:
    # create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input


    # read file in to buffer in utf 8 format
    uri = filename
    req = urllib.request.Request(filename)
    response = urllib.request.urlopen(req)
    buffer = response.read().decode('utf-8')
    #buffer = filename
    #buffer = read_file(filename=filename)


    a2d = []
    # set size of grid, read each line from file (sep by return)
    for line in buffer.split('\n'):
    #with open("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_.txt") as f:
        #for line in f:
            #linedata = line.split('\n')
            #check line is not empty
            if line == "":
                break

            if line.isdigit():
                N = int(line)
                a2d = [[0] * N for _ in range(N)]

            else:

                command, x1, x2, y1, y2 = split(line)

                if command == "turn on":

                    x1, x2, y1, y2 = sanitize(x1, x2, y1, y2, N)
                    #print(x1, x2, y1, y2)

                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        turnOn(int(x1), int(x2), int(y1), int(y2), a2d)
                    #print(splitVal, splitVal2, splitVal3, x1, x2, y1, y2)

                elif command == "turn off":

                    x1, x2, y1, y2 = sanitize(x1, x2, y1, y2, N)
                    #print(x1, x2, y1, y2)

                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        turnOff(int(x1), int(x2), int(y1), int(y2), a2d)
                    #print(splitVal, splitVal2, splitVal3, x1, x2, y1, y2)

                elif command == "switch":

                    x1, x2, y1, y2 = sanitize(x1, x2, y1, y2, N)
                    #print(x1, x2, y1, y2)

                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        switch(int(x1), int(x2), int(y1), int(y2), a2d)
                    #print(splitVal, splitVal2, splitVal3, x1, x2, y1, y2)

    count = countLights(N, a2d)
    print("Number of lights on ", count)
    print(filename)


    return


if __name__ == '__main__':
    main()
