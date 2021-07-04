lista = input().split(" ")
diccionario={}
repetidos=""
cantidad=0
anterior=lista[0]
simbolos=anterior+" "
for simbolo in lista:
    if simbolo != anterior:
        if cantidad > 0:
            repetidos+=str(cantidad)+" "     
        anterior = simbolo
        simbolos += simbolo+" "
        cantidad=1
    else:
        cantidad+=1
repetidos+=str(cantidad)        

print (lista)
print (simbolos)
print (repetidos)

