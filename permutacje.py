from math import factorial


def permutations(l):
    permutations = []
    length = len(l)
    for x in range(factorial(length)):
        available = list(l)
        newPermutation = []
        for radix in range(length, 0, -1):
            placeValue = factorial(radix-1)
            index = x/placeValue
            newPermutation.append(available.pop(index))
            x -= index*placeValue
        permutations.append(newPermutation)
    return permutations


print(permutations(range(3)))

print()
# def make_list(str):
#     list = []
#     for char in str:
#         list.append(int(char))
#     return list


# def permutations(head, tail=''):
#     list_of_perms=[]
#     if len(head) == 0:
#         perm = (make_list(tail))
#         print(perm)
#         list_of_perms.append(perm)
        
#     else:
#         for i in range(len(head)):
#             permutations(head[0:i] + head[i+1:], tail+head[i])

    

# print(permutations("12345"))
# print()


def permutList(lista):
    if not lista:
        return [[]]
    res = []
    for e in lista:
        temp = lista[:]
        temp.remove(e)
        nw = [[e] + r for r in permutList(temp)]
        # if len(nw) == len(lista):
        #     print(nw)
            
        res.extend(nw)
    # print(res)a
            

    return res

permsall = permutList([1,2,3,4])
print(permsall)

# for perm in permsall:
#     print(perm)


print()
listaaa=[11,22,33,44,55,66]
print(listaaa[:])
listaaa.remove(22)
print(listaaa[:])
listaaa.extend([15,11])
print(listaaa[:])
listaaa.extend([a for a in listaaa])
print(listaaa[:])
lis = list(reversed(listaaa))
print(lis)
# print(make_list("123456"))

