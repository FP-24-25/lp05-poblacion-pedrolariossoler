import csv
from collections import namedtuple
RegistroPoblacion = namedtuple ('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    poblaciones=[]
    with open(ruta_fichero, encodin='utf-8') as f:
        lector=csv.reader(f)
        for nombre,codigo,anyo, censo in f:
            anyo=int(anyo)
            censo=int(censo)
            tupla=RegistroPoblacion(nombre,codigo,anyo,censo)
            poblaciones.append(tupla)
    return poblaciones


def calcula_paises(poblaciones, nombre_o_codigo):
    lista_paises=[0]
    sorted(lista_paises)

    return 

def filtrar_por_paises(poblaciones,anyo,paises):
    filtrado=[]
    for registro in poblaciones:
        if registro.nombre==paises:
            tupla=(registro.anyo,registro.censo)
            filtrado.append(tupla)
    return filtrado

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    filtrado2=[]
    for registro in poblaciones:
        if registro.anyo==anyo and (registro.paises in paises):
            tupla=(registro.nombre, registro.censo)
            filtrado2.append(tupla)
    return filtrado2

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    anyo=[]  
    habitantes=[]
    for t in filtrar_por_paises(poblaciones, paises):
        anyo.append(t[0])
        habitantes.append(t[1])

    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


def muestra_comparativa_paises_anyo(poblaciones,anyo,paises):
    anyo=[]
    lista_paises=[]
