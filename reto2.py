primeros = input()
nuevos = input()
ganados = input()
ganaPrimeros = 0
ganaNuevos = 0

for item in ganados :
    if item in primeros :
        ganaPrimeros+=1
    if item in nuevos :
        ganaNuevos+=1
        
    if ganaPrimeros > ganaNuevos :
        print("P",end="")
    elif ganaNuevos > ganaPrimeros :
        print("N",end="")
    else :
        print("E",end="")