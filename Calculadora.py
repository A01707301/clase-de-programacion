def calcular_velocidad(distancia, tiempo):
    velocidad = distancia / tiempo
    return velocidad

def calcular_distancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo

def calcular_fuerza(masa, aceleracion):
    fuerza = masa * aceleracion 
    return fuerza

def calcular_masa(fuerza, aceleracion):
    masa = fuerza / aceleracion
    return masa

def calcular_aceleracion(fuerza, masa):
    aceleracion = fuerza / masa
    return aceleracion

def calcular_fuerza_normal(coeficiente_friccion_estatica, fuerza_friccion):
    fuerza_normal = coeficiente_friccion_estatica * fuerza_friccion
    return fuerza_normal

def calcular_fuerza_friccion(coeficiente_friccion_estatica, fuerza_normal):
    fuerza_friccion = coeficiente_friccion_estatica * fuerza_normal
    return fuerza_friccion

def calcular_suma_nc(suma_nc1, suma_nc2):
    suma_nc = suma_nc1 + suma_nc2
    return suma_nc

def calcular_resta_nc(resta_nc1, resta_nc2):
    resta_nc = resta_nc1 - resta_nc2
    return resta_nc

def suma_vectores(a1, a2, b1, b2):
    suma_v = (a1 + b1), (a2 + b2)
    return suma_v

def resta_vectores(a1, a2, b1, b2):
    resta_v = (a1 - b1), (a2 - b2)
    return resta_v

def calcular_km_a_m(kilometro):
    km_a_m = kilometro * 1000
    return km_a_m

def calcular_m_a_km(metro):
    m_a_km = metro / 1000
    return m_a_km

def calcular_kg_a_g(kilogramo):
    kg_a_g = kilogramo * 1000
    return kg_a_g

def calcular_g_a_kg(gramo):
    g_a_kg = gramo / 1000 
    return g_a_kg

def calcular_m_a_s(minuto):
    m_a_s = minuto * 60
    return m_a_s

def calcular_s_a_m(segundo):
    s_a_m = segundo / 60 
    return s_a_m

print("¿Qué deseas hacer?")
print("1. Usar el formulario")
print("2. Resolver una ecuación")
print("3. Conversión de unidades")

calculadora = int(input("Selecciona una opción (1/2/3): "))

while calculadora == 1:
    print("Formulario de física")
    print("1. Fuerzas")
    print("2. Movimiento")

    opcion_uno = int(input("Selecciona una opción (1/2/3): "))

    if opcion_uno == 1:
        print("1. Segunda Ley de Newton")
        print("2. Aceleración")
        print("3. Fricción")
        print("4. Fuerza centripeta")

        formulario = int(input("Selecciona una opción (1/2/3/4): "))

        if formulario == 1: 
            fuerza = calcular_fuerza(float(input("Masa: ")), float(input("Aceleración: ")))
            print(f"Fuerza: {fuerza} N")
        elif formulario == 2: 
            aceleracion = calcular_aceleracion(float(input("Fuerza: ")), float(input("Masa: ")))
            print(f"Aceleración: {aceleracion} m/s²")
        elif formulario == 3: 
            fuerza_normal = calcular_fuerza_normal(float(input("Coeficiente de fricción estática: ")), float(input("Fuerza de fricción: ")))
            print(f"Fuerza Normal: {fuerza_normal} N")
        elif formulario == 4:
            fuerza_centripeta = calcular_fuerza(float(input("Masa: ")), float(input("Aceleración centrípeta: ")))
            print(f"Fuerza Centrípeta: {fuerza_centripeta} N")
        else: 
            print("No insertaste una opción válida")

    elif opcion_uno == 2:
        print("1. Movimiento rectilíneo uniforme")
        print("2. Movimiento parabólico")
        print("3. Movimiento de caída libre")
        print("4. Movimiento circular")

        opcion_seis = int(input("Selecciona una opción (1/2/3/4): "))

        if opcion_seis == 1:
            velocidad = calcular_velocidad(float(input("Distancia: ")), float(input("Tiempo: ")))
            print(f"Velocidad: {velocidad} m/s")
        elif opcion_seis == 2:
            tiempo_vuelo = calcular_tiempo(float(input("Altura máxima: ")), float(input("Aceleración debido a la gravedad: ")))
            print(f"Tiempo de vuelo: {tiempo_vuelo} s")
        elif opcion_seis == 3:
            tiempo_caida = calcular_tiempo(float(input("Altura desde la que cae: ")), float(input("Aceleración debido a la gravedad: ")))
            print(f"Tiempo de caída: {tiempo_caida} s")
        elif opcion_seis == 4:
            velocidad = calcular_velocidad(float(input("Radio: ")), float(input("Aceleración centrípeta: ")))
            print(f"Velocidad: {velocidad} m/s")
        else: 
            print("No insertaste una opción válida")

    else:
        print("No insertaste una opción válida")

