def turnOn(x1, x2, y1, y2, a2d):
    for i in range(x1, y1):
        for j in range(x2, y2):
            a2d[i][j] = True
        return

def switch(x1, x2, y1, y2, a2d):
        for i in range(x1, y1):
            for j in range(x2, y2):

                if a2d[i][j] == False:
                    a2d[i][j] = True

                if a2d[i][j] == True:
                    a2d[i][j] = False
        return

N = 10
a2d = [ [0]*N for _ in range(N) ]
turnOn(1, 1, 7, 7, a2d)
print(a2d)
switch(2, 2, 6, 6, a2d)
print(a2d)

