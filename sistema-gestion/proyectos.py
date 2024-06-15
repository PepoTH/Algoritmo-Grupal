#Clase para la unidad de proyecto
class proyecto:
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

        self.Tareas

    #Funciones


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