while calculadora == 2: 
    print("Calculadora de Física")
    print("1. Distancia, Velocidad o Tiempo")
    print("2. Fuerza, Masa, Aceleración")
    print("3. Fuerza normal o fuerza de fricción")
    print("4. Notación científica Suma/Resta con exponentes iguales")
    print("5. Suma y resta de vectores")

    opciones = int(input("Selecciona una opción (1/2/3/4/5): "))
    if opciones == 1:
        print("1. Calcular velocidad")
        print("2. Calcular distancia")
        print("3. Calcular tiempo")
        
        opcion_dos = int(input("Selecciona una opción (1/2/3): "))
        
        if opcion_dos == 1:
            distancia = float(input("Insertar la distancia: "))
            tiempo = float(input("Insertar el tiempo: "))
            velocidad = calcular_velocidad(distancia, tiempo)
            print(f"La velocidad es {velocidad} m/s ")

        elif opcion_dos == 2:
            tiempo = float(input("Insertar el tiempo: "))
            velocidad = float(input("Insertar la velocidad: "))
            distancia = calcular_distancia(velocidad, tiempo)
            print(f"La distancia es {distancia} m ")

        elif opcion_dos == 3:
            distancia = float(input("Insertar la distancia: "))
            velocidad = float(input("Insertar la velocidad: "))
            tiempo = calcular_tiempo(distancia, velocidad)
            print(f"El tiempo es {tiempo} s ")

        else: 
            print("No insertaste una opción válida")

    elif opciones == 2:
        print("1. Calcular Fuerza")
        print("2. Calcular Masa")
        print("3. Calcular Aceleración")

        opcion_tres = int(input("Selecciona una opción (1/2/3): "))

        if opcion_tres == 1:
            masa = float(input("Insertar la masa: "))
            aceleracion = float(input("Insertar la aceleración: "))
            fuerza = calcular_fuerza(masa, aceleracion)
            print(f"La fuerza es {fuerza} N")

        elif opcion_tres == 2:
            fuerza = float(input("Insertar la fuerza: "))
            aceleracion = float(input("Insertar la aceleración: "))
            masa = calcular_masa(fuerza, aceleración)
            print(f"La masa es: {masa} kg")

        elif opcion_tres == 3:
            fuerza = float(input("Insertar la fuerza: "))
            masa = float(input("Insertar la masa: "))
            aceleracion = calcular_aceleración(fuerza, masa)
            print(f"La aceleración es: {aceleracion} m/s²")

        else: 
            print("No insertaste una opción válida")

    elif opciones == 3:
        print("1. Calcular la fuerza normal")
        print("2. Calcular la fuerza de fricción")

        opcion_cuatro = int(input("Selecciona una opción (1/2): "))

        if opcion_cuatro == 1:
            fuerza_friccion = float(input("Insertar la fuerza de fricción: "))
            coeficiente_friccion_estatica = float(input("Insertar el coeficiente de fricción estática: "))
            fuerza_normal = calcular_fuerza_normal(coeficiente_friccion_estatica, fuerza_friccion)
            print(f"La fuerza normal es: {fuerza_normal} N")

        elif opcion_cuatro == 2:
            fuerza_normal = float(input("Insertar la fuerza normal: "))
            coeficiente_friccion_estatica = float(input("Insertar el coeficiente de fricción estática: "))
            fuerza_fricción = calcular_fuerza_friccion(coeficiente_friccion_estatica, fuerza_normal)
            print(f"La fuerza de fricción es: {fuerza_fricción} N")
        
    elif opciones == 4: 
        print("1. Suma de notación científica con exponentes iguales")
        print("2. Resta de notación científica con exponentes iguales")

        opcion_siete = int(input("Selecciona una opción (1/2): "))
        if opcion_siete == 1:
            suma_nc1 = float(input("Insertar el primer número entero: "))
            suma_nc_ex = float(input("Insertar el primer exponente: "))
            suma_nc2 = float(input("Insertar el segundo número entero: "))
            suma2_nc_ex = float(input("Insertar el segundo exponente: "))
        
            if suma_nc_ex == suma2_nc_ex:
                suma_nc = calcular_suma_nc(suma_nc1, suma_nc2)
                print(f"La suma es: {suma_nc} x10^{suma_nc_ex}")
               
        elif opcion_siete ==2:
                resta_nc1 = float(input("Insertar el primer número entero: "))
                resta_nc_ex = float(input("Insertar el primer exponente: "))
                resta_nc2 = float(input("Insertar el segundo número entero: "))
                resta2_nc_ex = float(input("Insertar el segundo exponente: "))
        
                if resta_nc_ex == resta2_nc_ex:
                    resta_nc = calcular_resta_nc(resta_nc1, resta_nc2)
                    print(f"La resta es: {resta_nc} x10^{resta_nc_ex}")

    elif opciones == 5:
        print ("1. Suma de vectores")
        print("2. Resta de vectores")

        opcion_ocho = int(input("Selecciona una opción (1/2): "))

        if opcion_ocho == 1:
            a1 = float(input("Insertar el primer número x1: "))
            a2 = float(input("Insertar el primer número x2: "))
            b1 = float(input("Insertar el primer número y1: "))
            b2 = float(input("Insertar el primer número y2: "))

            suma_v = suma_vectores(a1, a2, b1, b2)
            print(f"La suma de vectores es: {suma_v}")

        if opcion_ocho == 2:
            a1 = float(input("Insertar el primer número x1: "))
            a2 = float(input("Insertar el primer número x2: "))
            b1 = float(input("Insertar el primer número y1: "))
            b2 = float(input("Insertar el primer número y2: "))

            resta_v = resta_vectores(a1, a2, b1, b2)
            print(f"La resta de vectores es: {resta_v}")

    else: 
        print("No insertaste una opción válida")

