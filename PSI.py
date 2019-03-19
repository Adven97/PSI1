import random
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt2
import math
import itertools
from tabulate import tabulate

a = list()
b = list()
cities = list()
pointsNom = 4

# generating and drawing points with labels
print(" ------------------------- Zachlanny --------------------------------- ")
plt.subplot(2, 1, 1)
plt.title('Zachlanny')

for x in range(pointsNom):
    a.append(random.randint(0, 90))
    b.append(random.randint(0, 90))
    cities.append(x)

    print("City "+str(cities[x]) + " : ( "+str(a[x])+" , "+str(b[x])+" )")
    plt.scatter(a[x], b[x], s=12)
    if x == 0:
        start = 'START - '+str(x)
        plt.annotate(start, (a[x], b[x]))
    else:
        plt.annotate(x, (a[x], b[x]))

cities_tmp= cities
print("tak wyglada cities: ")
print(cities_tmp)
### Choosing best way and closest points to go - zachłanny


def search_for_shortest():
    shortestWays = list()
    shortestWays2 = list()
    #smallest=0
    points = cities
    current = 0

    for x in range(pointsNom-1):
        temp = {}
        tmp2 = []
        for i in points:
            if current != i:
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
        if len(temp) != 1:
            points.remove(current)
        if 0 in points:
             points.remove(0)
        shortestWays.append(current)
        shortestWays2.append(min(tmp2))

    print('To sa najlepsze drogi: ')
    shortestWays.insert(0, 0)
    #shortestWays.insert(0)
    print(shortestWays2)  

    suma = sum(shortestWays2)
    xdd = (a[shortestWays[-1]] - a[shortestWays[0]])**2 + (b[shortestWays[-1]] - b[shortestWays[0]])**2
    cost2 = math.sqrt(xdd)
    suma += cost2
    print("Suma wynosi: "+str(suma))
    print('I maja takie wsp: ')
    print(shortestWays)
    return shortestWays


bestway = search_for_shortest()

# drawing lines betweeen points
def draw_connesctions(list_of_best_ways):
    for xx in list_of_best_ways:
        if xx == list_of_best_ways[-1]:
            begin = list_of_best_ways[list_of_best_ways.index(0)]
            plt.plot([a[xx], a[begin]], [b[xx], b[begin]])
        else:
            nextPoint = list_of_best_ways[list_of_best_ways.index(xx)+1]
            plt.plot([a[xx], a[nextPoint]], [b[xx], b[nextPoint]])

draw_connesctions(bestway)
###   Teraz robimy Brutforce

print(" ------------------------- Tera brutforce --------------------------------- ")
# print("000000000000000000000000")
# print(cities_tmp)
comb = list(itertools.product([1,2,3], repeat=pointsNom-1))
# sss = set(comb)
# print(sss)
brave_new_list=[]

counter=0
for minilist in comb:
    min2 = set(minilist)
    if len(min2) == len(minilist):
        brave_new_list.append(minilist)
        print(minilist)
        # print(min2)
        print(">><<")
        counter = counter+1

    
print(brave_new_list)
print("liczba elementow tej Listy to: "+str(counter))

wayss=[]
for way in brave_new_list:
    cost=0
    way=list(way)
    way.insert(0, 0)
    for node in way:
        if node == way[-1]:
            xd = (a[node] - a[0])**2 + (b[node] - b[0])**2
            cost += math.sqrt(xd)
        else:
            nextPoint = way[way.index(node)+1]
            xd = (a[node] - a[nextPoint])**2 + (b[node] - b[nextPoint])**2
            cost += math.sqrt(xd)
    wayss.append(cost)
    print("koszt calosci: "+ str(cost)+ " --> "+str(way))
        
print(wayss)
print('')
plt.subplot(2, 1, 2)
plt.title('Brutforce')
best = brave_new_list[wayss.index(min(wayss))]
best=list(best)
best.insert(0, 0)
print(best)
draw_connesctions(best)

plt.show()

