numero1 = int(input("Dime un número "))
numero2 = int(input("Dime otro número "))
operacion = input("Ahora dime la operación que quierees realizar (+,-,*,/) ")
if(operacion=="+"):
    print(numero1+numero2)
elif(operacion=="-"):
    print(numero1-numero2)
elif(operacion=="*"):
    print(numero1*numero2)
elif(operacion=="/"):
    print(numero1/numero2)
else:
    print("La operación que has pedido no es valida")