while calculadora == 3:
    print("1. Convertir kilómetros a metros")
    print("2. Convertir metros a kilómetros")
    print("3. Convertir kilogramos a gramos")
    print("4. Convertir gramos a kilogramos")
    print("5. Convertir minutos a segundos")
    print("6. Convertir segundos a minutos")

    opcion_cinco = int(input("Selecciona una opción (1/2/3/4/5/6): "))

    if opcion_cinco == 1:
        kilometro = float(input("Insertar los kilómetros: "))
        metro = calcular_km_a_m(kilometro)
        print(f"La conversión a metros es {metro} m")

    elif opcion_cinco == 2:
        metro = float(input("Insertar los metros: "))
        kilometro = calcular_m_a_km(metro)
        print(f"La conversión a kilómetros es {kilometro} km")
    
    elif opcion_cinco == 3:
        kilogramo = float(input("Insertar los kilogramos: "))
        gramo = calcular_kg_a_g(kilogramo)
        print(f"La conversión a gramos es {gramo} g")

    elif opcion_cinco == 4:
        gramo = float(input("Insertar los gramos: "))
        kilogramo = calcular_g_a_kg(gramo)
        print(f"La conversión a kilogramos es {kilogramo} kg")
    
    elif opcion_cinco == 5:
        minuto = float(input("Insertar los minutos: "))
        segundo = calcular_m_a_s(minuto)
        print(f"La conversión a segundos es {segundo} s")

    elif opcion_cinco == 6:
        segundo = float(input("Insertar los segundos: "))
        minuto = calcular_s_a_m(segundo)
        print(f"La conversión a minutos es {minuto} min")        

    else: 
        print("No insertaste una opción válida")

else: 
    print("No insertaste una opción válida")
