from os import system 
system ("cls")
import random
# este borrador lo cree  para corregir errores y que no pueda borrar nada en el archivo principal solo copiar y pegar
RECTIFICADORES=["RNEC","#Votaciones2023"]
VOTANTES={}
#CORREGIMIENTOS
ZONAS_RURALES={1:"palenquillo",2:"puerto viejo",3:"mahoma",4:"la estacion",5:"cascajal",6:"el contento",7:"puerto mosquito"}
#BARRIOS URBANOS
ZONAS_URBANA={1:"san jose",2:"araujo",3:"el carmen",4:"san martin",5:"el prado",6:"el comercio",7:"aceitunos",8:"san antonio",9:"capulco nuevo",10:"divino niño",11:"brisas del cesar",12:"balcones del olaya"}
#CANDIDATOS
CANDIDATOS={1:"pepito perez",2:"juanito gonzales",3:"pedro picapiedra",4:"fernando quintero",5:"voto en blanco"}
#PUESTOS Y MESAS DE VOTACION
PUESTO_URBANOS={"instituciion educativa rafael salazar":21,"institucion educativa promocion social":2}
PUESTO_RURALES={"palenquillo":3,"puerto viejo":1,"mahoma":1,"la estacion":2,"cascajal":1,"el contento":2,"puerto mosquito":2}

def registro_votantes(VOTANTES,ZONAS_URBANA,ZONAS_RURALES,PUESTO_URBANOS,PUESTO_RURALES):
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
        VOTANTES["zonas:"]=SELEC_ZONA
        if SELEC_ZONA == 1:
            print("tus zonas urbanas son:")
            for i in ZONAS_URBANA.items():
                print(i)
            OP_SELECCION=int(input("SELECCIONA TU BARRIO: "))
            #GUARDAR EN EL DICCIONARIO ESTA VARIABLE
            if OP_SELECCION <=11:
                print("tus puestos de votacion son:")
                for i in  PUESTO_URBANOS.keys():
                    print(i)
                puesto=input("seleccione la sede donde desea votar:")
                #GUARDAR ESTE AMBITO
                if puesto == "institucion educativa rafael salazar":
                    mesa=random.randrange(1,21)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}") 
                elif puesto == "institucion educativa rafael salazar":
                    mesa= random.randrange(1,2)
                    print(f"tu mesa de votacion es la mesa numero: {mesa}")
        if SELEC_ZONA == 2:
            print("tus zonas rurales son:")
            for i in ZONAS_RURALES.items():
                print(i)
            OP_SELECCION2=int(input("SELECCIONA TU ZONA:"))
            if OP_SELECCION2 <=7:
                print("tus puestos de votacion son:")
                for i in  PUESTO_RURALES.keys():
                    print(i)
            puesto=input("seleccione de nuevo corregimiento para obtener su puesto de votacion:")
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

if __name__=="__main__":
    registro_votantes(VOTANTES,ZONAS_URBANA,ZONAS_RURALES,PUESTO_URBANOS,PUESTO_RURALES)