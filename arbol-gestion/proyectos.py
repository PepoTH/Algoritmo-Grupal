from datetime import datetime
#Clase de los proyectos
class Proyecto:
    def __init__(self,id,nombre,descripcion,fechaI,fechaV,estado,empresa,gerente,equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaI = fechaI
        self.fechaV = fechaV
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
    
class GestorProyecto:
    def __init__(self):
        self.proyectos = []
    
    #Funcion que crear un nuevo proyecto
    def crear_proyecto(self,id,nombre,descripcion,fechaI,fechaV,estado,empresa,gerente,equipo):
        id = len(self.proyectos) + 1
        proyecto = Proyecto(id,nombre,descripcion,fechaI,fechaV,estado,empresa,gerente,equipo)
        self.proyectos.append(proyecto)
    
    #Funcion que elimina un proyecto
    def eliminar_proyecto(self,id):
        for pro in self.proyectos:
            if pro.id == id:
                self.proyectos.remove(pro)
            else:
                print("Error al eliminar el proyecto")
    
    #Funcion que modifica un proyecto
    def modifica_proyecto(self,id,nombre,descrpcion,fechaI,fechaV,estado,empresa,gerente,equipo):
        for pro in self.proyectos:
            if pro.id == id:
                if nombre:
                    pro.nombre = nombre
                if descrpcion:
                    pro.descipcion = descrpcion
                if fechaI:
                    pro.fechaI = fechaI
                if fechaV:
                    pro.fechaV = fechaV
                if estado:
                    pro.estado = estado
                if empresa:
                    pro.gerente = gerente
                if equipo:
                    pro.equipo = equipo
            else:
                print("Error al modificar el proyecto")
    #Funcion que consulta un proyecto
    def consultar_proyecto(self,id):
        for pro in self.proyectos:
            if pro.id == id:
                print(f"Id del proyecto: {pro.id}, Nombre del proyecto: {pro.nombre}, Descripción del proyecto: {pro.descripcion}")
    
    #Funcion que lista un proyecto
    def Listar_proyecto(self,id):
        for pro in self.proyectos:
            print(f"Id del proyecto: {pro.id}, Nombre del proyecto: {pro.nombre}, Descripcion del proyecto {pro.descripcion}")

#Funcion para el nodo del arbol AVL   
class nodoArbol:
    def __init__(self,fechaV):
        self.fechaV = fechaV
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    # Funcion que devuelve la altura del arbol
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    



    

        
