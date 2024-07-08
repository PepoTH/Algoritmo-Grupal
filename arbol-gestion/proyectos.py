from datetime import datetime
import empresas
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
        self.proyectos = empresas.EmpresaCliente().proyectos
    
    #Funcion que crear un nuevo proyecto
    def crear_proyecto(self,nombre,descripcion,fechaI,fechaV,estado,empresa,gerente,equipo):
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
    # Funcion que obtiene el balance del arbol
    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)
    
    #Funcion que rota el arbol a la derecha
    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y
    
    #Funcion que rota el arbol a la izquierda
    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y
    # Funcion que inserta la fecha de vencimiento al arbol
    def insertar(self,nodo,fechaV):
        if not nodo:
            return nodoArbol(fechaV)
        
        if fechaV < nodo.fechaV:
            nodo.izquierda = self.insertar(nodo.izquierda,fechaV)
        elif fechaV > nodo.fechaV:
            nodo.derecha = self.insertar(nodo.derecha,fechaV)
        else:
            return nodo
        
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        balance = self.obtener_balance(nodo)

        if balance > 1 and fechaV < nodo.izquierda.fechaV:
            return self.rotar_derecha(nodo)
        
        if balance < -1 and fechaV > nodo.derecha.fechaV:
            return self.rotar_izquierda(nodo)
        
        if balance > 1 and fechaV > nodo.izquierda.fechaV:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        
        if balance < -1 and fechaV <  nodo.derecha.fechaV:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo
    
    #Funcion que inserta la fecha de vencimiento
    def insertar_fecha(self, fechaV):
        self.raiz = self.insertar(self.raiz, fechaV)
    
    # Funcion que muestra el arbol
    def in_order(self, nodo):
        if nodo:
            self.in_order(nodo.izquierda)
            print(nodo.fechaV)
            self.in_order(nodo.derecha)

#Menu para la gestion de proyectos
def gestionar_proyectos():
    gestorP = GestorProyecto()
    avl = AVL()

    while True:
        print("1. Crear proyecto")
        print("2. Listar proyectos")
        print("3. Modificar proyecto")
        print("4. Eliminar proyecto")
        print("5. mostrar AVL")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del proyecto: ")
            descripcion = input("Ingrese la descripcion del proyecto: ")
            fechaInicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
            fechaVenci = input("Ingrese la fecha de fin del proyecto (YYYY-MM-DD): ")
            estadoActual = input("Ingrese el estado Actual del proyecto: ")
            empresa = input("Ingrese la empresa del proyecto: ")
            gerente = input("Ingrese el nombre del gerente encargado proyecto: ")
            equipo = input("Ingrese los equipos encargados del proyecto: ")
            result = gestorP.crear_proyecto(nombre,descripcion,datetime.strptime(fechaInicio,"%Y %m %d"), datetime.strptime(fechaVenci,"%Y %m %d")
                                   ,estadoActual,empresa,gerente,equipo)
            print(result)
        elif opcion == "2":
            gestorP.Listar_proyecto()
        elif opcion == "3":
            id = int(input("Ingrese el id del proyecto que quiere modificar:"))
            nombre = input("Ingrese el nombre del proyecto: ")
            descripcion = input("Ingrese la descripcion del proyecto: ")
            fechaInicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
            fechaVenci = input("Ingrese la fecha de fin del proyecto (YYYY-MM-DD): ")
            estadoActual = input("Ingrese el estado Actual del proyecto: ")
            empresa = input("Ingrese la empresa del proyecto: ")
            gerente = input("Ingrese el nombre del gerente encargado proyecto: ")
            equipo = input("Ingrese los equipos encargados del proyecto: ")
            gestorP.modifica_proyecto(id,nombre,descripcion,datetime.strptime(fechaInicio,"%Y %m %d"), datetime.strptime(fechaVenci, "%Y %m %d")
                                      ,estadoActual,empresa,gerente,equipo)
        elif opcion == "4":
            id = int(input("Ingrese el id del proyecto que quiere eliminar: "))
            gestorP.eliminar_proyecto(id)
        
        elif opcion == "5":
            avl.insertar_fecha(datetime.strptime(fechaVenci,"%Y %m %d"))
            avl.insertar_fecha(datetime.strptime(fechaVenci,"%Y %m %d"))
            avl.in_order(avl.raiz)

menu = gestionar_proyectos()
            




    

        
