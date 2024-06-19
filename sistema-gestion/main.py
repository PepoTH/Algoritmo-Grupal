from proyectos import *

def redigir(opcion):

    if(opcion == 1):
        print('\tPROYECTOS\t')
        print('1- Crear Proyecto')
        print('2- Modificar Proyecto')
        print('3- Borrar Proyecto')
        print('4- Consultar Proyecto')
        subopcion = int(input('Ingrese la opcion deseada: '))
        if(subopcion == 1):
            proyecto = Proyectos()
            proyecto.agregarProyecto()
        

    elif(opcion == 2):
        print('\tTAREAS\t')
    elif(opcion == 3):
        print('\tSUBTAREAS\t')
    elif(opcion == 4):
        print('\tCONSULTAS - REPORTES\t')

opcion = 999    
while opcion != 0:
    print('\tModulos\t')
    print('-1 Proyectos')
    print('-2 Tareas')
    print('-3 Subtareas')
    print('-4 Consultas - Reportes')
    print('-0 Finalizar')
    opcion = int(input('Ingrese una opcion: '))
    if opcion in [1,2,3,4]:
        redigir(opcion)
        opcion = 0

