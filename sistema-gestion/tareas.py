from datetime import datetime
#Clase para inicializar los valores
class Tarea:
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
        self.listaTarea = Tareas()
    
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
class Tareas:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def ultimoLlamado(self):
        if self.cabeza != None:
            aux = self.cabeza
            while aux.siguiente != None:
                aux = aux.siguiente
        else:
            aux = None
        return aux
    def agregar_final(self,tarea):
        ultimo = self.ultimoLlamado()
        if ultimo != None:
            ultimo.siguiente = tarea
            tarea.siguiente = None
        else:
            self.cabeza = tarea
    
    def agregar_Primero(self,tarea):
        primero = self.cabeza
        if primero != None:
            tarea.siguiente = primero
            self.cabeza = tarea
        else:
            self.cabeza = tarea
    
    def eliminar_tarea(self,valor):
        if self.cabeza == None:
            return False
        if self.cabeza.id == valor:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return True
        aux = self.cabeza
        while aux.siguiente:
            if aux.siguiente.id == valor:
                aux.siguiente = aux.siguiente.siguiente
                self.longitud -= 1
                return True
            aux = aux.siguiente
        return False
    
    def Listadetarea(self):
        aux = self.cabeza
        while aux is not None:
            lista = [aux.id,aux.nombre,aux.empresa,
                  aux.cliente,aux.descrip,aux.fechaI,
                  aux.fechaV,aux.estado,aux.porce]
            if len(aux.subtareas) == 0:
                print(lista)
            else:
                lista = [aux.id,aux.nombre,aux.empresa,
                  aux.cliente,aux.descrip,aux.fechaI,
                  aux.fechaV,aux.estado,aux.porce,aux.subtareas]
                print(lista)
            aux = aux.siguiente
        return aux



organ = Tareas()
tarea1 = Tarea(1,"Jose","Alpha","Carlos","Bestia",datetime.now(),datetime.now(),"En progreso","50%")
tarea2 = Tarea(2,"Jose","Alpha","Carlos","Bestia",datetime.now(),datetime.now(),"En progreso","50%")
print(organ.agregar_final(tarea1))

