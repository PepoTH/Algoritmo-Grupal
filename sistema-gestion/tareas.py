from datetime import datetime
#Clase para inicializar los valores
class NodoTarea:
    def __init__(self,id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc):
        self.id = id
        self.nombre = nombre
        self.empresa = empresa
        self.cliente = cliente
        self.descrip = descripcion
        self.fechaI = fechaI
        self.fechaV = fechaV
        self.estado = estadoAc
        self.porce = porc
        self.subtareas = []
        self.siguiente = None
    
    def agregar_subTareas(self):
        lista = []
        id = int(input("Ingrese el id de la tarea: "))
        nom = input("Ingrese el nombre de la subtarea: ")
        descri = input("Ingrese la descri de la subtarea: ")
        estado = input("Ingrese el estado de la subtarea: ")
        porc = input("Ingrese el porcentaje de la subtarea %: ")
        lista = [id,nom,descri,estado,porc]
        self.subtareas.append(lista)
    def eliminar_Subtareas(self):
        self.subtareas.clear()
        

#Clase para hacer todo los metodos de las listas entrelazadas
class LTareas:
    def __init__(self):
        self.cabeza = None

    #Funcion que agrega una tarea
    def agregar_tarea(self,id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc):
        nuevoNodo = NodoTarea(id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc)
        if not self.cabeza:
            self.cabeza = nuevoNodo
        else:
            aux = self.cabeza
            while aux.siguiente:
                aux = aux.siguiente
            aux.siguiente = nuevoNodo
    
    #Funcion que agrega el elemnto al principio de la lista
    def agregar_en_el_Inicio(self,id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc):
        nuevoNodo = NodoTarea(id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc)
        nuevoNodo.siguiente = self.cabeza
        self.cabeza = nuevoNodo
    
    #Funcion que elimina un elemento de la lista
    def eliminar_tarea(self,id):
        if not self.cabeza:
            return
        if self.cabeza.id == id:
            self.cabeza = self.cabeza.siguiente
            return
        ante = None
        aux = self.cabeza
        while aux and aux.id != id:
            anterior = aux
            aux = aux.siguiente
        if aux:
            anterior.siguiente = aux.siguiente
    
    





organ = LTareas()
tarea1 = NodoTarea(1,"Jose","Alpha","Carlos","Bestia",datetime.now(),datetime.now(),"En progreso","50%")
tarea2 = NodoTarea(2,"Jose","Alpha","Carlos","Bestia",datetime.now(),datetime.now(),"En progreso","50%")
tarea3 = NodoTarea(3,"Jose","Alpha","Carlos","Bestia",datetime.now(),datetime.now(),"En progreso","50%")
organ.agregar_final(tarea1)
organ.agregar_Primero(tarea2)
organ.agregar_Primero(tarea3)
organ.eliminar_tareas()
organ.Listadetarea()

