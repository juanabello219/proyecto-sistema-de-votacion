from os import system
system ("cls")
import os 
import random
VOTANTES=[]
#CORREGIMIENTOS
ZONAS_RURALES={1:"palenquillo",2:"puerto viejo",3:"mahoma",4:"la estacion",5:"cascajal",6:"el contento",7:"puerto mosquito"}
#BARRIOS URBANOS
ZONAS_URBANA={1:"san jose",2:"araujo",3:"el carmen",4:"san martin",5:"el prado",6:"el comercio",7:"aceitunos",8:"san antonio",9:"capulco nuevo",10:"divino niño",11:"brisas del cesar",12:"balcones del olaya"}
#CANDIDATOS
CANDIDATOS={1:"pepito perez",2:"juanito gonzales",3:"pedro picapiedra",4:"fernando quintero",5:"voto en blanco"}
#PUESTOS Y MESAS DE VOTACION
PUESTO_URBANOS={"instituciion educativa rafael salazar":21,"institucion educativa promocion social":2}
PUESTO_RURALES={"palenquillo":3,"puerto viejo":1,"mahoma":1,"la estacion":2,"cascajal":1,"el contento":2,"puerto mosquito":2}
def registro_votantes(VOTANTES):
    VOTANTES2=[]
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
        VOTANTES2.append(cedula)
    else:
        nombre=str(input("ingrese su nombre:"))
        apellido=str(input("ingresa tu apellido:"))
        VOTANTES2.append(nombre)
        VOTANTES2.append(apellido)
        SELEC_ZONA=int(input("SELECIONA TU ZONA 1.ZONA URBANA /2.ZONA RURAL:"))
        if SELEC_ZONA >2:
            quit()
        VOTANTES2.append(SELEC_ZONA)
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
                VOTANTES2.append(puesto)
                if puesto == "institucion educativa rafael salazar":
                    mesa=random.randrange(1,21)
                    VOTANTES2.append(mesa)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}") 
                elif puesto == "institucion educativa de promocion social":
                    mesa= random.randrange(1,3)
                    VOTANTES2.append(mesa)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
        if SELEC_ZONA == 2:
            print("tus zonas rurales son:")
            for i in ZONAS_RURALES.items():
                print(i)
            OP_SELECCION2=int(input("SELECCIONA TU ZONA:"))
            VOTANTES2.append(OP_SELECCION2)
            if OP_SELECCION2 <=7:
                print("tus puestos de votacion son:")
                for i in  PUESTO_RURALES.keys():
                    print(i)
            puesto=input("seleccione de nuevo corregimiento para obtener su puesto de votacion:")
            VOTANTES2.append(puesto)
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
            VOTANTES2.append(mesa)
            VOTANTES.append(VOTANTES2)
        opcion=input("desea agregar otro votante al sistema de registro si/no: ")
        if opcion == "no":
            print("sus datos fueron guardados correctamente",VOTANTES2)
    return (VOTANTES)


def sistema_votacion(VOTANTES):
    VOTANTES=[]
    x=0
    CANDIDATOS={1:"PEPITO PEREZ",2:"JUANITO GONZALES",3:"PEDRO PICAPIEDRA",4:"CANTINFLAS",5:"voto en blanco"}
    cedula=int(input("ingrese la cedula del votante"))
    print("los datos del votante son: ")
    for i in VOTANTES:
        x+=0
        print(x,i)
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
            sistema_votacion(VOTANTES)


if __name__=="__main__":
    menu_registro_y_votaciones()