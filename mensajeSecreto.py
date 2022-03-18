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
    
            
        print ("".join(arreglo))
cadenaReducida="".join(arreglo)
print(cadenaReducida)
print(LineaMensaje[1])
pala="".join(LineaMensaje[1])

print (pala in cadenaReducida)
print ("CeseAlFuego" in "XcamakCeseAlFuegoDLKmN")

    

