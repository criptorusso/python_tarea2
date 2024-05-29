# 3er ejemplo Agregar datos a un nuevo archivo
f = open("las_ruinas_circulares.txt","r")

lineas = []

for l in f:
    if l != '\n':
        l = l[:-1] # remover \n residual
        l = l.rstrip() # remover espacios al final        
        lineas.append(l)

print(lineas)
titulo = lineas[0]
autor = lineas[1]
print('título del libro:', titulo)
print('Autor:', autor )
print("Cantidad de líneas:",len(lineas))

# abrir un archivo de texto para escritura
f2 = open("resumen_del_libro.txt", "w")
f2.write("Título: " + titulo + "\n")
f2.write("Autor: " + autor + "\n")
f2.write("Cantidad de líneas: " + str(len(lineas)))

