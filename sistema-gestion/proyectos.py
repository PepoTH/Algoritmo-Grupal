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