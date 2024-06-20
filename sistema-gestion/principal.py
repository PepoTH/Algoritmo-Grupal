from datetime import datetime
import json, os

class Proyecto:    
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = ListaEnlazada()
        self.porcenta = 0
        self.p = 0

    def agregar_tarea(self, tarea):
        self.tareas.agregar(tarea)
        
    def calcular_p(self):
        if len(self.tareas) > 0:
            self.p = self.porcenta / len(self.tareas)
        else:
            self.p = 0
    
        

class Tarea:
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.porcentaje = porcentaje
        self.subtareas = []

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

class Subtarea:
    def __init__(self, id, nombre, descripcion, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        
def cargar_datos_desde_json(nombre_archivo):
    proyectos = []
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        datos = json.load(archivo)
        for proyecto_data in datos["proyectos"]:
            proyecto = Proyecto(
                proyecto_data["id"],
                proyecto_data["nombre"],
                proyecto_data["descripcion"],
                datetime.strptime(proyecto_data["fecha_inicio"], "%Y-%m-%d"),
                datetime.strptime(proyecto_data["fecha_vencimiento"], "%Y-%m-%d"),
                proyecto_data["estado"],
                proyecto_data["empresa"],
                proyecto_data["gerente"],
                proyecto_data["equipo"]
            )
            for tarea_data in proyecto_data["tareas"]:
                tarea = Tarea(
                    tarea_data["id"],
                    tarea_data["nombre"],
                    tarea_data["empresa_cliente"],
                    tarea_data["descripcion"],
                    datetime.strptime(tarea_data["fecha_inicio"], "%Y-%m-%d"),
                    datetime.strptime(tarea_data["fecha_vencimiento"], "%Y-%m-%d"),
                    tarea_data["estado"],
                    tarea_data["porcentaje"]
                )
                for subtarea_data in tarea_data.get("subtareas", []):
                    subtarea = Subtarea(
                        subtarea_data["id"],
                        subtarea_data["nombre"],
                        subtarea_data["descripcion"],
                        subtarea_data["estado"]
                    )
                    tarea.agregar_subtarea(subtarea)
                proyecto.agregar_tarea(tarea)
            proyecto.calcular_p()
            proyectos.append(proyecto)
    return proyectos

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
#Clase que representa todas las funciones que haremos con listas enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0
    def __len__(self):
        return self.longitud
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.valor
            actual = actual.siguiente
            
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1
        
    def eliminar(self, valor):
        if self.cabeza is None:
            return False
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False
    
    def insertar(self, indice, valor):
        if indice < 0 or indice > self.longitud:
            raise IndexError("Índice fuera de rango")
        nuevo_nodo = Nodo(valor)
        if indice == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for i in range(indice - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1
        
    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor
    
    def index(self, valor):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        raise ValueError("{} no está en la lista".format(valor))
    
    def pop(self, indice=None):
        if indice is None:
            indice = self.longitud - 1
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        if indice == 0:
            varsalor = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return valor
        actual = self.cabeza
        for i in range(indice - 1):
            actual = actual.siguiente
        valor = actual.siguiente.valor
        actual.siguiente = actual.siguiente.siguiente
        self.longitud -= 1
        return valor
#Clase que representa todas las funciones que haremos con la pila
class Pila:
    def __init__(self):
        self.tope = None
    
    def esta_vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo

    def __iter__(self):
        actual = self.tope
        while actual:
            yield actual.valor
            actual = actual.siguiente

    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_eliminado

    def ver_tope(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.valor

    def recorrer(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            self._recorrer_aux(self.tope)

    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor.nombre)
            self._recorrer_aux(nodo.siguiente)
#Clase qe realiza todas las funciones que aremos con la cola
class Cola:
    
    def __init__(self):
        self.frente = None
        self.fin = None
    
    def __iter__(self):
        actual = self.frente
        while actual:
            yield actual.valor
            actual = actual.siguiente

    def esta_vacia(self):
        return self.frente is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo
    
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.fin = None
            return valor_eliminado
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        else:
            return self.frente.valor
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            self._recorrer_aux(self.frente)
    
    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor)
            self._recorrer_aux(nodo.siguiente)

#Clase que modifica el json
class modificar:
    def __init__(self):    
        ruta_archivo = os.path.join(os.getcwd(), "Algoritmo-Grupal/datos.json")
        #ruta_archivo_subtarea = os.path.join(os.getcwd(), "Proyectos_Algoritmos_2/datos_subtareas.json")
        self.proyectox = cargar_datos_desde_json(ruta_archivo)
        #self.proyectox_subtarea = cargar_datos_desde_json(ruta_archivo_subtarea)
    
    # MODULO 3    
    #FILTRAR TAREAS   Inicio
        
    def filtrar_tareas_por_estado(self):
        tareas_filtradas = []
        estado_tarea = input("Ingrese el estado de la tarea: ")
        for proyecto in self.proyectox:
            for tarea in proyecto.tareas:
                if estado_tarea == tarea.estado:
                    tareas_filtradas.append(tarea)
        for x in tareas_filtradas:
            print(x.nombre)
            print(x.estado)
        
    def filtrar_tareas_por_fecha_rango(self):
        tareas_filtradas = []
        fecha_inicio = datetime.strptime(input("Fecha del inicio de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        fecha_fin = datetime.strptime(input("Fecha del fin de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        for proyecto in self.proyectox:
            for tarea in proyecto.tareas:
                if fecha_inicio <= tarea.fecha_inicio <= fecha_fin:
                    tareas_filtradas.append(tarea)
        for x in tareas_filtradas:
            print(x.nombre)
            print(x.fecha_inicio.date())
            print(x.fecha_vencimiento.date())
            
    
    def filtrar_tareas_por_fecha_menor(self):
        tareas_filtradas = []
        fecha_inicio = datetime.strptime(input("Fecha del inicio de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        for proyecto in self.proyectox:
            for tarea in proyecto.tareas:
                if fecha_inicio <= tarea.fecha_inicio:
                    tareas_filtradas.append(tarea)
        for x in tareas_filtradas:
            print(x.nombre)
            print(x.fecha_inicio.date())
            
    
    def filtrar_tareas_por_fecha_mayor(self):
        tareas_filtradas = []
        fecha_inicio = datetime.strptime(input("Fecha del inicio de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        for proyecto in self.proyectox:
            for tarea in proyecto.tareas:
                if fecha_inicio >= tarea.fecha_inicio:
                    tareas_filtradas.append(tarea)
        for x in tareas_filtradas:
            print(x.nombre)
            print(x.fecha_inicio.date())
    
    #FILTRAR TAREAS   Fin
     
    #FILTRAR PROYECTOS   Inicio 
     
    def filtrar_proyectos_por_fecha_rango(self):
        proyectos_f = []
        fecha_inicio = datetime.strptime(input("Fecha del inicio de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        fecha_fin = datetime.strptime(input("Fecha del fin de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        for proyecto in self.proyectox:
            if fecha_inicio <= proyecto.fecha_inicio <= fecha_fin: #SI LA FECHA DE INICIO DEL PROYECTO ESTA DENTRO DEL RANGO QUE INGRESO EL USUARIO
                proyectos_f.append(proyecto)
        for x in proyectos_f:
            print(x.nombre)
            print(x.fecha_inicio.date())
            print(x.fecha_vencimiento.date())
    
    def filtrar_proyectos_por_fecha_menor(self):
        proyectos_f = []
        fecha_inicio = datetime.strptime(input("Fecha del inicio de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        for proyecto in self.proyectox:
            if fecha_inicio <= proyecto.fecha_inicio: #SI LA FECHA DE INICIO DEL PROYECTO ES MAYOR O IGUAL A LA FECHA QUE INGRESO EL USUARIO
                proyectos_f.append(proyecto)
        for x in proyectos_f:
            print(x.nombre)
            print(x.fecha_inicio.date())
    
    def filtrar_proyectos_por_fecha_mayor(self):
        proyectos_f = []
        fecha_inicio = datetime.strptime(input("Fecha del inicio de rango que quiere buscar (Y-m-d) : "), "%Y-%m-%d")
        for proyecto in self.proyectox:
            if fecha_inicio >= proyecto.fecha_inicio: #SI LA FECHA DE INICIO DEL PROYECTO ES MAYOR O IGUAL A LA FECHA QUE INGRESO EL USUARIO
                proyectos_f.append(proyecto)
        for x in proyectos_f:
            print(x.nombre)
            print(x.fecha_inicio.date())
            
    def filtrar_proyecto_por_id(self):
        id_proyecto = int(input("Ingrese el id del proyecto: "))
        proyectos_f = []
        for proyecto in self.proyectox:
            if proyecto.id == id_proyecto:
                proyectos_f.append(proyecto)
        for x in proyectos_f:
            print(x.nombre)
            print(x.id)    
            
    def filtrar_proyecto_por_estado(self):
        estado_proyecto = input("Ingrese el estado del proyecto: ")
        proyectos_f = []
        for proyecto in self.proyectox:
            if proyecto.estado == estado_proyecto:
                proyectos_f.append(proyecto)
        for x in proyectos_f:
            print(x.nombre)
            print(x.estado)
                
    def filtrar_proyecto_por_empresa(self):
        empresa_proyecto = input("Ingrese la empresa del proyecto: ")
        proyectos_f = []
        for proyecto in self.proyectox:
            if proyecto.empresa == empresa_proyecto:
                proyectos_f.append(proyecto)
        for x in proyectos_f:
            print(x.nombre)
            print(x.empresa)   
             
    #FILTRAR PROYECTOS   Fin
    
    #impresion de todas las tareas y subtareas con la info de las subtareas e info relevante sorted jerarquia
    
    def opcion_quicksort(self, proyectos):
        self.quicksort(0, len(proyectos) - 1, proyectos)
        return proyectos
    
    def partition(self, l, r, nume):
        pivot, ptr = nume[r], l
        for i in range(l, r):
            if nume[i].fecha_vencimiento < pivot.fecha_vencimiento:
                nume[i], nume[ptr] = nume[ptr], nume[i]
                ptr += 1
        nume[ptr], nume[r] = nume[r], nume[ptr]
        return ptr

    def quicksort(self, l, r, nume):
        if l < r:
            pi = self.partition(l, r, nume)
            self.quicksort(l, pi - 1, nume)
            self.quicksort(pi + 1, r, nume)
    
    def opcion_quicksort2(self, proyectos):
        self.quicksort2(0, len(proyectos) - 1, proyectos)
        return proyectos
    
    def partition2(self, l, r, nume):
        pivot, ptr = nume[r], l
        for i in range(l, r):
            if nume[i].fecha_vencimiento > pivot.fecha_vencimiento:
                nume[i], nume[ptr] = nume[ptr], nume[i]
                ptr += 1
        nume[ptr], nume[r] = nume[r], nume[ptr]
        return ptr

    def quicksort2(self, l, r, nume):
        if l < r:
            pi = self.partition2(l, r, nume)
            self.quicksort2(l, pi - 1, nume)
            self.quicksort2(pi + 1, r, nume)
    
    def imprimir_todo_ordenado(self):
        proyectosx = self.opcion_quicksort(self.proyectox)
        for proyecto in proyectosx:
            print(proyecto.nombre)
            print(proyecto.estado)
            print(proyecto.fecha_inicio)
            print(proyecto.fecha_vencimiento)
            print(proyecto.empresa)
            for tarea in proyecto.tareas:
                print("\t", tarea.nombre)
                print("\t", tarea.estado)
                print("\t", tarea.fecha_inicio)
                print("\t", tarea.fecha_vencimiento)
                for subtarea in tarea.subtareas:
                    print("\t\t", subtarea.nombre)
                    print("\t\t", subtarea.id)
                    print("\t\t", subtarea.descripcion)
                    print("\t\t", subtarea.estado)
                    
    def Imprimir_Proyectos(self):
        proyectosx = self.opcion_quicksort(self.proyectox)
        cont = 0
        cont_ls = []
        for proyecto in proyectosx:
            cont += 1
            print(f"{cont}. {proyecto.nombre}")
            cont_ls.append(cont)
        return cont_ls
    
    def Imprimir_Tareas(self):
        proyectosx = self.opcion_quicksort(self.proyectox)
        for proyecto in proyectosx:
            for tarea in proyecto.tareas:
                print("\t", tarea.nombre)
                print("\t", tarea.estado)
                print("\t", tarea.fecha_inicio)
                print("\t", tarea.fecha_vencimiento)
    
    
        
                    
    # fin de impresion de todas las tareas y subtareas con la info de las subtareas e info relevante sorted jerarquia  
    """FIN DE MODULO 3  """ 
    

    def Agregar_Proyectos(self):
        id = int(input("Ingrese el id del proyecto: "))
        nombre = input("Ingrese el nombre del proyecto: ")
        descripcion = input("Ingrese la descripcion del proyecto: ")
        while True:
            try:
                fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Año-Mes-Dia): "), "%Y-%m-%d")
                fecha_vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Año-Mes-Dia): "), "%Y-%m-%d")
                if fecha_inicio < fecha_vencimiento:
                    break
            except ValueError:
                print("Fecha inválida, intente de nuevo")
        estado = input("Ingrese el estado del proyecto: ")
        empresa = input("Ingrese la empresa del proyecto: ")
        gerente = input("Ingrese el gerente del proyecto: ")
        equipo = input("Ingrese el equipo del proyecto: ")
        proyecto = Proyecto(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo)
        
        tareita= self.agregar_tareasx(proyecto)
        
        proyecto.agregar_tarea(tareita)    
        self.proyectox.append(proyecto)
        
    
    def Eliminar_Proyectos(self):
       
        
        eli = int(input("Cual Proyecto desea eliminar: "))
        eli -= 1
        self.proyectox.pop(eli)
    
    def Mostrar_Todo(self):
        for proyecto in self.proyectox:
            print(proyecto.nombre)
            for tarea in proyecto.tareas:
                print("\t", tarea.nombre)
                for subtarea in tarea.subtareas:
                    print("\t\t", subtarea.nombre)
    
    def agregar_tareasx(self, proyectoy):
        listoca = ListaEnlazada()
        for tarea in proyectoy.tareas:
            listoca.agregar(tarea)
        i = int(input("Cuantas tareas desea agregar: "))
        a = input("Desea agregar las tareas en una posicion especifica? s/n: ")
        if a =="n":
            while i !=0:
                idt = input("Ingrese el id de la tarea: ")
                nombret = input("Ingrese el nombre de la tarea: ")
                empresa_clientet = input("Ingrese la empresa del cliente: ")
                descripciont = input("Ingrese la descripcion de la tarea: ")
                while True:
                    try:
                        fecha_iniciot = datetime.strptime(input("Ingrese la fecha de inicio de la tarea (Año-Mes-Dia): "), "%Y-%m-%d")
                        fecha_vencimientot = datetime.strptime(input("Ingrese la fecha de vencimiento de la tarea (Año-Mes-Dia): "), "%Y-%m-%d")
                        if fecha_iniciot < fecha_vencimientot:
                            break
                    except ValueError:
                        print("Fecha inválida, intente de nuevo")
                estadot = input("Ingrese el estado de la tarea: ")
                porcentajet = int(input("Ingrese el porcentaje de la tarea: "))
                tareita = Tarea(idt, nombret, empresa_clientet, descripciont, fecha_iniciot, fecha_vencimientot, estadot, porcentajet)
                j = int(input("Cuantas subtareas desea agregar: "))
                
                while j !=0:
                    
                    ids = input("Ingrese el id de la subtarea: ")
                    nombres = input("Ingrese el nombre de la subtarea: ")
                    descripcions = input("Ingrese la descripcion de la subtarea: ")
                    estados = input("Ingrese el estado de la subtarea: ")
                    subtareita = Subtarea(ids, nombres, descripcions, estados)
                    tareita.agregar_subtarea(subtareita)
                    j -= 1
                    
                listoca.agregar(tareita)
                i -= 1
                for ele in listoca:
                    print(ele , end = "")
            return listoca
        
        elif a == "s":
            for ele in listoca:
                print(ele , end = "")
            posi = int(input("En que posición desea insertar la tarea? "))
            posi -= 1
            while i !=0:
                idt = input("Ingrese el id de la tarea: ")
                nombret = input("Ingrese el nombre de la tarea: ")
                empresa_clientet = input("Ingrese la empresa del cliente: ")
                descripciont = input("Ingrese la descripcion de la tarea: ")
                while True:
                    try:
                        fecha_iniciot = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Año-Mes-Dia): "), "%Y-%m-%d")
                        fecha_vencimientot = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Año-Mes-Dia): "), "%Y-%m-%d")
                        if fecha_iniciot < fecha_vencimientot:
                            break
                    except ValueError:
                        print("Fecha inválida, intente de nuevo")
                estadot = input("Ingrese el estado de la tarea: ")
                porcentajet = int(input("Ingrese el porcentaje de la tarea: "))
                tareita = Tarea(idt, nombret, empresa_clientet, descripciont, fecha_iniciot, fecha_vencimientot, estadot, porcentajet)
                j = int(input("Cuantas subtareas desea agregar: "))
                
                while j !=0:
                    
                    ids = input("Ingrese el id de la subtarea: ")
                    nombres = input("Ingrese el nombre de la subtarea: ")
                    descripcions = input("Ingrese la descripcion de la subtarea: ")
                    estados = input("Ingrese el estado de la subtarea: ")
                    subtareita = Subtarea(ids, nombres, descripcions, estados)
                    tareita.agregar_subtarea(subtareita)
                    j -= 1
                    
                listoca.insertar(posi,tareita)
                i -= 1
               
            return listoca
    def pilas_tareas(self):
        
        
        pilal = []
        for proyecto in self.proyectox:
            
            for tarea in proyecto.tareas:
                pilal.append(tarea)
        
        pila_ordenada = self.opcion_quicksort2(pilal)
        return pila_ordenada
    def pilas_tareas2(self):
        
        
        pilal = []
        for proyecto in self.proyectox:
            
            for tarea in proyecto.tareas:
                pilal.append(tarea)
        
        pila_ordenada = self.opcion_quicksort(pilal)
        return pila_ordenada
    
    def ordenar_tareas_pila(self):
        pila_ordenada = self.pilas_tareas()
        self.pila = Pila()
        for x in pila_ordenada:
            self.pila.agregar(x)
        for y in self.pila:
            print("")
            print("\t",y.nombre)
            print("\t",y.empresa_cliente)
            print("\t",y.descripcion)
            print("\t",y.fecha_inicio.date())
            print("\t",y.fecha_vencimiento.date())
            print("\t",y.estado)
    def eliminar_pila(self):
        self.pila.eliminar()

    def recorre_pila(self):
        for y in self.pila:
            print(" ")
            print("\t",y.nombre)
            print("\t",y.empresa_cliente)
            print("\t",y.descripcion)
            print("\t",y.fecha_inicio.date())
            print("\t",y.fecha_vencimiento.date())
            print("\t",y.estado)

    def agregar_pila(self):
        idt = input("Ingrese el id de la tarea: ")
        nombret = input("Ingrese el nombre de la tarea: ")
        empresa_clientet = input("Ingrese la empresa del cliente: ")
        descripciont = input("Ingrese la descripcion de la tarea: ")
        fecha_iniciot = datetime.strptime(input("Ingrese la fecha de inicio de la tarea: "), "%Y-%m-%d")
        fecha_vencimientot = datetime.strptime(input("Ingrese la fecha de vencimiento de la tarea: "), "%Y-%m-%d")
        estadot = input("Ingrese el estado de la tarea: ")
        porcentajet = int(input("Ingrese el porcentaje de la tarea: "))
        tareito = Tarea(idt, nombret, empresa_clientet, descripciont, fecha_iniciot, fecha_vencimientot, estadot, porcentajet)
        j = int(input("Cuantas subtareas desea agregar: "))

        while j !=0:

            ids = input("Ingrese el id de la subtarea: ")
            nombres = input("Ingrese el nombre de la subtarea: ")
            descripcions = input("Ingrese la descripcion de la subtarea: ")
            estados = input("Ingrese el estado de la subtarea: ")
            subtareito = Subtarea(ids, nombres, descripcions, estados)
            tareito.agregar_subtarea(subtareito)
            j -= 1

        self.pila.agregar(tareito)
        

    def ordenar_tareas_colas(self):
        pila_ordenada = self.pilas_tareas2()
        self.cola = Cola()
        for x in pila_ordenada:
            self.cola.agregar(x)

        for y in self.cola:
            print("")
            print("\t",y.nombre)
            print("\t",y.empresa_cliente)
            print("\t",y.descripcion)
            print("\t",y.fecha_inicio.date())
            print("\t",y.fecha_vencimiento.date())
            print("\t",y.estado)

    def eliminar_cola(self):
        self.cola.eliminar()

    def recorre_cola(self):
        for y in self.cola:
            print("")
            print("\t",y.nombre)
            print("\t",y.empresa_cliente)
            print("\t",y.descripcion)
            print("\t",y.fecha_inicio.date())
            print("\t",y.fecha_vencimiento.date())
            print("\t",y.estado)
    
    def agregar_cola(self):

        idt = input("Ingrese el id de la tarea: ")
        nombret = input("Ingrese el nombre de la tarea: ")
        empresa_clientet = input("Ingrese la empresa del cliente: ")
        descripciont = input("Ingrese la descripcion de la tarea: ")
        fecha_iniciot = datetime.strptime(input("Ingrese la fecha de inicio de la tarea: "), "%Y-%m-%d")
        fecha_vencimientot = datetime.strptime(input("Ingrese la fecha de vencimiento de la tarea: "), "%Y-%m-%d")
        estadot = input("Ingrese el estado de la tarea: ")
        porcentajet = int(input("Ingrese el porcentaje de la tarea: "))
        tareito = Tarea(idt, nombret, empresa_clientet, descripciont, fecha_iniciot, fecha_vencimientot, estadot, porcentajet)
        j = int(input("Cuantas subtareas desea agregar: "))

        while j !=0:

            ids = input("Ingrese el id de la subtarea: ")
            nombres = input("Ingrese el nombre de la subtarea: ")
            descripcions = input("Ingrese la descripcion de la subtarea: ")
            estados = input("Ingrese el estado de la subtarea: ")
            subtareito = Subtarea(ids, nombres, descripcions, estados)
            tareito.agregar_subtarea(subtareito)
            j -= 1

        self.cola.agregar(tareito)
       

proyecto = modificar()