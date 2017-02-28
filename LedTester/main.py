#!/bin/python

import argparse
import urllib.request

def countLights(N, a2d):
    count = 0
    for i in range(N):
        for j in range(N):
            if a2d[i][j] == 1:
                count += 1
    return count
       

def turnOn(x1, x2, y1, y2, a2d):
    for i in range(x1, y1 +1):
        for j in range(x2, y2 +1):
            a2d[i][j] = 1
    return
    
    
def turnOff(x1, x2, y1, y2, a2d):
    for i in range(x1, y1 +1):
        for j in range(x2, y2 +1):
            a2d[i][j] = 0
    return
        
                
    
def switch(x1, x2, y1, y2, a2d):
    for i in range(x1, y1 +1):
        for j in range(x2, y2 +1):   
            if a2d[i][j] == 0:
                a2d[i][j] = 1        
            elif a2d[i][j] == 1:
                a2d[i][j] = 0
        return
def main():
    #create parser
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--input', help='input help')
    #args = parser.parse_args()
    #filename = args.input  
      
    
    #read file in to buffer in utf 8 format
    #uri = filename
    req = urllib.request.Request("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    response = urllib.request.urlopen(req)
    buffer = response.read().decode('utf-8')
    
    
    
    #set size of grid, read each line from file (sep by return)
    for line in buffer.split('\n'):
        #N = line #interpreting line as a string cant pass in to a2d as string.
        #N = 0 - possibly solution until gets to  if
        #a2d = [[0]*N for _ in range(N)]

        if line.isdigit():
            newRange = line
            
            N = int(line)
            a2d = [ [0]*N for _ in range(N) ]
            
        
        else:
            newCommand = line
            newCommand = newCommand.replace("through", "")
            
            if newCommand.startswith( 'turn on' ):
                newCommand = newCommand.replace("turn on", "")
                splitVal = newCommand.split(" ")
                splitVal2 = splitVal[1].split(",")
                splitVal3 = splitVal[3].split(",")
                x1 = splitVal2[0]
                x2 = splitVal3[0]
                y1 = splitVal2[1]
                y2 = splitVal3[1]
                turnOn(int(x1), int(x2), int(y1), int(y2), a2d)

            elif newCommand.startswith( 'turn off' ):
                newCommand = newCommand.replace("turn off", "")
                splitVal = newCommand.split(" ")
                splitVal2 = splitVal[1].split(",")
                splitVal3 = splitVal[3].split(",")  
                x1 = splitVal2[0]
                x2 = splitVal3[0]
                y1 = splitVal2[1]
                y2 = splitVal3[1]
                turnOff(int(x1), int(x2), int(y1), int(y2), a2d)

            elif newCommand.startswith( 'switch' ):
                newCommand = newCommand.replace("switch", "")
                splitVal = newCommand.split(" ")
                splitVal2 = splitVal[1].split(",")
                splitVal3 = splitVal[3].split(",")
                x1 = splitVal2[0]
                x2 = splitVal3[0]
                y1 = splitVal2[1]
                y2 = splitVal3[1]
                switch(int(x1), int(x2), int(y1), int(y2), a2d)

            
    
    
    
    count = countLights(N, a2d)
    print ("Number of lights on ", count)
    
    
    return


if __name__ == '__main__':
    main()