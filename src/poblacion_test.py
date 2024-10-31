from poblacion import *
def test_lee_poblaciones(lista_poblaciones:list[RegistroPoblacion]):


def mostrar_numerado(coleccion):
    i=0
    for p in coleccion:
        i=i+1
        print (i, p) 

    registros=lee_poblaciones("data/population.csv")
    test_lee_poblaciones(registros)

def test_lee_poblaciones():
    print("Leidos " , len (POBLACIONES), "datos de población mundial")
    mostrar_numerado(POBLACIONES)    
        
        
def test_calcula_paises():         # Test de la función calcula_paises
    paises = calcula_paises(POBLACIONES)
    print("Paises")
    print("Leidos " , len (paises), "paises distintos")
    mostrar_numerado(paises)
  
def test_filtra_por_pais():         
    poblacion_es = filtrar_por_paises(POBLACIONES, "Spain")
    print("Poblacion españa")
    print("Leidos " , len (poblacion_es), "datos de población de España")
    mostrar_numerado(poblacion_es)

def test_filtra_por_paises_y_anyo():        
    paises= ["Spain","Portugal","France","Mexico","China"]
    poblacion_2016 = filtra_por_paises_y_anyo(POBLACIONES, 2016, paises)
    print("Leidos " , len (poblacion_2016), "datos del año 2016 para los paises", paises)
    mostrar_numerado(poblacion_2016)
        
def test_muestra_evolucion_poblacion():
    muestra_evolucion_poblacion(POBLACIONES, "Spain")

def test_muestra_comparativa_paises_anyo():
    muestra_comparativa_paises_anyo(POBLACIONES, 2016,["Spain","Portugal","France","Mexico","China"])

POBLACIONES = lee_poblaciones('../data/population.csv')

