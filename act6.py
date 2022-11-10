#Crear una funció que, passat 2 paràmetres, els sumarà entre ells.
def suma(var1,var2):
    print("La suma del valor "+str(var1)+" més el valor "+str(var2)+" serà: "+str(var1)+"+"+str(var2)+"="+str(var1+var2))

# Cal tindre un arxiu main on cridi a la funció i, utilitzant input().
num1=int(input("1r. Indica un número enter per sumar: "))
num2=int(input("2n. Indica segón número enter per sumar: "))

#Cridem la funció
suma(num1,num2)
