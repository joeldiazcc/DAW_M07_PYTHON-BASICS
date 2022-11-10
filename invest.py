def invest():

    #Calers incial en euros
    initmoney = 100
    #porcentaje que s'incrementa cada any, es un 10%
    increment = initmoney * 1.1
    #posibilidad de hacer a 1.1
    #perido de tiempo
    totalmoney = increment * 7
    #Pasar el resultat de long a int
    parser = int(totalmoney)
    #Imprimir el total dels diners acumulats després de 7 anys
    #Resultado en int
    print('Al cap de 7 anys tindras ' + str(parser) +  ' de euros')
    #Resultado en tipus long
    print('Al cap de 7 anys tindras ' + str(totalmoney) +  ' de euros')
invest()

