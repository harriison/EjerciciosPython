import json

cotizacion=str(input())
cotizacion=json.loads(cotizacion)
listado = str(input()).split(" ")
valorAPagar= int()
articulosEncontrados = str()

for parte in listado:
    if parte in cotizacion:
        valorAPagar+= cotizacion[parte]
        articulosEncontrados += parte+" "

print(str(valorAPagar))
print (articulosEncontrados)
