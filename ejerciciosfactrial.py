# factoriales con while
def factorial_while(numero)-> int:
    if numero==0 or numero==1:
        return 1
    while numero>1:
        return numero * factorial_while(numero-1)
print(factorial_while(5))


#factorial con for
def factorial_for(numero2)->int:
    facto=1
    for i in range(2 , numero2+1 ):
        facto *= i
    return facto
print(factorial_for(4))

#recursución de factorial
def factorial_recursión(numero3):
    if numero3 ==0 or numero3==1:
        return 1
    else:
        return numero3 *  factorial_recursión(numero3-1)
print(factorial_recursión(6))
