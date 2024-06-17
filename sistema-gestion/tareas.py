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
    
    def modificar_subTareas(self,id):
        nuevo_id = int(input("Ingrese el nuevo id"))
        nuevo_nom = input("Ingrese el nuevo nombre: ")
        nueva_descri = input("Ingrese la nueva descripcion: ")
        nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
        nuevo_porc = input("Ingrese el nuevo porcentaje de la tarea %: ")
        listaNueva = [nuevo_id,nuevo_nom,nueva_descri,nuevo_estado,nuevo_porc]
        for i in range(len(self.subtareas)):
            if self[i].subtareas == id:
                self.subtareas.append(listaNueva)

        

#Clase para hacer todo los metodos de las listas entrelazadas
class LTareas:
    def __init__(self):
        self.cabeza = None

    #Funcion que agrega una tarea
    def agregar_tarea(self,tarea):
        nuevoNodo = tarea
        if not self.cabeza:
            self.cabeza = nuevoNodo
        else:
            aux = self.cabeza
            while aux.siguiente:
                aux = aux.siguiente
            aux.siguiente = nuevoNodo
    
    #Funcion que agrega el elemnto al principio de la lista
    def agregar_en_el_Inicio(self,tarea):
        nuevoNodo = tarea
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
    
    #Funcion que modifica una tarea
    def modificar_tarea(self,id):
        aux = self.cabeza
        nuevo_id = int(input("Ingrese el nuevo id"))
        nuevo_nom = input("Ingrese el nuevo nombre: ")
        nuevo_empresa = input("Ingrese la nueva empresa: ")
        nuevo_cliente = input("Ingrese el nuevo cliente: ")
        nueva_descri = input("Ingrese la nueva descripcion: ")
        nueva_FechaI = input("Ingrese la nueva fecha inicio: ")
        nueva_FechaV = input("Ingrese la nueva fecha de vencimiento: ")
        nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
        nuevo_porc = int(input("Ingrese el nuevo porcentaje de la tarea %: "))
        while aux:
            if aux.id == id:
                aux.id = nuevo_id
                aux.nombre = nuevo_nom
                aux.empresa = nuevo_empresa
                aux.cliente = nuevo_cliente
                aux.descrip = nueva_descri
                aux.fechaI = nueva_FechaI
                aux.fechaV = nueva_FechaV
                aux.estado = nuevo_estado
                aux.porce = nuevo_porc
                return True
            aux = aux.siguiente
        return False
    
    #Funcion que busca una tarea
    def Buscar_tarea(self,id):
        aux = self.cabeza
        while aux:
            if aux.id == id:
                return True
            aux = aux.siguiente
        return False
    
    #Funcion que obtiene la posicion de una lista
    def Obtener_tarea(self,id):
        aux = self.cabeza
        pos = 0
        ult = -1
        while aux:
            if aux.id == id:
                return pos
            aux = aux.siguiente
            pos += 1
        return ult
    
    #Funcion que muestra las tareas
    def mostrar_tarea(self):
        aux = self.cabeza
        while aux:
            if len(aux.subtareas) == 0:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce)
            else:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce,aux.subtareas)
            aux = aux.siguiente

class PTareas:
    def __init__(self):
        self.cima= None
    #Funcion que agrega las tareas prioritarias
    def agregar_TareaPrior(self,tarea):
        nuevoNodo = tarea
        nuevoNodo.siguiente = self.cima
        self.cima = nuevoNodo
    def esta_Vacia(self):
        return self.cima is None
    #Funcion que elimina una tarea prioritaria
    def eliminar_tareaPrior(self):
        if not self.cima:
            return None
        elimina = self.cima
        self.cima = self.cima.siguiente
        return elimina
    #Funcion que muestra las tareas prioritarias  
    def mostrar_tareaPri(self):
        aux = self.cima
        while aux:
            if len(aux.subtareas) == 0:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce)
            else:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce,aux.subtareas)
            aux = aux.siguiente
organ = LTareas()
tarea1 = NodoTarea(1,"Tarea1","Aplha","Jorge","Bestia",datetime.now(),datetime.now(),"En progreso",50)
tarea2 = NodoTarea(2,"Tarea2","Omega","Luis","don Juan",datetime.now(),datetime.now(),"Completada",100)
tarea3 = NodoTarea(3,"Tarea3","Chi","Susan","wwe",datetime.now(),datetime.now(),"Pendiente",12)
organ.agregar_tarea(tarea2)
organ.agregar_en_el_Inicio(tarea1)
organ.agregar_tarea(tarea3)
organ.mostrar_tarea()
print("-----------------------------------------------------------")
organP = PTareas()
if(tarea1.porce < tarea2.porce and tarea3.porce < tarea2.porce):
    organP.agregar_TareaPrior(tarea2)
    organP.agregar_TareaPrior(tarea1)
    organP.agregar_TareaPrior(tarea3)
    organP.mostrar_tareaPri()
    result = organP.mostrar_Cima()