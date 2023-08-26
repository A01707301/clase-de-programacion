def calcular_velocidad(distancia, tiempo):
    velocidad = distancia / tiempo
    return velocidad

def calcular_distancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo

print("¿Quieres formulario? o ¿Quieres resolver la ecuación?")
print("1. Formulario")
print("2. Resolver la ecuación")

calculadora = int(input("Selecciona una opción (1/2): "))

if calculadora == 1:
    print("Formulario de física")
    print("1. Segunda Ley de Newton")
    print("2. Aceleración")
    print("3. Fricción")
    print("4. Fuerza centripeta")

    formulario = int(input("Selecciona una opción (1/2/3/4): "))

    if formulario == 1: 
        Newton = input("F=ma")
    elif formulario == 2: 
        aceleracion = input(" \n a= Vf-Vo/tf-to \n a= Vf-Vo/t \n xf= xo + vot + 1/2 at2 ")
    elif formulario == 3: 
        friccion = input("\n Fr= μN \n Fr= μmg")
    elif formulario == 4:
        centripeta = input("\n F=mat \n F=v2/R")

elif calculadora == 2: 
    print("Calculadora de Física")
    print("1. Calcular velocidad")
    print("2. Calcular distancia")
    print("3. Calcular tiempo")

    opciones = int(input("Selecciona una opción (1/2/3): "))

    if opciones == 1:
        distancia = float(input("Insertar la distancia: "))
        tiempo = float(input("Insertar el tiempo: "))
        velocidad = calcular_velocidad(distancia, tiempo)
        print(f"La velocidad es {velocidad} m/s ")

    elif opciones == 2:
        tiempo = float(input("Insertar el tiempo: "))
        velocidad = float(input("Insertar la velocidad: "))
        distancia = calcular_distancia(velocidad, tiempo)
        print(f"La distancia es {distancia} m ")

    elif opciones == 3:
        distancia = float(input("Insertar la distancia: "))
        velocidad = float(input("Insertar la velocidad: "))
        tiempo = calcular_tiempo(distancia, velocidad)
        print(f"El tiempo es {tiempo} s ")

    else: 
        print("No insertaste un dato correcto, regresa al menú principal")

else: 
    print("No insertaste un dato correcto, regresa al menú principal")
