from os import system
system ("cls")
import os 
#declaramos variables 
RECTIFICADORES=["RNEC","#Votaciones2023"]
VOTANTES={}
ZONAS_RURALES={1:"palenquillo",2:"puerto viejo",3:"mahoma",4:"la estacion",5:"cascajal",6:"el contento",7:"calpulco nuevo",8:"puerto mosquito"}
ZONAS_URBANA={1:"san jose",2:"araujo",3:"el carmen",4:"san martin",5:"el prado",6:"el comercio",7:"aceitunos",8:"san antonio",9:"capulco nuevo",10:"divino niño",11:"brisas del cesar",12:"balcones del olaya"}
CANDIDATOS={1:"pepito perez",2:"juanito gonzales",3:"pedro picapiedra",4:"fernando quintero",5:"voto en blanco"}
PUESTO_URBANOS={"INSTITUCION EDUCATIVA RAFAEL SALAZAR":21,"INSTITUCION EDUCATIVA DE PROMOCIÓN SOCIAL":2}
PUESTO_RURALES={"palenquillo":3,"puerto viejo":1,"mahoma":1,"la estacion":2,"cascajal":1,"el contento":2,"puerto mosquito":2}
#declaramos las funciones 
#esta funcion me permite registrar los votantes para las elecciones municipales
def registro_votantes(VOTANTES,ZONAS_URBANA,ZONAS_RURALES):
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
        nombre=str(input("ingrese su nombre:"))
        apellido=str(input("ingresa tu apellido:"))
        VOTANTES["nombre"]=nombre
        VOTANTES["apellido"]=apellido
        SELEC_ZONA=int(input("SELECIONA TU ZONA 1.ZONA URBANA /2.ZONA RURAL:"))
        if SELEC_ZONA == 1:
            print("tus zonas urbanas son:")
            for i in ZONAS_URBANA.items():
                print(i)
            OP_SELECCION=int(input("SELECCIONA TU ZONA:"))
            print(f"tu zona seleccionada fue{OP_SELECCION}")
            
            if OP_SELECCION == ZONAS_URBANA:
                print("tus puestos de votacion son:")
                for i in  PUESTO_URBANOS.items():
                    print(i)
        if SELEC_ZONA == 2:
            print("tus zonas rurales son:")
            for i in ZONAS_RURALES.items():
                print(i)
            OP_SELECCION=int(input("SELECCIONA TU ZONA:"))
            if OP_SELECCION == i:
                print("hola")

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
            registro_votantes(VOTANTES,ZONAS_URBANA,ZONAS_RURALES)
        if opcion == 2:
            os.system("cls")
            print("esta opcion se encuentra en desarrollo....")
            menu_registro_y_votaciones()
def menu():
    while(True):
        print("--------BIENVENIDOS AL SISTEMA DE VOTACION--------------")
        print("|                                                      |")                                                    
        print("-------------------------------------------------------|")
        print("|1.INICIE SESION..                                        |")
        print("|------------------------------------------------------|")
        op_cajero=int(input("elije la opcion:-->"))
        if op_cajero == 1:
            os.system("cls")
            rectificador()

def rectificador():
    if input("ingrese su usuario:--->") != RECTIFICADORES[0] or input("ingrese la contraseña-->") != RECTIFICADORES[1] or print("sesion iniciada") or os.system("cls") or menu_registro_y_votaciones():
        print("acceso denegado")or quit()

if __name__=="__main__":
    menu()