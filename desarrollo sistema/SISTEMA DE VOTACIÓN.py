from os import system 
system ("cls")
import os
import random
import time
#entradas
#declaramos variables 
#variables de inicio
RECTIFICADORES=["RNEC","2023#"]
VOTANTES_GENERAL={}
#variabes para saber cuales son los votantes que han reportado sus votos
#CORREGIMIENTOS
ZONAS_RURALES={1:"palenquillo",
                2:"puerto viejo",
                3:"mahoma",
                4:"la estacion",
                5:"cascajal",
                6:"el contento",
                7:"puerto mosquito"}
#BARRIOS URBANOS
ZONAS_URBANA={1:"san jose",
                2:"araujo",
                3:"el carmen",
                4:"san martin",
                5:"el prado",
                6:"el comercio",
                7:"aceitunos",
                8:"san antonio",
                9:"capulco nuevo",
                10:"divino niño",
                11:"brisas del cesar",
                12:"balcones del olaya"}
#Candidatos a la alcadia del municipio de gamarra
CANDIDATOS={1:"pepito perez",
            2:"juanito gonzales",
            3:"pedro picapiedra",
            4:"fernando quintero",
            5:"voto en blanco"}
#PUESTOS Y MESAS DE VOTACION
PUESTO_VOTACION_URBANOS=[{"codigo":1240,"nombre":"institucion educativa rafael salazar","direccion":"Cl-8-N-13-54","mesas":21},{"codigo":3477,"nombre":"institucion educativa promoción social","dirección":"Kilometro 2 Via Aguachica","mesas":3}]

PUESTO_VOTACIÓN_RURALES={"palenquillo":3
                ,"puerto viejo":1
                ,"mahoma":1
                ,"la estacion":2
                ,"cascajal":1
                ,"el contento":2
                ,"puerto mosquito":2}
