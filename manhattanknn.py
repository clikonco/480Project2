def manhattan():
    #manhattan
    p = [(2, 10),(2, 5),(8, 4),(5, 8),(7, 5),
    (6, 4),
    (1, 2),
    (4, 9)]

    p2 = [(1,1),(2,1),(4,3),(5,4)]

    #choose n number of clusters(centers)
    orig = p[0]
    orig2 = p[3]
    orig3 = p[6]

    print("\nDist mean1: ",orig)
    print("\nDist mean2: ",orig2)
    print("\nDist mean3: ",orig3)


    #Change to add more
    firstdist=list(map(lambda point: (abs(point[0]-orig[0])+ abs(point[1]-orig[1])), p))
    print("First Distance Mean: ",firstdist)

    seconddist=list(map(lambda point: (abs(point[0]-orig2[0])+ abs(point[1]-orig2[1])), p))
    print("Second Distance Mean: ",seconddist)

    thirddist=list(map(lambda point: (abs(point[0]-orig3[0])+ abs(point[1]-orig3[1])), p))
    print("Third Distance Mean: ",thirddist)

    #Change to add more
    zipped = zip(firstdist,seconddist,thirddist)
    ###################

    listzip=list(zipped)
    print(listzip)
    length = len(listzip)

    #Change to add more
    L1 = list()
    L2 = list()
    L3 = list()

    xlist=list()
    ylist=list()




    ##############
    for n in range(length):
        print("Size of tuple: ",length)
        mint = min(listzip[n])
        print("Min in current Tuple: ",mint)
        minttuple = (listzip[n].index(mint))
        j=p[n]
        print("Current Coordinates: ", p[n])
        print("Location of Min Tuple (Closest to): ",minttuple+1)

        if ((minttuple+1) == 1):
            L1.append(p[n])

        elif((minttuple+1) == 2):
            L2.append(p[n])

        elif((minttuple+1) == 3):
            L3.append(p[n])
            
        
        n=n+1
        print("\n")
    print("Near Cluster one:",L1)
    print("Near CLuster two:",L2)
    print("Near CLuster three:",L3)

    uz1=list(zip(*L1))
    uz2=list(zip(*L2))
    uz3=list(zip(*L3))

    print("Unziped L1: ",uz1)
    print("Unziped L2: ",uz2)
    print("Unziped L3: ",uz3)


    #FOR X
    uz2ttl=sum(uz2[0])
    #print(uz2ttl)
    uz2len=len(uz2[0])
    #print(uz2len+1)
    uz2ttl=(uz2ttl/(uz2len))
    xlist.append(uz2ttl)
    #print(uz2ttl)

    #FOR Y
    uz2ttl2=sum(uz2[1])
    #print(uz2ttl2)
    uz2len2=len(uz2[1])
    #print(uz2len2+1)
    uz2ttl2=(uz2ttl2/(uz2len2))
    #print(uz2ttl2)
    ylist.append(uz2ttl2)


    newcenter2=zip(xlist,ylist)
    listcoord2=list(newcenter2)

    xlist[:] = []
    ylist[:] = []


    #FOR X
    uz3ttl=sum(uz3[0])
    #print(uz2ttl)
    uz3len=len(uz3[0])
    #print(uz2len+1)
    uz3ttl=(uz3ttl/(uz3len))
    xlist.append(uz3ttl)
    #print(uz2ttl)

    #FOR Y
    uz3ttl3=sum(uz3[1])
    #print(uz2ttl2)
    uz3len3=len(uz3[1])
    #print(uz2len2+1)
    uz3ttl3=(uz3ttl3/(uz3len3))
    #print(uz2ttl2)
    ylist.append(uz3ttl3)


    newcenter2=zip(xlist,ylist)
    listcoord3=list(newcenter2)




    print("New Center for CLuster two: ",listcoord2)
    print("New Center for CLuster three: ",listcoord3)
    return (listcoord2,listcoord3)
