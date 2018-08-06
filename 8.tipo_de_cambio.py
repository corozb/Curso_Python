def foreign_exchange_calculator(ammount):
    vcop = float(input("Valor de COP al día de hoy: "))
    return str(ammount * vcop)

def run():
    print("C A L C U L A D O R A  D E  D I V I S A S ")
    print("Convierte pesos mexicanos a pesos colombianos")
    print("")
    ammount = float(input("Ingresa la cantidad de MXN para convertir a COP: "))
    result = foreign_exchange_calculator(ammount)
    print('Por tus ${} pesos mexicanos recibes ${} pesos colombianos'.format(ammount,result))
    print('')

if __name__== '__main__':
    run()
    print('GASTALOS SABIAMENTE')



#Se podría realizar la calcula de ésta forma sencilla:
#print("C A L C U L A D O R A  D E  D I V I S A S ")
#print("Convierte pesos mexicanos a pesos colombianos")
#print("")
#ammount = float(input("Ingresa la cantidad de MXN para convertir a COP: "))
#vcop = int(input("Valor de COP al día de hoy: "))
#saldo = str(ammount * vcop)
#print("Tienes un total de: $" + saldo + " pesos colombianos")
