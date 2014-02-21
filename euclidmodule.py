import numpy as np
import math
#Second Method
def euclidmain():
    p = [(2, 10),(2, 5),(8, 4),(5, 8),(7, 5),
    (6, 4),
    (1, 2),
    (4, 9)]

    NOT = [(1,1),(2,1),(4,3),(5,4)]
    p2 = p


    #choose n number of clusters(centers)
    orig = p[0]
    orig2 = p[3]
    orig3 = p[6]

        #Change to add more
    L1 = list()
    L2 = list()
    L3 = list()    

    G = list()
    Gprev = list()

    xlist=list()
    ylist=list()


    def euclid():
        print("\nDist mean1: ",orig)
        print("\nDist mean2: ",orig2)
        #print("\nDist mean3: ",orig3)

    #Calculates Distances by doing x points first then y points
    #Change to add more
        firstdist=list(map(lambda point: (math.sqrt(((point[0]-orig[0])**2)+ ((point[1]-orig[1])**2))), p))
        print("First Distance Mean: ",firstdist)

        seconddist=list(map(lambda point:(math.sqrt(((point[0]-orig2[0])**2)+ ((point[1]-orig2[1])**2))), p))
        print("Second Distance Mean: ",seconddist)

        thirddist=list(map(lambda point:(math.sqrt(((point[0]-orig3[0])**2)+ ((point[1]-orig3[1])**2))), p))
        print("THrid Distance Mean: ",thirddist)



    #Combining the x and y coordinates back into pairs
        #Change to add more
        zipped = zip(firstdist,seconddist,thirddist)
        ###################

    #turning Zipped pairs into a list
        listzip=list(zipped)
        print("\nCalculated Distances: ",listzip)
        length = len(listzip)


    #Determining the minimum of each pair
        ##############
        for n in range(length):
            #print("Size of tuple: ",length) #Total number of points to find min distances
            mint = min(listzip[n]) #Finding minimum of each pair at "n" position
            #print("Min in current Tuple: ",mint) #The min in the pair
            minttuple = (listzip[n].index(mint)) #location of that minimum
            #print("Current Coordinates: ", p[n])
            #print("Location of Min Tuple (Closest to): ",minttuple+1) #Which cluster is closest, add one because of start being [0]

            G.append(minttuple+1)
            if ((minttuple+1) == 1):
                L1.append(p[n])

            elif((minttuple+1) == 2):
                L2.append(p[n])

            elif((minttuple+1) == 3):
                L3.append(p[n])
            
            n=n+1
            #print("\n")


        poped = p2.pop(0)
        print("P List: ",p2)

    while True:
        euclid()
        orig = list(np.average(L1, axis = 0))
        orig2 = list(np.average(L2, axis=0))
        orig3 = list(np.average(L3, axis=0))
        print("C1: ",orig)
        print("C2: ",orig2)
        print("C3: ",orig3)
        print("Cur G: ",G)
        print("Prev G: ",Gprev)
        if G == Gprev:
            break
        elif G != Gprev:
            Gprev = G
    return orig,orig2,orig3
 
#euclidmain()
