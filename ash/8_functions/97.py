#
# * 97. Default Parameters

# ! O argumento não padrão segue o argumento padrão (parametros default ficam por ultimo)

def area(radius, pi=3.14): # //, po):
    print(pi*radius*radius)

area(10)