set1 = {1,2,3}
set2= {2,3,4}

set3= set1 | set2#uniao 
print(set3)

set3= set1 & set2#interseção
print(set3)

set3= set1 - set2#diferença
print(set3)

set3= set1 ^ set2#diferença simetrica
print(set3)


# def encontra_duplicado (lista):
#     l= set()
#     for item in lista:
#         if item in l:
#             return item
#         else:
#             l.add(item)
#     return -1

# print(encontra_duplicado([1,2,3,4,4,5]))