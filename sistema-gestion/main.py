from proyectos import *
from reporte import *

def redigir(opcion):

    if(opcion == 1):
        print('\tPROYECTOS\t')
        print('1- Crear Proyecto')
        print('2- Modificar Proyecto')
        print('3- Borrar Proyecto')
        print('4- Consultar Proyecto')
        subopcion = int(input('Ingrese la opcion deseada: '))
        proyecto = Proyectos()
        if(subopcion == 1):
            proyecto.crearProyecto()
        elif(subopcion == 2):
            proyecto.modificarProyecto()
        elif(subopcion == 3):
            proyecto.borrarProyectoJSON()
        elif(subopcion == 4):
            proyecto.consultarProyectoJSON()

    elif(opcion == 2):
        print('\tTAREAS\t')
    elif(opcion == 3):
        print('\tSUBTAREAS\t')
    elif(opcion == 4):
        print('\tCONSULTAS - REPORTES\t')
        print('1- Consulta de Tareas por Estado')
        print('2- Filtrado por Fecha')
        print('3- Filtrado de proyectos')
        print('4- Listar subtareas')
        subopcion = int(input('Ingrese la opcion deseada: '))
        proyecto = reporte()
        if(subopcion == 1):
            estado = input('Ingrese el estado: ')
            reporte.tareas(estado)
        elif(subopcion == 2):
            proyecto.modificarProyecto()
        elif(subopcion == 3):
            proyecto.borrarProyectoJSON()
        elif(subopcion == 4):
            proyecto.consultarProyectoJSON()

opcion = 999    
while opcion != 0:
    print('\tModulos\t')
    print('1- Proyectos')
    print('2- Tareas')
    print('3- Subtareas')
    print('4- Consultas - Reportes')
    print('5- Finalizar')
    opcion = int(input('Ingrese una opcion: '))
    if opcion in [1,2,3,4]:
        redigir(opcion)
        opcion = 0

