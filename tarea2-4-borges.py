# 4to ejemplo Contar las palabras y Agregar datos a un nuevo archivo
f = open("las_ruinas_circulares.txt","r")
lineas = []
for l in f:
    if l != '\n':
        l = l[:-1] # remover \n residual
        l = l.rstrip() # remover espacios al final
        l = l.lower() # colocar todo el texto en minúsculas     
        lineas.append(l)
f.close # esto es opcional

print(lineas)
titulo = lineas[0].upper()
autor = lineas[1].upper()
print('título del libro:', titulo)
print('Autor:', autor)
print("Cantidad de líneas:",len(lineas))

# eliminar título y Autor
lineas.pop(0)
lineas.pop(0)

# extraer palabras
texto = '' # concatenar lineas en una unica variable texto
for l in lineas:
    texto = texto + l + ' '
print(texto)
palabras = texto.split(' ')
palabras.pop(-1) # eliminar último elemento en blanco de la lista
print(palabras)

# crear un diccionario con las palabras y la cantidad de apariciones
conteo = {}
for p in palabras:
    ind = palabras.index(p) # obtengo el índice de la palabra en la lista
    puntuacion_rmv = p[-1] # obtengo último carater de la palabra
    if puntuacion_rmv == ',' or puntuacion_rmv == '.': # si la palabra finaliza con puntuacion reasigno la palabra a la lista eliminando la puntuación
        palabras[ind] = p[:-1]

palabras_lista = palabras
palabras_conj = set(palabras)
# contar las palabras
for p in palabras_conj:
    c = palabras_lista.count(p)
    #print(p,c)
    conteo[p] = c
print(conteo)

# otra forma de control de archivo
with open("resumen_del_libro.txt", "w") as f2:
    f2.write("Título: " + titulo + "\n")
    f2.write("Autor: " + autor + "\n")
    f2.write("Cantidad de líneas: " + str(len(lineas)) + "\n")
    f2.write("*"*40)   
    for p in palabras_conj:
        apariciones = conteo[p]
        f2.write("\nla palabra <" + p + "> aparece " + str(apariciones) + " veces")




