class reporte:
    def __init__(self,proyectos):
        self.proyectos = proyectos

    def tareas(self,estado):
        #Arreglar los nombres de los atributos de ls proyectos
        for i in range(0,len(self.proyectos)-1):
            #Recorrido de Proyectos
            for j in range(0,len(self.proyectos[i].tareas) - 1):
                #Recorrido de Tareas
                tarea = self.proyectos[i].tareas[j]
                if(tarea.estado == estado):
                    #Verificacion del estado de la tarea
                    print('Nombre de la tarea: ' + tarea.nombre)
                    print('Descripcion de la tarea: ' + tarea.descripcion)
                    print('Fecha de Inicio de la tarea: ' + tarea.fechainit)
                    print('Fecha de Fin de la tarea: ' + tarea.fechafin)
                    print('Subtareas: ')
                    for k in range(0,len(tarea.subtareas)-1):
                        #Recorrido de Subtareas
                        print('\t'+ tarea.subtareas[k].nombre)
                print('\n')

    def proyectos(self,filtro):

        #Arreglar los nombres de los atributos de ls proyectos
        for i in range(0,len(self.proyectos)-1):
            #Recorrido de Proyectos
            if(self.proyectos[i].fechainit == filtro or self.proyectos[i].fechafin == filtro or self.proyectos[i].estado == filtro or self.proyectos[i].empresa == filtro):
                #Verificar si el filtro concuerda con algun parametro
                print('Nombre del proyecto: ',self.proyectos[i].nombre)
                print('Descripcion del proyecto: ',self.proyectos[i].nombre)
                print('Empresa del proyecto: ',self.proyectos[i].nombre)
                print('Fecha de Inicio del proyecto: ',self.proyectos[i].nombre)
                print('Fecha de Fin del proyecto: ',self.proyectos[i].nombre)
                print('Porcentaje de Finalizacion: ',end='')
                terminadas = 0
                for j in range(0,len(self.proyectos[i].tareas) - 1):
                    #Contador de Tareas completadas
                    if(self.proyectos[i].tareas[j].estado == 'Completada'):
                        terminadas += 1
                #Calculo de Porcentaje respecto al total de tareas
                porcentaje = terminadas / len(self.proyectos[i].tareas) * 100
                print(porcentaje + '\n')