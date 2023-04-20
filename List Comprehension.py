if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coords = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if [i, j, k] not in coords and i+j+k != n:
                    coords.append([i,j,k])
    print(coords)
