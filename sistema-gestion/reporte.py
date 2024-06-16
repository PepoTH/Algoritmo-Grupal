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