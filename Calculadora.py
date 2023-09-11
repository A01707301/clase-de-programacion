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

def calcular_suma_nc(suma_nc1, suma_nc2):
    suma_nc = suma_nc1 + suma_nc2
    return suma_nc

def calcular_resta_nc(resta_nc1, resta_nc2):
    resta_nc = resta_nc1 - resta_nc2
    return resta_nc

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

if calculadora == 1:
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
            Newton = input("F=ma")
        elif formulario == 2: 
            aceleracion = input(" \n a= Vf-Vo/tf-to \n a= Vf-Vo/t \n xf= xo + vot + 1/2 at2 ")
        elif formulario == 3: 
            friccion = input("\n Fr= μN \n Fr= μmg")
        elif formulario == 4:
            centripeta = input("\n F=mat \n F=v2/R")
        else: 
            print("No insertaste un dato correcto, regresa al menú principal")

    elif opcion_uno == 2:
        print("1. Movimiento rectilíneo uniforme")
        print("2. Movimiento parabólico")
        print("3. Movimiento de caída libre")
        print("4. Movimiento circular")

        opcion_seis = int(input("Selecciona una opción (1/2/3/4): "))

        if opcion_seis == 1:
            rectilineo = input ("\n x=vt \n x=x0+vt \n v= x1-x2/t1-t2 \n v=v0+at \n x= x0+v0t+1/2 at2")
        elif opcion_seis == 2:
            parabolico = input ("\n vx=v0cosα \n vy=v0sina \n x(t)=x0+vxt \n y=y0 + vyt - 1/2gt2 \n y= vy0 -gt = v0 sin a -gt")
        elif opcion_seis ==3:
            caida_libre = input("y= y0 + v0t - 1/2 gt2 \n v=v0 - gt \n y= h - 1/2 gt2")
        elif opcion_seis == 4:
            circular = input ("∣v1∣=∣v2∣ \n w= θ2-θ1/t2-t1 \n w=dθ/dt \n w=2π/T \n v=wR \n ac= v2/R \n ac=w2R \n θf=θ0+wt \n w=w0 + at \n t=w - w0/a")
        else: 
            print("No insertaste un dato correcto, regresa al menú principal")

    else:
        print("No insertaste un dato correcto, regresa al menú principal")

elif calculadora == 2: 
    print("Calculadora de Física")
    print("1. Distancia, Velocidad o Tiempo")
    print("2. Fuerza, Masa, Aceleración")
    print("3. Fuerza normal o fuerza de fricción")
    print("4. Notación científica Suma/Resta")

    opciones = int(input("Selecciona una opción (1/2/3/4): "))
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
        
    elif opciones == 4: 
        print("1. Suma de notación científica")
        print("2. Resta de notación científica")

        opcion_siete = int(input("Selecciona una opción (1/2): "))
        if opcion_siete == 1:
            suma_nc1 = float(input("Insertar el primer número entero: "))
            suma_nc_ex = float(input("Insertar el primer exponente: "))
            suma_nc2 = float(input("Insertar el segundo número entero: "))
            suma2_nc_ex = float(input("Insertar el segundo exponente: "))
        
            if suma_nc_ex == suma2_nc_ex:
                suma_nc = calcular_suma_nc(suma_nc1, suma_nc2)
                print(f"La suma es: {suma_nc} x10 {suma_nc_ex}")

            if (suma_nc_ex < suma2_nc_ex) or (suma_nc_ex > suma2_nc_ex):
                # Aquí falta manejar los casos en los que los exponentes son diferentes.
        
        if opcion_siete ==2:
            resta_nc = float(input("Insertar el primer número entero: "))
            resta_nc_ex = float(input("Insertar el primer exponente: "))
            resta2_nc = float(input("Insertar el segundo número entero: "))
            resta2_nc_ex = float(input("Insertar el segundo exponente: "))
        
            if resta_nc_ex == resta2_nc_ex:
                resta_nc = calcular_resta_nc(resta_nc, resta2_nc)
                print(f"La resta es: {resta_nc} x10 {resta_nc_ex}")
                # Aquí falta manejar los casos en los que los exponentes son diferentes.
                
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
