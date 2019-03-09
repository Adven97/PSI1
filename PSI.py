import random
import matplotlib.pyplot as plt
import math

a= list()
b=list()
cities=list()
pointsNom =10

# generating and drawing points with labels

for x in range(pointsNom):
    a.append(random.randint(0,90))
    b.append(random.randint(0,90))
    cities.append(x)

    print("City "+str(cities[x]) + " : ( "+str(a[x])+" , "+str(b[x])+" )" )
    plt.scatter(a[x],b[x],s=12)
    if x==0:
        start = 'START - '+str(x)
        plt.annotate(start ,(a[x],b[x]))
    else:
        plt.annotate(x ,(a[x],b[x]))

### Choosing best way and closest points to go

def  searchForShortest():
    shortestWays =list()
    shortestWays2 =list()
    #smallest=0
    points = cities
    current=0

    for x in range(pointsNom-1):
        temp ={} 
        tmp2=[]
        for i in points:
            if current !=i:
                xd = (a[current] - a[i])**2 + (b[current] - b[i])**2 
                cost = math.sqrt(xd)
               # if cost != smallest or i==1:
                temp.update({i: cost})
                tmp2.append(cost)
                print("droga "+str(i)+" wynosi: "+str(cost))
                
        print(' - - - - - - -- - - -  -- - - - ')
        print(temp)
        print(' - - - - - - -- - - -  -- - - - ')
       
        current = min(temp, key=lambda k: temp[k])
        #points.pop(current)
        if len(temp) !=1:
            points.remove(current)
        if 0 in points:
             points.remove(0)
        shortestWays.append(current)
        shortestWays2.append(min(tmp2))
        
    print('To sa najlepsze drogi: ')
    shortestWays.insert(0, 0)
    #shortestWays.insert(0)
    print(shortestWays2)    ### tu jest pizda, bo tempy muszą miec stala wielkosc
    print('I maja takie wsp: ')
    print(shortestWays)
    return shortestWays 
    
    
bestway = searchForShortest()

# drawing lines betweeen points

for xx in bestway:
    
    if xx==bestway[-1]:
        # print(xx)
        # print(0)
        # print()
        plt.plot([ a[xx],a[0] ] , [ b[xx],b[0] ] )
    else:
        # print(xx)
        nextPoint = bestway[bestway.index(xx)+1]
        # print(nextPoint)
        # print()
        plt.plot([a[xx], a[nextPoint]], [b[xx], b[nextPoint]])


plt.show()