'''
declaramos variables para la primera funcion que me va a permitir, registrar los votantes del cual al momento de ejercer la votación verificaremos sus datos para asi poder avanzar al siguiente proceso
'''
def REGISTRO_VOTANTES(VOTANTES):
    '''
    utilizaremos los diccionarios para trabajar con ellos internamente para tener un manejo correcto de la información 
    ademas, utilizarmos una lista interna para almacenar los datos del votante y asi poderlo subir a la respectiva base general del programa
    '''
    VOTANTES=[]
    ZONAS_URBANA={1:"san jose",
                2:"araujo",
                3:"el carmen",
                4:"san martin",
                5:"el prado",
                6:"el comercio",
                7:"aceitunos",
                8:"san antonio",
                9:"capulco nuevo",
                10:"divino niño",
                11:"brisas del cesar",
                12:"balcones del olaya"}
    
    ZONAS_RURALES={1:"palenquillo",
                    2:"puerto viejo",
                    3:"mahoma",
                    4:"la estacion",
                    5:"cascajal",
                    6:"el contento",
                    7:"puerto mosquito"}
    
    PUESTO_VOTACION_URBANOS=[{"codigo":1240,"nombre":"institucion educativa rafael salazar","direccion":"Cl-8-N-13-54","mesas":21},
                            {"codigo":3477,"nombre":"institucion educativa promoción social","dirección":"Kilometro 2 Via Aguachica","mesas":3}]
    
    PUESTO_VOTACIÓN_RURALES={
                "palenquillo":3
                ,"puerto viejo":1
                ,"mahoma":1
                ,"la estacion":2
                ,"cascajal":1
                ,"el contento":2
                ,"puerto mosquito":2}
    while True:
        try:
            cedula=int(input("ingresa la cedula del votante: "))
        except:
            print("error: ingrese el numero de documentos sin puntos ni comas")
            continue
        else:
            break
    if cedula in VOTANTES:
        print("su documento se encuentra en la base de datos:")
    else:
        VOTANTES.append(cedula)
        while True:
            try:
                nombre=str(input("ingrese sus nombre:  ")).split()
            except:
                print("error no se permiten numeros")
                continue
            else:
                break
        while True:
            try:
                apellido=str(input("ingresa tu apellido: ")).split()
            except:
                print("error no se permiten numeros")
                continue
            else:
                break
        VOTANTES.append(nombre)
        VOTANTES.append(apellido)
        SELEC_ZONA=int(input("SELECIONA TU ZONA 1.ZONA URBANA /2.ZONA RURAL: "))
        if SELEC_ZONA >2:
            quit()  
        VOTANTES.append(SELEC_ZONA)
        if SELEC_ZONA == 1:
            print("tus zonas urbanas son:")
            for i in ZONAS_URBANA.items():
                print(i)
            OP_SELECCION=int(input("SELECCIONA TU BARRIO: "))
            if OP_SELECCION <=11:
                print("tus colegios de votacion son:")
                for i in PUESTO_VOTACION_URBANOS:
                    print(i)
                while True:
                    try:
                        op_colegios=int(input("escribe el codigo del colegio: "))
                    except:
                        print("error solo se permiten numeros")
                        continue
                    else:
                        break
                if op_colegios== 1240:
                    mesa=random.randrange(1,21)
                    print(f"su mesa de votacion es la numero: {mesa}")
                    VOTANTES.append(mesa)
                    print(f"sus datos fueron guardados correctamente:cedula: {cedula},nombre: {nombre},apellido: {apellido},SELEC_ZONA: {SELEC_ZONA},mesa: {mesa}")
                    for i in reversed(range(1,4)):
                        print(f"redirigiendo al sistema de votación...{i}")
                        time.sleep(4)
                    os. system("cls")
                    sistema_votacion(VOTANTES)
                    for i in reversed(range(1,2)):
                        print(f"Gracias por participar en estas elecciones municipales 2023, que tengas un buen dia...{i}")
                        time.sleep(2)
                        exit()
                elif op_colegios == 3477:
                    mesa=random.randrange(1,3)
                    print(f"su mesa de votacion es la mesa numero: {mesa}")
                    VOTANTES.append(mesa)
                    print(f"sus datos fueron guardados correctamente:cedula: {cedula},nombre: {nombre},apellido: {apellido},SELEC_ZONA: {SELEC_ZONA},mesa: {mesa}")
                    for i in reversed(range(1,4)):
                        print(f"redirigiendo al sistema de votación...{i}")
                        time.sleep(4)
                    os. system("cls")
                    sistema_votacion(VOTANTES)
                    for i in reversed(range(1,2)):
                        print(f"Gracias por participar en estas elecciones municipales 2023, que tengas un buen dia...{i}")
                        time.sleep(2)
                        exit()
        if SELEC_ZONA == 2:
            print("tus zonas rurales son:")
            for i in ZONAS_RURALES.items():
                print(i)
            OP_SELECCION2=int(input("SELECCIONA TU ZONA:"))
            VOTANTES.append(OP_SELECCION2)
            if OP_SELECCION2 <=7:
                print("tus puestos de votacion son:")
                for i in  PUESTO_VOTACIÓN_RURALES.keys():
                    print(i)
                while True:
                    try:
                        puesto=input("seleccione de nuevo corregimiento para obtener su puesto de votacion:")
                    except:
                        print("error")
                        continue
                    else:
                        break
                VOTANTES.append(puesto)
                if puesto == "palenquillo":
                    mesa=random.randrange(1,3)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
                elif puesto == "puerto viejo":
                    mesa=random.randrange(1,2)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
                elif puesto == "mahoma":
                    mesa=random.randrange(1,2)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
                elif puesto == "la estacion":
                    mesa=random.randrange(1,2)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
                elif puesto == "cascajal":
                    mesa=random.randrange(1,2)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
                elif puesto == "el contento":
                    mesa=random.randrange(1,2)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
                elif puesto == "puerto mosquito":
                    mesa=random.randrange(1,2)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
                VOTANTES.append(mesa)
                VOTANTES.append(VOTANTES)
                opcion=input("desea agregar otro votante al sistema de registro si/no: ")
                if opcion == "no":
                    print("sus datos fueron guardados correctamente:",VOTANTES)
                    os.system("cls")
                    sistema_votacion(VOTANTES)
                return VOTANTES

