zx = ["CASA","LKKK","ABB"]

for x in range(len(zx)):
    for y in range(len(zx)-1):
        if zx[y]> zx[y+1]:
            zx[y+1],zx[y] = zx[y],zx[y+1]

print(zx)
