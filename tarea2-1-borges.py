
# 1er ejemplo obtener líneas
f = open("las_ruinas_circulares.txt","r")

lineas = []

for l in f:
    lineas.append(l)

print(lineas)
print('título del libro:', lineas[0])
print('Autor:', lineas[2]) # esta línea esta vacia, debe removerse ver ejemplo2
