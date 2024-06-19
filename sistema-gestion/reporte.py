from tareas import *
from proyectos import *

class reporte:
    def __init__(self, proyectos=None):
        if proyectos is None:
            with open('datos.json', 'r') as f:
                data = json.load(f)
                #ARREGLAR ESTO PONER todo DENTRO
                self.proyectos = data['proyectos']
                #self.proyectos = [Proyecto for p in data]
        else:
            self.proyectos = proyectos

    def tareas_por_estado(self,estado):
        for proyecto in self.proyectos:
            for tarea in proyecto.tareas:
                if tarea.estado == estado:
                    print(f"Nombre de la tarea: {tarea.nombre}")
                    print(f"Descripción de la tarea: {tarea.descripcion}")
                    print(f"Fecha de inicio de la tarea: {tarea.fecha_inicio}")
                    print(f"Fecha de fin de la tarea: {tarea.fecha_fin}")
                    print("Subtareas:")
                    for subtarea in tarea.subtareas:
                        print(f"\t{subtarea.nombre}")
                    print()

    def filtrar_por_fecha(self, fecha_inicio=None, fecha_fin=None, fecha_vencimiento=None):
        if fecha_inicio and fecha_fin:
            # Filtrar por rango de fechas
            for proyecto in self.proyectos:
                for tarea in proyecto.tareas:
                    if fecha_inicio <= tarea.fecha_inicio <= fecha_fin:
                        print(f"Nombre de la tarea: {tarea.nombre}")
                        print(f"Descripción de la tarea: {tarea.descripcion}")
                        print(f"Fecha de inicio de la tarea: {tarea.fecha_inicio}")
                        print(f"Fecha de fin de la tarea: {tarea.fecha_fin}")
                        print("Subtareas:")
                        for subtarea in tarea.subtareas:
                            print(f"\t{subtarea.nombre}")
                        print()
        elif fecha_vencimiento:
            # Filtrar por fecha de vencimiento
            for proyecto in self.proyectos:
                for tarea in proyecto.tareas:
                    if tarea.fecha_vencimiento == fecha_vencimiento:
                        print(f"Nombre de la tarea: {tarea.nombre}")
                        print(f"Descripción de la tarea: {tarea.descripcion}")
                        print(f"Fecha de inicio de la tarea: {tarea.fecha_inicio}")
                        print(f"Fecha de fin de la tarea: {tarea.fecha_fin}")
                        print("Subtareas:")
                        for subtarea in tarea.subtareas:
                            print(f"\t{subtarea.nombre}")
                        print()
        else:
            print("No se ha especificado un rango de fechas o una fecha de vencimiento")

    def proyectos(self,filtro):

        #Arreglar los nombres de los atributos de ls proyectos
        for i in range(0,len(self.proyectos)-1):
            #Recorrido de Proyectos
            if(self.proyectos[i].fechaInicio == filtro or self.proyectos[i].fechaVencimiento == filtro or self.proyectos[i].estado == filtro or self.proyectos[i].empresa == filtro):
                #Verificar si el filtro concuerda con algun parametro
                print('Nombre del proyecto: ',self.proyectos[i].nombre)
                print('Descripcion del proyecto: ',self.proyectos[i].nombre)
                print('Empresa del proyecto: ',self.proyectos[i].nombre)
                print('Fecha de Inicio del proyecto: ',self.proyectos[i].nombre)
                print('Fecha de Fin del proyecto: ',self.proyectos[i].nombre)
                print('Porcentaje de Finalizacion: ',end='')
                terminadas = 0
                for j in range(0,len(self.proyectos[i].Tareas) - 1):
                    #Contador de Tareas completadas
                    if(self.proyectos[i].Tareas[j].estado == 'Completada'):
                        terminadas += 1
                #Calculo de Porcentaje respecto al total de tareas
                porcentaje = terminadas / len(self.proyectos[i].Tareas) * 100
                print(porcentaje + '\n')

    #ARREGLAR ESTE METODO Y AGREGAR EL OTRO
    def subtareas(self,filtro):
        #Arreglar nombre de atributos
        for i in range(0,len(self.proyectos)-1):
            #Recorrido de Proyectos
            if(self.proyectos[i].nombre == filtro or self.proyectos[i].id == filtro):
                #Verificacion de filtro
                #Salida por pantalla de datos basicos
                print('Nombre del proyecto: ',self.proyectos[i].nombre)
                print('Descripcion del proyecto: ',self.proyectos[i].nombre)
                print('Tareas del ',self.proyectos[i].nombre, ': ')

                for j in range(0,len(self.proyectos[i].Tareas)-1):
                    #Recorrido de tareas
                    #Salida por pantalla de datos basicos de la tarea
                    tarea = self.proyectos[i].Tareas[j]
                    print('\tNombre de la Tarea: ' ,tarea.nombre)
                    print('\tDescripcion de la Tarea: ' ,tarea.nombre)
                    print('\tFecha Inicio de la Tarea: ' ,tarea.nombre)
                    print('\tFecha Final de la Tarea: ' ,tarea.nombre)
                    print('\tPorcentaje de Finalizacion: ',end='')
                    terminadas = 0
                    for j in range(0,len(tarea.subtareas) - 1):
                        #Recorrido de subtareas
                        #Contador de estado de subtarea
                        if(tarea.subtareas[j].estado == 'Completada'):
                            terminadas += 1
                    porcentaje = terminadas / len(tarea.subtareas) * 100
                    print(porcentaje + '\n')