#Esta matriz guarda el menu de toda la calculadora
opciones = [
    ["Usar el formulario", "Resolver una ecuación", "Conversión de unidades"],
    ["Fuerzas", "Movimiento"],
    ["Segunda Ley de Newton", "Aceleración", "Fricción", "Fuerza centripeta"],
    ["Movimiento rectilíneo uniforme", "Movimiento parabólico", "Movimiento de caída libre", "Movimiento circular"],
    ["Distancia, Velocidad o Tiempo", "Fuerza, Masa, Aceleración", "Fuerza normal o fuerza de fricción",
     "Notación científica Suma/Resta con exponentes iguales", "Suma y resta de vectores"],
    ["Calcular velocidad", "Calcular distancia", "Calcular tiempo"],
    ["Calcular Fuerza", "Calcular Masa", "Calcular Aceleración"],
    ["Calcular la fuerza normal", "Calcular la fuerza de fricción"],
    ["Suma de notación científica con exponentes iguales", "Resta de notación científica con exponentes iguales"],
    ["Suma de vectores", "Resta de vectores"],
    ["Convertir kilómetros a metros", "Convertir metros a kilómetros", "Convertir kilogramos a gramos",
     "Convertir gramos a kilogramos", "Convertir minutos a segundos", "Convertir segundos a minutos"]
]
#Define la formula de la velocidad
def calcular_velocidad(distancia, tiempo):
    velocidad = distancia / tiempo
    return velocidad

#Define la formula de la distancia
def calcular_distancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

#Define la formula del tiempo
def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo

#Define la formula de la fuerza
def calcular_fuerza(masa, aceleracion):
    fuerza = masa * aceleracion
    return fuerza

#Define la formula de la masa
def calcular_masa(fuerza, aceleracion):
    masa = fuerza / aceleracion
    return masa

#Define la formula de la aceleración
def calcular_aceleracion(fuerza, masa):
    aceleracion = fuerza / masa
    return aceleracion

#Define la formula de la fuerza normal
def calcular_fuerza_normal(coeficiente_friccion_estatica, fuerza_friccion):
    fuerza_normal = coeficiente_friccion_estatica * fuerza_friccion
    return fuerza_normal

#Define la formula de la fuerza de fricción
def calcular_fuerza_friccion(coeficiente_friccion_estatica, fuerza_normal):
    fuerza_friccion = coeficiente_friccion_estatica * fuerza_normal
    return fuerza_friccion

#Define la formula de suma de notación científica
def calcular_suma_nc(suma_nc1, suma_nc2):
    suma_nc = suma_nc1 + suma_nc2
    return suma_nc

#Define la formula de resta de notación científica
def calcular_resta_nc(resta_nc1, resta_nc2):
    resta_nc = resta_nc1 - resta_nc2
    return resta_nc

#Define la formula de suma de vectores
def suma_vectores(a1, a2, b1, b2):
    suma_v = (a1 + b1), (a2 + b2)
    return suma_v

#Define la formula de resta de vectores
def resta_vectores(a1, a2, b1, b2):
    resta_v = (a1 - b1), (a2 - b2)
    return resta_v

#Define la formula para convertir unidades de kilometro a metro
def calcular_km_a_m(kilometro):
    km_a_m = kilometro * 1000
    return km_a_m

#Define la formula para convertir unidades de metro a kilometro
def calcular_m_a_km(metro):
    m_a_km = metro / 1000
    return m_a_km

#Define la formula para convertir unidades de kilogramo a gramo
def calcular_kg_a_g(kilogramo):
    kg_a_g = kilogramo * 1000
    return kg_a_g

#Define la formula para convertir unidades de gramo a kilogramo
def calcular_g_a_kg(gramo):
    g_a_kg = gramo / 1000
    return g_a_kg

#Define la formula para convertir unidades de minuto a segundo
def calcular_m_a_s(minuto):
    m_a_s = minuto * 60
    return m_a_s

