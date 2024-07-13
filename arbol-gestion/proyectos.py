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
    def __init__(self):
        self.proyectos = []
    #Funcion que crear un proyecto
    def crear_proyecto(self):
        lista = []
        id = len(self.proyectos) + 1
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
        self.proyectos.append(proyecto)
        return proyecto
    #funcion que modifica un proyecto segun su id
    def modificar_proyecto(self):
        id_proyecto = int(input("Ingrese el ID del proyecto que desea modificar: "))
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                print("Proyecto encontrado!")
                nombre = input("Ingrese el nuevo nombre del proyecto: ")
                des = input("Ingrese la nueva descripcion del proyecto: ")
                fechaI = input("Ingrese la nueva fecha de inicio del proyecto en el formato YYYY-MM-DD: ")
                fechaV = input("Ingrese la nueva fecha de vencimiento del proyecto en el formato YYYY-MM-DD: ")
                estado = input("Ingrese el nuevo estado del proyecto: ")
                empresa = input("Ingrese el nuevo nombre de la empresa: ")
                gerente = input("Ingrese el nuevo nombre del gerente encargado del proyecto: ")
                equipo = input("Ingrese el nuevo equipo encargado del proyecto: ")
                proyecto.nombre = nombre
                proyecto.descripcion = des
                proyecto.fecha_inicio = datetime.strptime(fechaI, "%Y-%m-%d")
                proyecto.fecha_fin = datetime.strptime(fechaV, "%Y-%m-%d")
                proyecto.estado = estado
                proyecto.empresa = empresa
                proyecto.gerente = gerente
                proyecto.equipo = equipo
                print("Proyecto modificado con éxito!")
                return
        print("Proyecto no encontrado!")
    #Funcion que consulta un proyecto segun su id
    def consultar_proyecto(self):
        id_proyecto = int(input("Ingrese el ID del proyecto que desea consultar: "))
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                print(proyecto)
                return
        print("Proyecto no encontrado!")
    #Funcion que elimina un proyecto segun su id
    def eliminar_proyecto(self):
        id_proyecto = int(input("Ingrese el ID del proyecto que desea eliminar: "))
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                self.proyectos.remove(proyecto)
                print("Proyecto eliminado con éxito!")
                return
        print("Proyecto no encontrado!")
    #Funcion que muestra todo los proyectos
    def mostrar_proyectos(self):
        for proyecto in self.proyectos:
            print(proyecto)

class NodoArbol:
    def __init__(self,fechaV):
        self.fechaV = fechaV
        self.izquierda = None
        self.derecha = None
        self.altura = 1
class AVL:
    def __init__(self):
        self.raiz = None
    #Funcion que obtiene la altura del arbol
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    #Funcion que obtiene el balance del arbol
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
    #Funcion que inserta la fecha
    def insertar(self, nodo,fechaV):
        if not nodo:
            return NodoArbol(fechaV)

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

        if balance < -1 and fechaV < nodo.derecha.fechaV:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo
    #Funcion que inserta la fecha
    def insertar_fecha(self,fechaV):
        self.raiz = self.insertar(self.raiz,fechaV)

    def in_order(self, nodo):
        if nodo:
            self.in_order(nodo.izquierda)
            print(nodo.fechaV)
            self.in_order(nodo.derecha)
    

def main():
    gestor = GestorProyecto()
    while True:
        proyectos = []
        print("Menú:")
        print("1. Crear proyecto")
        print("2. Modificar proyecto")
        print("3. Consultar proyecto")
        print("4. Eliminar proyecto")
        print("5. Mostrar todos los proyectos")
        print("6.Arbol AVL")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            result = gestor.crear_proyecto()
            proyectos.append(result.__dict__)
        elif opcion == "2":
            gestor.modificar_proyecto()
        elif opcion == "3":
            gestor.consultar_proyecto()
        elif opcion == "4":
            gestor.eliminar_proyecto()
        elif opcion == "5":
            gestor.mostrar_proyectos()
        elif opcion == "6":
            avl = AVL()
            for proyecto in proyectos:
                fecha_vencimiento = datetime.strptime(proyecto["fecha_vencimiento"], "%Y-%m-%d")
                avl.insertar_fecha(fecha_vencimiento)
            avl.in_order(avl.raiz)
menu = main()
            




    

        
