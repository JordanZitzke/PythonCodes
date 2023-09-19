# Formatações de strings

a = 'A'
b = 'B'
c = 1.111

# As chaves são referentes aos indices dos valores, ex: {} vai printar 'A' primeiro
# Pode ser colocado o valor do indice dentro das chaves
string = 'a = {} b = {} c = {:.2f}'
formato = string.format(a, b, c)

print(formato)

