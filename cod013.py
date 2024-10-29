# def criar_saldacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}'
#     return saudar

# falar_bom_dia= criar_saldacao('boa tarde')
# falr_boa_noite= criar_saldacao('boa noite')

# for nome in ['uendle','lilian','bernardo']:
#     print(falar_bom_dia)
#     print(falr_boa_noite)
#     print(falar_bom_dia(nome))
#     print(falr_boa_noite(nome))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar= criar_multiplicador(2)
triplicar= criar_multiplicador(3)
quadruplicar= criar_multiplicador(4)

print(duplicar(5))
print(triplicar(6))
print(quadruplicar(7))