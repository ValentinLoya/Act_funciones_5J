print("ejemplo de funciones")
# declarando funciones 
def hola():
    print("Alguien uso la funcion hola")
def chat(mensa):
    print(f"chat {mensa}")
def ellacontesta(mensa):
    print(f"chat ella :{mensa}")
def escribenombre(ap,n):
    print(f"tu nombre completo es : {n} {ap}")
def suma(a,b):
    s=a+b 
    return s
def resta(a,b):
    s=a-b 
    return s
def mult(a,b):
    s=a*b 
    return s
def div(a,b):
    s=a/b 
    return s
#llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Valentin","Loya")
print("operaciones basicas")
print("operacion suma")
c1=int(input("ingresa un numero: "))
c2=int(input("ingresa un numero: "))
damesuma=suma(c1,c2)
print(f"la suma de {c1} + {c2} = {damesuma}")
print("operacion resta")
c3=int(input("ingresa un numero: "))
c4=int(input("ingresa un numero: "))
dameresta=resta(c3,c4)
print(f"la resta de: {c3} - {c4} = {dameresta}")
print("operacion multiplicacion")
c5=int(input("ingresa un numero: "))
c6=int(input("ingresa un numero: "))
damemult=mult(c5,c6)
print(f"la multiplicacion de: {c5} * {c6} = {damemult}")
print("operacion division")
c7=int(input("ingresa un numero: "))
c8=int(input("ingresa un numero: "))
damediv=div(c7,c8)
print(f"la division de: {c7} / {c8} = {damediv}")