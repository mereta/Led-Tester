#!/bin/python

import argparse

def turnOn(x1, x2, y1, y2, a2d):
    for i in range(x1, y1):
        for j in range(x2, y2):
            a2d[i][j] = True
return
    
    
def turnOff(x1, x2, y1, y2, a2d):
        for i in range(x1, y1):
            for j in range(x2, y2):
                a2d[i][j] = False
return
        
                
    
def switch(x1, x2, y1, y2, a2d):
        for i in range(x1, y1):
            for j in range(x2, y2):
                
                if a2d[i][j] = False:
                    a2d[i][j] = True
                    
                if a2d[i][j] = True:
                    a2d[i][j] = False
return

def main():
    #create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input  
      
    
    #read file in to buffer in utf 8 format
    uri = filename
    req = urllib.request.urlopen(uri)
    buffer = req.read().decode('utf-8') 
    
    #set size of grid, read each line from file (sep by return)
    for i, line in buffer.split('\n'):
        if i == 0:
            newRange = line
            
            N = line
            a2d = [ [False]*N for _ in range(N) ]
            
        
        elif 
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

                elif newCommand.startswith( 'turn off' ):
                    newCommand = newCommand.replace("turn off", "")
                    splitVal = newCommand.split(" ")
                    splitVal2 = splitVal[1].split(",")
                    splitVal3 = splitVal[3].split(",")
                    x1 = splitVal2[0]
                    x2 = splitVal3[0]
                    y1 = splitVal2[1]
                    y2 = splitVal3[1]

                elif newCommand.startswith( 'switch' ):
                    newCommand = newCommand.replace("switch", "")
                    splitVal = newCommand.split(" ")
                    splitVal2 = splitVal[1].split(",")
                    splitVal3 = splitVal[3].split(",")
                    x1 = splitVal2[0]
                    x2 = splitVal3[0]
                    y1 = splitVal2[1]
                    y2 = splitVal3[1]

            
    
    
    
    
    
    return


if __name__ == '__main__':
    main()