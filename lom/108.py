# 
# * 108. (Parte 1) Escopo de funções e módulos em Python + global
'''
escopo -> limite da influencia do codigo (D.S.)
'''

x = 1

def escopo():
    global x                # ! manipula o 'x' global
    x = 10                  # ! modifica o 'x' global de '1' (primeira declaracao) para '10'
    def escopo_local():
        y = 2
        print(x + y)
    escopo_local()
    return escopo_local

print(x)
escopo()
