from os import system
system ("cls")
import os 
import random

#entradas
#declaramos variables 
RECTIFICADORES=["RNEC","elecciones2023"]
VOTANTES={

}
#CORREGIMIENTOS
ZONAS_RURALES={1:"palenquillo",2:"puerto viejo",3:"mahoma",4:"la estacion",5:"cascajal",6:"el contento",7:"puerto mosquito"}
#BARRIOS URBANOS
ZONAS_URBANA={1:"san jose",2:"araujo",3:"el carmen",4:"san martin",5:"el prado",6:"el comercio",7:"aceitunos",8:"san antonio",9:"capulco nuevo",10:"divino niño",11:"brisas del cesar",12:"balcones del olaya"}
#CANDIDATOS
CANDIDATOS={1:"pepito perez",
            2:"juanito gonzales",
            3:"pedro picapiedra",
            4:"fernando quintero",
            5:"voto en blanco"}
#PUESTOS Y MESAS DE VOTACION
PUESTO_URBANOS={"instituciion educativa rafael salazar":21,"institucion educativa promocion social":2}
PUESTO_RURALES={"palenquillo":3,"puerto viejo":1,"mahoma":1,"la estacion":2,"cascajal":1,"el contento":2,"puerto mosquito":2}
#declaramos las funciones 
#esta funcion me permite registrar los votantes para las elecciones municipales
def registro_votantes(VOTANTES):
    VOTANTES={}
    ZONAS_RURALES={1:"palenquillo",2:"puerto viejo",3:"mahoma",4:"la estacion",5:"cascajal",6:"el contento",7:"calpulco nuevo",8:"puerto mosquito"}
    ZONAS_URBANA={1:"san jose",2:"araujo",3:"el carmen",4:"san martin",5:"el prado",6:"el comercio",7:"aceitunos",8:"san antonio",9:"capulco nuevo",10:"divino niño",11:"brisas del cesar"}
    PUESTO_URBANOS={"INSTITUCION EDUCATIVA RAFAEL SALAZAR":21,"INSTITUCION EDUCATIVA DE PROMOCIÓN SOCIAL":2}
    PUESTO_RURALES={"palenquillo":3,"puerto viejo":1,"mahoma":1,"la estacion":2,"cascajal":1,"el contento":2,"puerto mosquito":2}
    while True:
        try:
            cedula=int(input("ingrese el numero de cedula del votante:"))
        except:
            print("error ingresa el numero de documento sin comas ni puntos")
            continue
        else:
            break
    if cedula in VOTANTES:
        print("su numero de documentos se encuentra en la base de datos por favor digite nuevamente")
    else:
        VOTANTES["cedula"]=cedula
        while True:
            try:
                nombre=str(input("ingrese su nombre:"))
            except:
                print("error solo le permite letra")
                continue
            else:
                break
        while True:
            try:
                apellido=str(input("ingresa tu apellido:"))
            except:
                print("error no se permiten numeros")
                continue
            else:
                break
        VOTANTES["nombre"]=nombre
        VOTANTES["apellido"]=apellido
        SELEC_ZONA=int(input("SELECIONA TU ZONA 1.ZONA URBANA /2.ZONA RURAL:"))
        if SELEC_ZONA >2:
            quit()
        VOTANTES["zonas:"]=SELEC_ZONA
        if SELEC_ZONA == 1:
            print("tus zonas urbanas son:")
            for i in ZONAS_URBANA.items():
                print(i)
            OP_SELECCION=int(input("SELECCIONA TU BARRIO: "))
            if OP_SELECCION <=11:
                print("tus puestos de votacion son:")
                for i in  PUESTO_URBANOS.keys():
                    print(i)
                puesto=input("seleccione la sede donde desea votar:")
                VOTANTES["PUESTO-VOTACION"]=puesto
                if puesto == "institucion educativa rafael salazar":
                    mesa=random.randrange(1,21)
                    VOTANTES["mesa"]=mesa
                    print(f"tu mesa de votacion es la mesa numero: {mesa}") 
                elif puesto == "institucion educativa de promocion social":
                    mesa= random.randrange(1,3)
                    VOTANTES["mesa"]=mesa
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
        if SELEC_ZONA == 2:
            print("tus zonas rurales son:")
            for i in ZONAS_RURALES.items():
                print(i)
            OP_SELECCION2=int(input("SELECCIONA TU ZONA:"))
            VOTANTES["zonas corregimiento"]=OP_SELECCION2
            if OP_SELECCION2 <=7:
                print("tus puestos de votacion son:")
                for i in  PUESTO_RURALES.keys():
                    print(i)
            puesto=input("seleccione de nuevo corregimiento para obtener su puesto de votacion:")
            VOTANTES["lugar_votacion"]=puesto
            if puesto == "palenquillo":
                mesa=random.randrange(1,3)
                print(f"tu mesa de votacion es la mesa numero: {mesa}")
            elif puesto == "puerto viejo":
                mesa=random.randrange(1)
                print(f"tu mesa de votacion es la mesa numero: {mesa}")
            elif puesto == "mahoma":
                mesa=random.randrange(1)
                print(f"tu mesa de votacion es la mesa numero: {mesa}")
            elif puesto == "la estacion":
                mesa=random.randrange(1,2)
                print(f"tu mesa de votacion es la mesa numero: {mesa}")
            elif puesto == "cascajal":
                mesa=random.randrange(1)
                print(f"tu mesa de votacion es la mesa numero: {mesa}")
            elif puesto == "el contento":
                mesa=random.randrange(1,2)
                print(f"tu mesa de votacion es la mesa numero: {mesa}")
            elif puesto == "puerto mosquito":
                mesa=random.randrange(1,2)
                print(f"tu mesa de votacion es la mesa numero: {mesa}")
            VOTANTES["mesa"]=mesa
        opcion=input("desea agregar otro votante al sistema de registro si/no: ")
        if opcion == "no":
            print("sus datos fueron guardados correctamente:",VOTANTES)
    return (VOTANTES)

