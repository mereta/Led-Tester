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
N = 10
a2d = [ [0]*N for _ in range(N) ]
turnOn(2, 2, 9, 9, a2d)
turnOff(3,3, 4, 4, a2d)
switch(0, 0, 2, 2, a2d)
#print(a2d)
for a in a2d:
    print(a)

#print(a2d)
count = countLights(N, a2d)
print (count)


