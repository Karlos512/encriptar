import os

fichero = open('mensajeEncriptado.txt')
lineas = fichero.readlines()
LineaMensaje = []
nuevo = []
for linea in lineas:
    LineaMensaje.append(linea)

print (LineaMensaje[3])

list_Mensaje = LineaMensaje[3]
arreglo = list(list_Mensaje)

aux=1
for i in range(0,len(arreglo)):
    if i < (len(arreglo)-1):
        tamaño=len(arreglo)
        a=i+1
        if arreglo[i] == arreglo[a]:
            nuevo.append(i)
    else:
        for i in range(0,len(nuevo)):
            if i == 0:
                arreglo.pop(0)
            else:
                indice = nuevo[i] - aux 
                arreglo.pop(indice)
                aux=aux+1
    
            
cadenaReducida="".join(arreglo)

file = open("mensajeDescifrado.txt", "w")

print(type(LineaMensaje[2]))
print(type(cadenaReducida))

existeM1=LineaMensaje[1] in cadenaReducida
existeM2=LineaMensaje[2] in cadenaReducida

file.write(str(existeM1) + os.linesep)
file.write(str(existeM2))
file.close()


    

