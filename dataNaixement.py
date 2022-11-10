#Importem data actual
from datetime import date

#Funcio per calcular edad
def calcularEdad(yyyy,mm,dd):
    avui = date.today()
    edad = int(avui.year) - int(yyyy) - ((int(avui.month), int(avui.day)) < (int(mm), int(dd)))
    return edad
#Demanem data de neixement
any = input("En quin any vas neixer? (YYYY)")
mes = input("En quin mes vas neixer? (MM)")
dia = input("En quin dia vas neixer? (DD)")

#Mostrem edad per pantalla
print("La teva edad actual es: " + str(calcularEdad(any,mes,dia)))