def sistema_votacion(VOTANTES,CANDIDATOS):
    CANDIDATOS={1:"PEPITO PEREZ",
                2:"JUANITO GONZALES",
                3:"PEDRO PICAPIEDRA",
                4:"CANTINFLAS",
                5:"voto en blanco"}
    cedula=int(input("ingresa tu numero de cedula:"))
    for i in VOTANTES:
        print("sus datos se encuentran en la base de datos:",i)
    while True:
        print("los candidatos a la alcadia municipal son: ")
        for i in CANDIDATOS.items():
            print(i)
        opcion=int(input("seleccione el candidato por el cual desea votar: "))
        if opcion == 1:
            acu_candidato1=0

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
            registro_votantes(VOTANTES)
        if opcion == 2:
            os.system("cls")
            sistema_votacion(VOTANTES,CANDIDATOS)
def menu():
    while(True):
        print("-----------------SISTEMA DE VOTACION-------------------|")
        print("|                                                      |")                                                    
        print("-------------------------------------------------------|")
        print("|1.INICIE SESION..                                     |")
        print("|------------------------------------------------------|")
        op_cajero=int(input("elije la opcion:-->"))
        if op_cajero == 1:
            os.system("cls")
            rectificador()

def rectificador():
    if input("ingrese su usuario:--->") != RECTIFICADORES[0] or input("ingrese la contraseña-->") != RECTIFICADORES[1] or print("sesion iniciada") or os.system("cls") or menu_registro_y_votaciones():
        print("acceso denegado")or quit()

if __name__=="__main__":
    print("bienvenidos al sistema de registro y votaciones,para nosotros es un placer que nos hayas elegido como plataforma")
    print("para estas nuevas elecciones municipales 2023")
    print("                                           ")
    input("presiona enter para continuar..:")
    os.system("cls")
    menu()