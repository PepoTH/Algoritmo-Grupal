from tareas import Tarea,Tareas

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
        self.siguiente = None #Variable que contendrá el siguiente proyecto

    #Setters
    def setId(self,id): self.id=id
    def setNombre(self,nombre): self.nombre=nombre
    def setDescripcion(self,descripcion): self.descripcion=descripcion
    def setFechaInicio(self,fechaInicio): self.fechaInicio=fechaInicio
    def setFechaVencimiento(self,fechaVencimiento): self.fechaVencimiento=fechaVencimiento
    def setEstado(self,estado): self.estado=estado
    def setEmpresa(self,empresa): self.empresa=empresa
    def setGerente(self,gerente): self.gerente=gerente
    def setEquipo(self,equipo): self.equipo=equipo

    #Getters
    def getId(self): return self.id
    def getNombre(self): return self.nombre
    def getDescripcion(self): return self.descripcion
    def getFechaInicio(self): return self.fechaInicio
    def getFechaVencimiento(self): return self.fechaVencimiento
    def getEstado(self): return self.estado
    def getEmpresa(self): return self.empresa
    def getGerente(self): return self.gerente
    def getEquipo(self): return self.equipo

class Proyectos:
    def __init__(self):
        self.cabeza = None

    #Funciones
    def ultimoProyecto(self): #Función que retorna el ultimo proyecto de la lista
        if self.cabeza == None:
            aux = None
            return aux
        else:
            aux = self.cabeza
            while aux.siguiente != None:
                aux = aux.siguiente
        return aux
    
    def agregarProyecto(self,proyecto): #Funcion que agrega un proyecto a la lista
        ultimo = self.ultimoProyecto()
        if ultimo != None:
            ultimo.siguiente = proyecto
            proyecto.siguiente = None
        else:
            self.cabeza = proyecto
    
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
        proyecto = Proyecto(id,nombre,descripcion,fechaInicio,fechaVencimiento,estado,empresa,gerente,equipo)
        self.agregarProyecto(proyecto)

    def buscarProyecto(self):
        print("1. Nombre")
        print("2. ID")
        print("3. Empresa")
        print("4. Equipo")
        opcion = ("Elige un criterio de busqueda (1,2,3,4): ")
        busqueda = input("Ingrese el criterio: ")
        aux = self.cabeza
        while aux != None:
            if opcion == "1" and aux.getNombre == busqueda:
                return aux
            if opcion == "2" and aux.getId == busqueda:
                return aux
            if opcion == "3" and aux.getEmpresa == busqueda:
                return aux
            if opcion == "4" and aux.getEquipo == busqueda:
                return aux
            aux = aux.siguiente
        return print("No hay ningún proyecto con es criterio")