#Define la formula para convertir unidades de segundo a minuto
def calcular_s_a_m(segundo):
    s_a_m = segundo / 60
    return s_a_m

#Muestra un menú con opciones
def print_opciones(lista_de_opciones):
    for i, opcion in enumerate(lista_de_opciones, start=1):
        print(f"{i}. {opcion}")

#Define el menú principal para que le aparezca al usuario si desea regresar al menu o no
def regresar_al_menu_principal():
    while True:
        menu = input("¿Deseas regresar al menú principal? (s/n): ")
        if menu == 's':
            return True
        elif menu == 'n':
            return False
        else:
            print("Opción no válida. Por favor, ingresa 's' para regresar al menú principal o 'n' para salir.")

#Define el menú principal
def menu_principal():
    global opciones
    while True: #Ciclo While para que cuando sea verdadero, ejecute todo lo siguiente
        print("¿Qué deseas hacer?") #Pregunta al usuario que desea hacer en la calculadora
        print_opciones(opciones[0]) #Va a la matriz y selecciona la primera opción que es 0
        calculadora = int(input("Selecciona una opción (1/2/3): ")) #Le da a elegir al usuario que quiere hacer con las 3 opciones de la matriz

        if calculadora == 1: #La elección sobre elegir el formulario de la calculadora
            print("Formulario de física")
            print_opciones(opciones[1]) #Va a la matriz y selecciona la segunda opcion 1
            opcion_uno = int(input("Selecciona una opción (1/2): ")) #Da a elegir entre las 2 opciones del formulario

            if opcion_uno == 1:
                print_opciones(opciones[2]) #Va a la matriz y selecciona la opcion 3 que es 2

                formulario = int(input("Selecciona una opción (1/2/3/4): ")) #Le da a elegir al usuario entre las 4 opciones del formulario de fuerzas

                if formulario == 1: #Imprime la formula de fuerza
                    fuerza = (int(input("\n F=m*a"))) 
                elif formulario == 2: #Imprime la formula de aceleración
                    aceleracion = (int(input("\n a = vf-v0/tf-t0 \n a=vf-v0/t \n xf = x0 + v0t + 1/2 at^2")))
                elif formulario == 3: #Imprime la formula de fuerza de fricción
                    fuerza_friccion = (int(input("\n Fr=μN")))
                elif formulario == 4: #Imprime la formula de fuerza centripeta
                    fuerza_centripeta = (int(input("\n F=mat \n at = v^2/R \n at = w^2R")))

                else:
                    print("No insertaste una opción válida") #Si selecciona una opción incorrecta, aparece esta opción

            elif opcion_uno == 2:
                print_opciones(opciones[3]) #Va a la matriz y selecciona la opción 3

                opcion_seis = int(input("Selecciona una opción (1/2/3/4): ")) #El usuario elije una opción sobre las formulas del movimiento

                if opcion_seis == 1: #Imprime la formula del movimiento rectilineo
                    rectilineo = input("\n x=vt \n x=x0+vt \n v= x1-x2/t1-t2 \n v=v0+at \n x= x0+v0t+1/2 at2")
                elif opcion_seis == 2: #Imprime la formula del movimiento parabólico
                    parabolico = input("\n vx=v0cosα \n vy=v0sina \n x(t)=x0+vxt \n y=y0 + vyt - 1/2gt2 \n y= vy0 -gt = v0 sin a -gt")
                elif opcion_seis == 3: #Imprime la formula de caida libre
                    caida_libre = input("y= y0 + v0t - 1/2 gt2 \n v=v0 - gt \n y= h - 1/2 gt2")
                elif opcion_seis == 4: #Imprime la formula del movimiento circular
                    circular = input("∣v1∣=∣v2∣ \n w= θ2-θ1/t2-t1 \n w=dθ/dt \n w=2π/T \n v=wR \n ac= v2/R \n ac=w2R \n θf=θ0+wt \n w=w0 + at \n t=w - w0/a")
                else:
                    print("No insertaste una opción válida") #Si selecciona una opción incorrecta, aparece esta opción


            elif opcion_uno == 3:
                break  # Volver al menú principal

            else:
                print("No insertaste una opción válida") #Si selecciona una opción incorrecta, aparece esta opción

        elif calculadora == 2: #De la calculadora, le da a elegir la calculadora de física
            print("Calculadora de Física") 
            print_opciones(opciones[4]) #Va a la matriz y selecciona la opción 4
            opcion = int(input("Selecciona una opción (1/2/3/4/5): ")) #Selecciona una de las 5 opciones sobre la calculadora

            if opcion == 1:
                print_opciones(opciones[5]) #Va a la matriz y selecciona la opción 5 
                opcion_dos = int(input("Selecciona una opción (1/2/3): "))

                if opcion_dos == 1: #Elegir para seleccionar la velocidad insertando la distancia y el tiempo
                    distancia = float(input("Insertar la distancia: "))
                    tiempo = float(input("Insertar el tiempo: "))
                    velocidad = calcular_velocidad(distancia, tiempo)
                    print(f"La velocidad es {velocidad} m/s ") #Imprime el resultado de la velocidad

                elif opcion_dos == 2: #Elegir para seleccionar la distancia insertando el tiempo y la velocidad
                    tiempo = float(input("Insertar el tiempo: "))
                    velocidad = float(input("Insertar la velocidad: "))
                    distancia = calcular_distancia(velocidad, tiempo)
                    print(f"La distancia es {distancia} m ") #Imprime el resultado de la distancia

                elif opcion_dos == 3: #Elegir para seleccionar el tiempo insertando la distancia y la velocidad
                    distancia = float(input("Insertar la distancia: "))
                    velocidad = float(input("Insertar la velocidad: "))
                    tiempo = calcular_tiempo(distancia, velocidad)
                    print(f"El tiempo es {tiempo} s ") #Imprime el resultado del tiempo

                else:
                    print("No insertaste una opción válida")  #Si selecciona una opción incorrecta, aparece esta opción

            elif opcion == 2: #Selecciona la opción sobre elegir sacar entre la masa, aceleración y fuerza
                print_opciones(opciones[6]) #Va a la matriz y selecciona la opción 6
                opcion_tres = int(input("Selecciona una opción (1/2/3): ")) #Pide elegir entre la opción de masa, aceleracion y fuerza

                if opcion_tres == 1: #Da a elegir sobre sacar la fuerza
                    masa = float(input("Insertar la masa: ")) #Se inserta la fuerza
                    aceleracion = float(input("Insertar la aceleración: ")) #Se inserta la aceleracion
                    fuerza = calcular_fuerza(masa, aceleracion)  #Se usa la formula de la definición de la fuerza
                    print(f"La fuerza es {fuerza} N") #Da como resultado la fuerza

                elif opcion_tres == 2: #Da a elegir sobre sacar la masa
                    fuerza = float(input("Insertar la fuerza: ")) #Se inserta la fuerza
                    aceleracion = float(input("Insertar la aceleración: ")) #Se inserta la aceleración
                    masa = calcular_masa(fuerza, aceleracion) #Se usa la formula de la definición de la masa
                    print(f"La masa es: {masa} kg") #Da como resultado la masa

                elif opcion_tres == 3: #Da a elegir sobre sacar la aceleración
                    fuerza = float(input("Insertar la fuerza: ")) #Se inserta la fuerza
                    masa = float(input("Insertar la masa: ")) #Se inserta la masa
                    aceleracion = calcular_aceleracion(fuerza, masa) #Se usa la formula de la definición de la aceleración
                    print(f"La aceleración es: {aceleracion} m/s²") #Da como resultado de la aceleración 

                else:
                    print("No insertaste una opción válida") #Si selecciona una opción incorrecta, aparece esta opción

            elif opcion == 3: #Da a seleccionar para  calcular la fuerza de fricción o la fuerza normal
                print_opciones(opciones[7]) #Va a la matriz y selecciona la opción 7
                opcion_cuatro = int(input("Selecciona una opción (1/2): "))

                if opcion_cuatro == 1: #Da a elegir para sacar la fuerza normal
                    fuerza_friccion = float(input("Insertar la fuerza de fricción: ")) #Se inserta la fuerza de fricción
                    coeficiente_friccion_estatica = float(input("Insertar el coeficiente de fricción estática: ")) #Se inserta la coeficiente de fricción estática
                    fuerza_normal = calcular_fuerza_normal(coeficiente_friccion_estatica, fuerza_friccion) #Se usa la formula de la definición de la fuerza normal
                    print(f"La fuerza normal es: {fuerza_normal} N") #Da el resultado de la fuerza normal

                elif opcion_cuatro == 2: #Da a elegir para sacar la fuerza de fricción
                    fuerza_normal = float(input("Insertar la fuerza normal: ")) #Se inserta la fuerza normal
                    coeficiente_friccion_estatica = float(input("Insertar el coeficiente de fricción estática: ")) #Se inserta el coeficiente de fricción estática
                    fuerza_friccion = calcular_fuerza_friccion(coeficiente_friccion_estatica, fuerza_normal) #Se usa la formula de la definición de la fuerza de fricción
                    print(f"La fuerza de fricción es: {fuerza_friccion} N") #Da el resultado de la fuerza de fricción

            elif opcion == 4: #Da a elegir sobre sumar o restar notación científica
                print_opciones(opciones[8]) #Va a la matriz y selecciona la opción 8
                opcion_siete = int(input("Selecciona una opción (1/2): ")) #Se selecciona entre suma o resta de notación científica

                if opcion_siete == 1:  #Da a elegir entre suma de notación cientifica
                    suma_nc1 = float(input("Insertar el primer número entero: ")) #Se inserta el primer numero
                    suma_nc_ex = float(input("Insertar el primer exponente: ")) #Se inserta el primer exponente
                    suma_nc2 = float(input("Insertar el segundo número entero: ")) #Se inserta el segundo numero
                    suma2_nc_ex = float(input("Insertar el segundo exponente: ")) #Se inserta el segundo exponente

                    if suma_nc_ex == suma2_nc_ex:
                        suma_nc = calcular_suma_nc(suma_nc1, suma_nc2) #Se usa la formula de la definición de calcular la suma de exponentes
                        print(f"La suma es: {suma_nc} x10^{suma_nc_ex}") #Se resuelve la suma de exponentes

                elif opcion_siete == 2: #Da a elegir entre resta de notación cientifica
                    resta_nc1 = float(input("Insertar el primer número entero: ")) #Se inserta el primer numero
                    resta_nc_ex = float(input("Insertar el primer exponente: ")) #Se inserta el primer exponente
                    resta_nc2 = float(input("Insertar el segundo número entero: ")) #Se inserta el segundo numero
                    resta2_nc_ex = float(input("Insertar el segundo exponente: ")) #Se inserta el segundo exponente

                    if resta_nc_ex == resta2_nc_ex:
                        resta_nc = calcular_resta_nc(resta_nc1, resta_nc2) #Se usa la formula de la definición de calcular la resta de exponentes
                        print(f"La resta es: {resta_nc} x10^{resta_nc_ex}") #Se resuelve la resta de exponentes

            elif opcion == 5: 
                print_opciones(opciones[9]) #Va a la matriz y selecciona la opción 9
                opcion_ocho = int(input("Selecciona una opción (1/2): ")) #Da a elegir para sumar o restar vectores

                if opcion_ocho == 1:
                    a1 = float(input("Insertar el primer número x1: ")) #Se inserta el primer numero x1
                    a2 = float(input("Insertar el primer número x2: ")) #Se inserta el segundo numero x2
                    b1 = float(input("Insertar el primer número y1: ")) #Se inserta el segundo numero y1
                    b2 = float(input("Insertar el primer número y2: ")) #Se inserta el segundo numero y2

                    suma_v = suma_vectores(a1, a2, b1, b2)
                    print(f"La suma de vectores es: {suma_v}") #Se da el resultado de la suma de vectores

                if opcion_ocho == 2:
                    a1 = float(input("Insertar el primer número x1: ")) #Se inserta el primer numero x1
                    a2 = float(input("Insertar el primer número x2: ")) #Se inserta el segundo numero x2
                    b1 = float(input("Insertar el primer número y1: ")) #Se inserta el segundo numero y1
                    b2 = float(input("Insertar el primer número y2: ")) #Se inserta el segundo numero y2

                    resta_v = resta_vectores(a1, a2, b1, b2)
                    print(f"La resta de vectores es: {resta_v}") #Se da el resultado de la resta de vectores

            else:
                print("No insertaste una opción válida") #Si selecciona una opción incorrecta, aparece esta opción

        elif calculadora == 3: #Da la opción para hacer la conversión de unidades
            print_opciones(opciones[10]) #Va a la matriz y selecciona la opción 10
            opcion_cinco = int(input("Selecciona una opción (1/2/3/4/5/6): ")) #Selecciona una opción sobre la conversión de unidades

            if opcion_cinco == 1: #Se elige la conversión de kilometros a metros
                kilometro = float(input("Insertar los kilómetros: ")) #Se insertan los kilometros
                metro = calcular_km_a_m(kilometro) #Se hace la conversión a metros
                print(f"La conversión a metros es {metro} m") #Se da el resultado a metros

            elif opcion_cinco == 2: #Se elige la conversión de metros a kilometros
                metro = float(input("Insertar los metros: ")) #Se insertan los metros
                kilometro = calcular_m_a_km(metro) #Se hace la conversión a kilometros
                print(f"La conversión a kilómetros es {kilometro} km") #Se da el resultado a kilometros

            elif opcion_cinco == 3: #Se elige la conversión de kilogramos a gramos
                kilogramo = float(input("Insertar los kilogramos: ")) #Se insertan los kilogramos
                gramo = calcular_kg_a_g(kilogramo) #Se hace la conversion a gramos
                print(f"La conversión a gramos es {gramo} g") #Se da el resultado a gramos

            elif opcion_cinco == 4: #Se elige la conversión de gramos a kilogramos
                gramo = float(input("Insertar los gramos: ")) #Se insertan los gramos
                kilogramo = calcular_g_a_kg(gramo) #Se hace la conversion a kilogramos
                print(f"La conversión a kilogramos es {kilogramo} kg") #Se da el resultado a kilogramos

            elif opcion_cinco == 5:  #Se elige la conversión de minutos a segundos
                minuto = float(input("Insertar los minutos: ")) #Se insertan los minutos
                segundo = calcular_m_a_s(minuto) #Se hace la conversión a segundos
                print(f"La conversión a segundos es {segundo} s") #Se da el resultado de los segundos

            elif opcion_cinco == 6:  #Se elige la conversión de segundos a minutos
                segundo = float(input("Insertar los segundos: ")) #Se insertan los segundos
                minuto = calcular_s_a_m(segundo) #Se hace la conversión a minutos
                print(f"La conversión a minutos es {minuto} min") #Se da el resultado a minutos

            else:
                print("No insertaste una opción válida") #Si selecciona una opción incorrecta, aparece esta opción

        if not regresar_al_menu_principal(): #Aparece si se selecciona la opción de no querer regresar al menú principal
            print("Hasta luego") #Se imprime cuando no se quiere regresar al menu principal
            break #Se rompe el ciclo while

menu_principal()
