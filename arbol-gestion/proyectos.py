from datetime import datetime
class Proyecto:
    def __init__(self,id,nombre,descripcion,fechaI,fechaV,
                 estadoActual,empresa,gerente,equipo):
        
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaI = fechaI
        self.fechaV = fechaV
        self.estado = estadoActual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo

    def __str__(self) -> str:
         return f"Proyecto: {self.nombre}, Descripcion: {self.descripcion}, Fecha inicio: {self.fechaI}, fecha vencimiento: {self.fechaV},estado: {self.estado}, empresa: {self.empresa}, gerente: {self.gerente}, equipo: {self.equipo}"
class GestorProyecto:
    #Funcion que crear un proyecto
    def crear_proyecto(self,lista):
        id = len(lista) + 1
        nombre = input("Ingrese el nombre del proyecto: ")
        des = input("Ingrese una descripcion al proyectO: ")
        fechaI = input("Ingrese la fecha de inicio del proyecto en el formato YYYY-MM-DD: ")
        fechaV = input("Ingrese la fecha de vencimiento del proyecto en el formato YYYY-MM-DD: ")
        estado = input("Ingrese el estado actual del proyecto: ")
        empresa = input("Ingrese el nombre de la empresa: ")
        gerente = input("Ingrese el nombre del gerente encargado del proyecto: ")
        equipo = input("Ingrese el equipo encargado del proyecto: ")
        proyecto = Proyecto(id,nombre,des,datetime.strptime(fechaI,"%Y-%m-%d"),datetime.strptime(fechaV,"%Y-%m-%d"),
                            estado,empresa,gerente,equipo)
        lista.append(proyecto)
        result_str = [str(proc) for proc in lista]
        listanueva = ','.join(result_str)
        return listanueva
            




    

        
