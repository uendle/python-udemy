import sys

lista= [i for i in range(100000)]
print(lista)

iterator = iter(lista)


print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

generator = (i for i in range(10000))

for i in generator:
    print(i)

print('tamanho da lista= ',sys.getsizeof(lista))
print('tamanho do generator= ',sys.getsizeof(generator))




def genera(n=0 , max= 10):
#     yield 1
#     print('parando em ')
#     yield 2
#     print('parando em ')
#     yield 3
#     print('parando em ')

# for i in genera():
#     print('--------------',i,sep='\n')


    while True:
        yield n
        n+= 1

        if n >= max:
            return

# gen= genera(max=1000)

for i in genera(max=100):
    print(i)