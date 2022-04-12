"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""




def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    #OMG

    data = open('data.csv','r').readlines()
    col2 = [int(row[2]) for row in data]

    suma = sum(col2)
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    #HELP

    data = open('data.csv','r').readlines()
    contador={}
    tupla = []

    for i in data:
        mi_lista= i[0]
        if mi_lista in contador.keys():
            contador[mi_lista]= contador[mi_lista]+ 1
        else:
            contador[mi_lista] = 1
        tupla=list(zip(contador.keys(),contador.values()))
        tupla.sort()
        
    return tupla

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    #WHATT

    data = open('data.csv','r').readlines()
    data=[z.replace('\n','') for z in data]
    data = [z.replace('\t','') for z in data]

    suma={}
    tupla=[]


    for i in data:
        mi_tupla= i[0]
        col1=int(i[1])
        if mi_tupla in suma.keys():
            suma[mi_tupla]= suma[mi_tupla]+ col1
        else:
            suma[mi_tupla]= col1
        tupla=list(zip(suma.keys(),suma.values()))
        tupla.sort()
    return tupla



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    #AUXILIPP
    
    data = open('data.csv','r').readlines()
    data=[x.replace('\n','') for x in data]
    data=[x.split('\t') for x in data]

    tupla={}

    for row in data:
        vble=row[2].split('-')
        mes=vble[1]
        if mes in tupla.keys():
            tupla[mes]=tupla[mes]+1
        else:
             tupla[mes]=1

    tupla=list(zip(tupla.keys(), tupla.values()))
    tupla.sort()

    return tupla


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    #NODIOOOO


    with open('data.csv','r') as file:
        data= file.readlines()
    data=[x.replace('\n','') for x in data]
    data=[x.split('\t') for x in data] 
    id_list=sorted(set([x[0] for x in data]))
    lista_datos=[(x[0], int(x[1])) for x in data]    
    
    valor=[]
    result=[]
        

    for letra in id_list:
        for num in lista_datos:
             if num[0]==letra:
                 valor.append(num[1])
        
        result.append((letra, max(valor), min(valor)))
        valor.clear()
    
    return result
            
    
   
 
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv','r') as file:
        data = file.readlines()
    data=[x.replace('\n','') for x in data]
    data=[x.split('\t') for x in data] 
    mi_lista=[x[4].split(',') for x in data]

    nueva_lista = [(j[:3], int(j[4:])) for i in mi_lista for j in i]
    mi_dict = sorted(set(elm[0] for elm in nueva_lista))

    result=[]
    mi_tupla=[]

    for letra in mi_dict:
        for elm in nueva_lista:
            if elm[0] == letra:
                result.append(elm[1])
        mi_tupla.append((letra, min(result), max(result)))
        result.clear()

    return mi_tupla


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    # WHY :(

    from operator import itemgetter
    data = open('data.csv','r').readlines()
    data=[z.replace('\n','') for z in data]
    data=[z.replace('\t',';') for z in data]
    data=[z.split(';') for z in data] 

    datos_siete=[[row[1]]+[row[0]] for row in data]
    result={}
    for valor, letra in datos_siete:
        if valor in result.keys():
            result[valor].append(letra)
        else:
            result[valor]=[letra]

    result=[(int(key), letra) for key, letra in result.items()]
    result=sorted(result, key=itemgetter(0), reverse=False)
    

    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv','r') as file:
        data = file.readlines()
    data=[x.replace('\n','') for x in data]
    data=[x.split('\t') for x in data]
    nuevos_datos=[(int(x[1]), x[0]) for x in data]
    mi_data=sorted(set(x[0] for x in nuevos_datos))


    result=[]
    mi_tupla=[]

    for x in mi_data:
            for y in nuevos_datos:
                    if y[0]-x==0:
                            result.append(y[1])
            mi_tupla.append((x, sorted(set(result))))
            result=[]
    
    return mi_tupla


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv','r') as file:
        data = file.readlines()
    data=[x.replace('\n','') for x in data]
    data=[x.split('\t') for x in data]
    mi_data=[x[4].split(',') for x in data]

    mi_lista=[(y[:3]) for x in mi_data for y in x]
    mi_dict= sorted(set(elm for elm in mi_lista))
    mi_tupla=[(x, mi_lista.count(x))for x in mi_dict]
    dictionary=dict(mi_tupla)

    return dictionary


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
