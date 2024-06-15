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
    
    def AgregarFinal(self,proyecto): #Función que agrega un proyecto a la cabeza de la lista
        ultimo = self.ultimoProyecto()
        if ultimo != None:
            ultimo.siguiente = proyecto
            proyecto.siguiente = None
        else:
            self.cabeza = proyecto

