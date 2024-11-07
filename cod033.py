from functools import reduce


lista= [
    {'nome':'pera','valor':2},
    {'nome':'uva','valor':4},
    {'nome':'maca','valor':6},
    {'nome':'abacaxi','valor':8},
]

total = reduce(
    lambda a, b :a + b['valor'],#a --> valor inicial do acumulador --0
    lista,#lista de que sera passada item a item
    0#valor inicial do acumulador
)
print(total)