def sistema_votacion(VOTANTES):
    ACU_CAN1=0
    ACU_CAN2=0
    ACU_CAN3=0
    ACU_CAN4=0
    ACU_CAN5=0 
    print("bienvenidos al sistema de votacion es un gusto para nosotros el tenerte aqui ejerciendo su voto")
    while True:
        try:
            cedula=int(input(" por favor ingrese su numero de cedula:"))
        except:
            print("no se permiten puntos ni comas ")
            continue
        else:
            break
    if cedula in VOTANTES:
        print("su cedula no se encuentra registrada en la base de datos...")
        quit
    else:
        print("los datos del votante son: ")
        for i in VOTANTES:
            print(i)
            CANDIDATOS={1:"PEPITO PEREZ",
                        2:"JUANITO GONZALES",
                        3:"PEDRO PICAPIEDRA",
                        4:"CANTINFLAS",
                        5:"voto en blanco"}
            print("los candidatos a la alcadia municipal son: ")
            for i in CANDIDATOS.items():
                print(i)
            while True:
                try:
                    opcion=int(input("seleccione el candidato por el cual desea votar: "))
                except:
                    print("solo debes escribir el numero que lo representa")
                    continue
                else:
                    break
            if opcion >5:
                print("lo sentimos el numero seleccionado no esta dentro del rango permitido")
                quit()
            if opcion == 1:
                ACU_CAN1=+1
                print("su voto se a guardado correctamente..",ACU_CAN1)
            elif opcion == 2:
                ACU_CAN2+=1
                print("voto correctamente guardado")
                print(ACU_CAN2)
            elif opcion == 3:
                ACU_CAN3+=1
                print("voto correctamente guardado")
                print(ACU_CAN3)
            elif opcion == 4:
                ACU_CAN4+=1
                print("voto correctamente guardado")
                print(ACU_CAN4)
            elif opcion == 5:
                ACU_CAN5+=1
                print("voto correctamente guardado")
                print(ACU_CAN5)
            else:

                print("no seleccionaste ningun candidato")
                quit()

def apertura_votaciones():
    abrir_votacion=False
    cerrar_votacion=False
    if abrir_votacion==False:
        aper=str(input("deseas abrir la votacion si/no"))
        if aper=="si":
            abrir_votacion=True
            print(f"la votación fue aperturada correctamente: {abrir_votacion}")
            for i in reversed(range(1,2)):
                print("cargando sistema....",i)
                time.sleep(2)
                os.system("cls")
                menu_registro_y_votaciones()
            opcion=str(input("deseas cerrar la votacion si/no:"))
            if opcion == "si":
                cerrar_votacion=True
                print("la votacion se ha cerrado correctamente")
                exit()

def menu_registro_y_votaciones():
    while(True):
        print("*******BIENVENIDO AL MENU GENERAL DE VOTACION*********")
        print(" ")
        print("*****************************************************")
        print("1.REGISTRO DE VOTANTES")
        print("2.SISTEMA DE VOTACION")
        print("******************************************************")
        opcion=int(input("que opcion deseas:"))
        if opcion == 1:
            REGISTRO_VOTANTES(VOTANTES_GENERAL)
        if opcion == 2:
            sistema_votacion(VOTANTES_GENERAL)
def menu():
    while(True):
        print("-----------------SISTEMA DE VOTACION-------------------|")
        print("|                                                      |")                                                    
        print("-------------------------------------------------------|")
        print("|1.INICIE SESION..                                     |")
        print("|------------------------------------------------------|")
        while True:
            try:
                op_inicio=int(input("elije la opcion:-->"))
            except:
                print("error")
                continue
            else:
                break
        if op_inicio >1:
            print("lo sentimos el numero seleccionado no esta dentro del rango permitido")
            os.system("cls")
            continue
        if op_inicio == 1:
            os.system("cls")
            rectificador()
        else:
            quit()

def rectificador():
    if input("ingrese su usuario:--->") != RECTIFICADORES[0] or input("ingrese la contraseña-->") != RECTIFICADORES[1] or print("sesion iniciada") or os.system("cls") or apertura_votaciones():
        print("acceso denegado")or quit()

if __name__=="__main__":
    print("bienvenidos al sistema de registro y votaciones,para nosotros es un placer que nos hayas elegido como plataforma")
    print("para estas nuevas elecciones municipales 2023")
    print("                                           ")
    input("presiona enter para continuar..:")
    for i in reversed(range(1,2)):
        print(i)
        time.sleep(2)
    os.system("cls")
    menu()