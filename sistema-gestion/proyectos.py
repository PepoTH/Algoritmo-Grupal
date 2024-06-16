from tareas import Tarea,Tareas

#Clase para la unidad de proyecto
class Proyecto:
    def __init__(self,id,nombre,descripcion="",fechaInicio="",fechaVencimiento="",estado="",empresa="",gerente="",equipo=""):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio
        self.fechaVencimiento = fechaVencimiento
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo

        self.Tareas = Tareas() #Variable que contendrá un dato de tipo 'Tareas'
        self.siguiente = None #Variable que contendrá el siguiente proyecto

    def modificar(self):
        self.id = input("Ingrese el nuevo ID del proyecto: ")
        self.descripcion = input("Ingrese la nueva descripción del proyecto: ")
        self.fechaInicio = input("Ingrese la nueva fecha de inicio: ")
        self.fechaVencimiento = input("Ingrese la nueva fecha de vencimiento: ")
        self.estado = input("Ingrese el nuevo estado del proyecto: ")
        self.equipo = input("Ingrese la nueva empresa del proyecto: ")
        self.gerente = input("Ingrese el nuevo gerente del proyecto: ")
        self.equipo = input("Ingrese el nuevo equipo del proyecto: ")
        self.nombre = input("Ingrese el nuevo nombre del proyecto: ")

class NodoProyectos:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.siguiente = None

class Proyectos:
    def __init__(self):
        self.cabeza = None
    
    def agregarProyecto(self,proyecto): #Funcion que agrega un proyecto a la lista
        NodoNuevo = NodoProyectos(proyecto)
        NodoNuevo.siguiente = self.cabeza
        self.cabeza = NodoNuevo

    def buscar(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None
    
    def crearProyecto(self): #Función que crea un proyecto
        id = input("Ingrese la ID del nuevo proyecto: ")
        nombre = input("Ingrese el nombre del proyecto: ")
        descripcion = input("Ingrese la descripcion del proyecto: ")
        fechaInicio = input("Ingrese la fecha en la que inicia el proyecto: ")
        fechaVencimiento = input("Ingrese la fecha en la que finaliza el proyecto: ")
        estado = input("Ingrese el estado actual del proyecto: ")
        empresa = input("Ingrese la empresa que ocupa el proyecto: ")
        gerente = input("Ingrese el gerente que gestiona el proyecto: ")
        equipo = input("Ingrese el equipo encargado del proyecto: ")
        aux = self.cabeza
        band = True
        while aux != None:
            if aux.nombre == nombre or aux.id == id: band = False
        if band:
            proyecto = Proyecto(id,nombre,descripcion,fechaInicio,fechaVencimiento,estado,empresa,gerente,equipo)
            self.agregarProyecto(proyecto)
        else:
            print("Ya hay un proyecto con el mismo id o nombre")

    def buscarProyecto(self):
        print("Busqueda del proyecto")
        print("1. Nombre")
        print("2. ID")
        print("3. Empresa")
        print("4. Gerente")
        opcion = input("Elige un criterio de busqueda (1,2,3,4): ")
        busqueda = input("Ingrese el criterio: ")
        return busqueda(self.cabeza,opcion,busqueda)
    
    def busqueda(self,aux,op,b):
        if aux != None:
            if op == "1" and aux.nombre == b:
                return aux
            elif op == "2" and aux.id == b:
                return aux
            elif op == "3" and aux.empresa == b:
                return aux
            elif op == "4" and aux.gerente == b:
                return aux
            self.busqueda(aux.siguiente,op,b)
        print("No hay ningún proyecto con ese criterio")
        return None
    
    def modificarProyecto(self):
        viejo = Proyecto("","")
        viejo.id = input("Ingrese el nuevo ID del proyecto: ")
        viejo.nombre = input("Ingrese el nuevo nombre del proyecto: ")
        viejo.descripcion = input("Ingrese la nueva descripción del proyecto: ")
        viejo.fechaInicio = input("Ingrese la nueva fecha de inicio: ")
        viejo.fechaVencimiento = input("Ingrese la nueva fecha de vencimiento: ")
        viejo.estado = input("Ingrese el nuevo estado del proyecto: ")
        viejo.equipo = input("Ingrese la nueva empresa del proyecto: ")
        viejo.gerente = input("Ingrese el nuevo gerente del proyecto: ")
        viejo.equipo = input("Ingrese el nuevo equipo del proyecto: ")
        self.modificar(self.buscarProyecto(),viejo)
    def modificar(self,a,b):
        a = b

while True:
    lista = Proyectos()
    p1 = Proyecto("1","alfa")
    lista.agregarProyecto(p1)
    p2 = Proyecto("2","beta")
    lista.agregarProyecto(p2)
    lista.modificarProyecto()

