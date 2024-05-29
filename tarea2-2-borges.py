
# 2do ejemplo Remover líneas vacias
f = open("las_ruinas_circulares.txt","r")
lineas = []
for l in f:
    if l != '\n':
        l = l[:-1] # remover \n residual
        l = l.rstrip() # remover espacios al final
        lineas.append(l)

print(lineas)
print('título del libro:', lineas[0])
print('Autor:', lineas[1])

