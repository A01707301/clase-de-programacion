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

def calcular_masa(aceleracion, fuerza):
    masa = fuerza / aceleracion
    return masa

def calcular_aceleracion(masa, fuerza):
    aceleracion = fuerza / masa
    return aceleracion

def calcular_fuerza_normal(coeficiente_friccion_estatica, fuerza_friccion):
    fuerza_normal = coeficiente_friccion_estatica * fuerza_friccion
    return fuerza_normal

def calcular_fuerza_friccion(coeficiente_friccion_estatica, fuerza_normal):
    fuerza_friccion = coeficiente_friccion_estatica * fuerza_normal
    return fuerza_friccion

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
    g_a_kg = gram / 1000 
    return g_a_kg

def calcular_m_a_s(minuto):
    m_a_s = minuto * 60
    return m_a_s

def calcular_s_a_m(segundo):
    s_a_m = segundo / 60 
    return s_a_m

print("¿Quieres usar el formulario?, ¿Quieres resolver una ecuación? o ¿Quieres hacer conversión de unidades?")
print("1. Formulario")
print("2. Resolver la ecuación")
print("3. Conversión de unidades")

calculadora = int(input("Selecciona una opción (1/2/3): "))

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
    else: 
        print("No insertaste un dato correcto, regresa al menú principal")

elif calculadora == 2: 
    print("Calculadora de Física")
    print("1. Distancia, Velocidad o Tiempo")
    print("2. Fuerza, Masa, Aceleración")
    print("3. Fuerza normal o fuerza de fricción")

    opciones = int(input("Selecciona una opción (1/2/3): "))
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
            print("No insertaste un dato correcto, regresa al menú principal")

    elif opciones == 2:
        print("1. Calcular Fuerza")
        print("2. Calcular Masa")
        print("3. Calcular Aceleración")

        opcion_tres = int(input("Selecciona una opción (1/2/3): "))

        if opcion_tres == 1:
            masa = float(input("Insertar la masa: "))
            aceleracion = float(input("Insertar la aceleracion: "))
            fuerza = calcular_fuerza(masa, aceleracion)
            print(f"la fuerza es {fuerza} N")

        elif opcion_tres == 2:
            fuerza = float(input("Insertar la fuerza: "))
            aceleracion = float(input("Insertar la aceleracion: "))
            masa = calcular_masa(aceleracion, fuerza)
            print(f"La masa es: {masa} g")

        elif opcion_tres == 3:
            fuerza = float(input("Insertar la fuerza: "))
            masa = float(input("Insertar la masa: "))
            aceleracion = calcular_aceleracion(masa, fuerza)
            print(f"La aceleración es: {aceleracion} m/s**2")

        else: 
            print("No insertaste un dato correcto, regresa al menú principal")

    elif opciones == 3:
        print("1. Calcular la fuerza normal")
        print("2. Fuerza de fricción")

        opcion_cuatro = int(input("Selecciona una opción (1/2): "))

        if opcion_cuatro == 1:
            fuerza_friccion = float(input("Insertar la fuerza de fricción: "))
            coeficiente_friccion_estatica = float(input("Insertar el coeficiente de fricción estatica: "))
            fuerza_normal = calcular_fuerza_normal(coeficiente_friccion_estatica, fuerza_friccion)
            print(f"La fuerza normal es: {fuerza_normal} N")

        elif opcion_cuatro == 2:
            fuerza_normal = float(input("Insertar la fuerza normal: "))
            coeficiente_friccion_estatica = float(input("Insertar el coeficiente de fricción estatica: "))
            fuerza_friccion = calcular_fuerza_friccion(coeficiente_friccion_estatica, fuerza_normal)
            print(f"La fuerza de fricción es: {fuerza_friccion} N ")
        
        else: 
            print("No insertaste un dato correcto, regresa al menú principal")

elif calculadora == 3:
    print("1. Convertir kilometros a metros")
    print("2. Convertir metros a kilometros")
    print("3. Convertir kilogramos a gramos")
    print("4. Convertir gramos a kilogramos")
    print("5. Convertir minuto a segundo")
    print("6. Convertir segundos a minuto")

    opcion_cinco = int(input("Selecciona una opción (1/2/3/4/5/6): "))

    if opcion_cinco == 1:
        kilometro = float(input("Insertar los kilometros: "))
        kilometro = calcular_km_a_m(kilometro)
        print(f"La conversión a metros es {kilometro} m")

    elif opcion_cinco == 2:
        metro = float(input("Insertar los metros: "))
        metro = calcular_m_a_km(metro)
        print(f"La conversión a kilometros es {metro} km")
    
    elif opcion_cinco == 3:
        kilogramo = float(input("Insertar los kilogramos: "))
        kilogramo = calcular_kg_a_g(kilogramo)
        print(f"La conversión a gramos es {kilogramo} g")

    elif opcion_cinco == 4:
        gramo = float(input("Insertar los gramos: "))
        gramo = calcular_g_a_kg(gramo)
        print(f"La conversión a kilogramo es {gramo} kg")
    
    elif opcion_cinco == 5:
        minuto = float(input("Insertar los minutos: "))
        minuto = calcular_m_a_s(minuto)
        print(f"La conversion a segundos es {minuto} s")

    elif opcion_cinco == 6:
        segundo = float(input("Insertar los segundos: "))
        segundo = calcular_s_a_m(segundo)
        print(f"La conversión a minutos es {segundo} m")        

    else: 
        print("No insertaste un dato correcto, regresa al menú principal")

elif calculadora >= 4: 
    print("No insertaste un dato correcto, regresa al menú principal")

else: 
    print("No insertaste un dato correcto, regresa al menú principal")
