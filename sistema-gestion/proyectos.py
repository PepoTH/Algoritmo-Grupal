from tareas import Tareas
from datetime import datetime

#Clase para la unidad de proyecto
class Proyecto:
    def __init__(self,id,nombre,descripcion,fechaInicio,fechaVencimiento,estado,empresa,gerente,equipo):
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

    def modificar(self):
        self.id = input("Ingrese el nuevo ID del proyecto: ")
        self.nombre = input("Ingrese el nuevo nombre del proyecto: ")
        self.descripcion = input("Ingrese la nueva descripción del proyecto: ")
        self.fechaInicio = input("Ingrese la nueva fecha de inicio: ")
        self.fechaVencimiento = input("Ingrese la nueva fecha de vencimiento: ")
        self.estado = input("Ingrese el nuevo estado del proyecto: ")
        self.equipo = input("Ingrese la nueva empresa del proyecto: ")
        self.gerente = input("Ingrese el nuevo gerente del proyecto: ")
        self.equipo = input("Ingrese el nuevo equipo del proyecto: ")

    def mostrar(self):
        print("Id: {}\nNombre: {}\nDescripcion: {}\nFecha de inicio: {}\nFecha de vencimiento: {}\nEstado: {}\nEquipo: {}\nGerente: {}\nEquipo: {}".format(self.id,self.nombre,self.descripcion,self.fechaInicio,self.fechaVencimiento,self.estado,self.empresa,self.gerente,self.equipo))

#Clase para los nodos de la lista entrelazada
class NodoProyectos:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.siguiente = None

#Clase de la lista entrelazada
class Proyectos:
    def __init__(self):
        self.cabeza = None
    
    def agregarProyecto(self,proyecto): #Funcion que agrega un proyecto a la lista
        NodoNuevo = NodoProyectos(proyecto)
        NodoNuevo.siguiente = self.cabeza
        self.cabeza = NodoNuevo

    def buscarProyecto(self,nombre): #Función que busca un proyecto por su nombre
        nodoaux = self.cabeza
        while nodoaux:
            if nodoaux.proyecto.nombre == nombre:
                return nodoaux
            nodoaux = nodoaux.siguiente
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
        p = Proyecto(id,nombre,descripcion,fechaInicio,fechaVencimiento,estado,empresa,gerente,equipo)
        self.agregarProyecto(p)
    
    def modificarProyecto(self): #Función que modifica un proyecto
        nombre = input("Ingrese el nombre del proyecto a modificar: ")
        nodo = self.buscarProyecto(nombre)
        if nodo:
            nodo.proyecto.modificar()
            return True
        else:
            return False
    
    def listarProyectos(self): #Función que lista todos los proyectos
        lista = []
        nodo = self.cabeza
        while nodo:
            lista.append(nodo.proyecto.nombre)
            nodo = nodo.siguiente
        return lista

    def borrarProyecto(self): #Función que borra un proyecto
        nombre = input("Ingrese el nombre del proyecto a borrar: ")
        nodo = self.cabeza
        prev = None
        while nodo:
            if nodo.proyecto.nombre == nombre:
                if prev:
                    prev.siguiente = nodo.siguiente
                else:
                    self.cabeza = nodo.siguiente
                return True
            prev = nodo
            nodo = nodo.siguiente
        return False
    
    def consultarProyecto(self): #Función que consulta un proyecto
        nombre = input("Ingrese el nombre del proyecto a consultar: ")
        nodo = self.buscarProyecto(nombre)
        if nodo: nodo.proyecto.mostrar()

#Prueba
lista = Proyectos()
p1 = Proyecto("1","alfa","Proyecto 1",datetime.now(),datetime.now(),"Completada","UJAP","Santana","JAC")
lista.agregarProyecto(p1)
p2 = Proyecto("2","beta","Proyecto 2",datetime.now(),datetime.now(),"Completada","UJAP","Cesar","JAC")
lista.agregarProyecto(p2)
print(lista.listarProyectos())
lista.modificarProyecto()
print(lista.listarProyectos())
lista.crearProyecto()
print(lista.listarProyectos())
lista.borrarProyecto()
print(lista.listarProyectos())
lista.consultarProyecto()