from datetime import datetime
import time
#Clase para inicializar los valores
class NodoTarea:
    def __init__(self,id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc):
        self.id = id
        self.nombre = nombre
        self.empresa = empresa
        self.cliente = cliente
        self.descrip = descripcion
        self.fechaI = fechaI
        self.fechaV = fechaV
        self.estado = estadoAc
        self.porce = porc
        self.subtareas = []
        self.siguiente = None
    
    def agregar_subTareas(self):
        lista = []
        id = int(input("Ingrese el id de la tarea: "))
        nom = input("Ingrese el nombre de la subtarea: ")
        descri = input("Ingrese la descri de la subtarea: ")
        estado = input("Ingrese el estado de la subtarea: ")
        porc = input("Ingrese el porcentaje de la subtarea %: ")
        lista = [id,nom,descri,estado,porc]
        self.subtareas.append(lista)

    def eliminar_Subtareas(self):
        self.subtareas.clear()
     

#Clase para hacer todo los metodos de las listas entrelazadas
class LTareas:
    def __init__(self):
        self.cabeza = None
        self.tareas = None

    #Funcion que agrega una tarea
    def agregar_tarea(self,tarea):
        nuevoNodo = tarea
        if not self.cabeza:
            self.cabeza = nuevoNodo
        else:
            aux = self.cabeza
            while aux.siguiente:
                aux = aux.siguiente
            aux.siguiente = nuevoNodo
    
    #Funcion que agrega el elemnto al principio de la lista
    def agregar_en_el_Inicio(self,tarea):
        nuevoNodo = tarea
        nuevoNodo.siguiente = self.cabeza
        self.cabeza = nuevoNodo
    
    #Funcion que elimina un elemento de la lista
    def eliminar_tarea(self,id):
        if not self.cabeza:
            return
        if self.cabeza.id == id:
            self.cabeza = self.cabeza.siguiente
            return
        ante = None
        aux = self.cabeza
        while aux and aux.id != id:
            anterior = aux
            aux = aux.siguiente
        if aux:
            anterior.siguiente = aux.siguiente
    
    #Funcion que modifica una tarea
    def modificar_tarea(self,id):
        aux = self.cabeza
        nuevo_id = int(input("Ingrese el nuevo id"))
        nuevo_nom = input("Ingrese el nuevo nombre: ")
        nuevo_empresa = input("Ingrese la nueva empresa: ")
        nuevo_cliente = input("Ingrese el nuevo cliente: ")
        nueva_descri = input("Ingrese la nueva descripcion: ")
        yI = int(input("Ingrese el nuevo año de inicio: "))
        mI = int(input("Ingrese el nuevo mes de inicio:  "))
        dI = int(input("Ingrese el dia de inicio: "))
        nueva_FechaI = datetime(yI,mI,dI).strftime("%y %m %d")
        yV = int(input("Ingrese el nuevo año de vencimiento: "))
        mV = int(input("Ingrese el nuevo mes de vencimiento:  "))
        dV = int(input("Ingrese el dia de vencimiento: "))
        nueva_FechaV = datetime(yV,mV,dV).strftime("%y %m %d")
        nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
        nuevo_porc = int(input("Ingrese el nuevo porcentaje de la tarea %: "))
        while aux:
            if aux.id == id:
                aux.id = nuevo_id
                aux.nombre = nuevo_nom
                aux.empresa = nuevo_empresa
                aux.cliente = nuevo_cliente
                aux.descrip = nueva_descri
                aux.fechaI = nueva_FechaI
                aux.fechaV = nueva_FechaV
                aux.estado = nuevo_estado
                aux.porce = nuevo_porc
                return True
            aux = aux.siguiente
        return False
    
    #Funcion que busca una tarea
    def Buscar_tarea(self,nombre):
        aux = self.cabeza
        while aux:
            if aux.nombre == nombre:
                return True
            aux = aux.siguiente
        return False
    
    #Funcion que obtiene la posicion de una lista
    def Obtener_tarea(self,id):
        aux = self.cabeza
        pos = 0
        ult = -1
        while aux:
            if aux.id == id:
                return pos
            aux = aux.siguiente
            pos += 1
        return ult
    
    #Funcion que muestra las tareas
    def mostrar_tarea(self):
        aux = self.cabeza
        while aux:
            if len(aux.subtareas) == 0:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce)
            else:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce,aux.subtareas)
            aux = aux.siguiente

class PTareas:
    def __init__(self):
        self.cima= None
    #Funcion que agrega las tareas prioritarias
    def agregar_TareaPrior(self,tarea):
        nuevoNodo = tarea
        nuevoNodo.siguiente = self.cima
        self.cima = nuevoNodo
    def esta_Vacia(self):
        return self.cima is None
    #Funcion que elimina una tarea prioritaria
    def eliminar_tareaPrior(self):
        if not self.cima:
            return None
        elimina = self.cima
        self.cima = self.cima.siguiente
        return elimina
    #Funcion que busca el eleemnto en la Pila y dice si existe o no
    def Buscar_tarea_Prioritaria(self,porc):
        actual = self.cabeza
        while actual:
            if actual.porce == porc:
                return True
            actual = actual.siguiente
        return False
    #Fucncion que modifica una tarea prioritaria
    def modificar_tarea(self,id):
        aux = self.cima
        nuevo_id = int(input("Ingrese el nuevo id de la tarea prioritaria: "))
        nuevo_nom = input("Ingrese el nuevo nombre de la tarea prioritaria: ")
        nuevo_empresa = input("Ingrese la nueva empresa de la tarea prioritaria: ")
        nuevo_cliente = input("Ingrese el nuevo cliente de la tarea prioritaria: ")
        nueva_descri = input("Ingrese la nueva descripcion de la tarea prioritaria: ")
        yI = int(input("Ingrese el nuevo año de inicio: "))
        mI = int(input("Ingrese el nuevo mes de inicio:  "))
        dI = int(input("Ingrese el dia de inicio: "))
        nueva_FechaI = datetime(yI,mI,dI).strftime("%y %m %d")
        yV = int(input("Ingrese el nuevo año de vencimiento: "))
        mV = int(input("Ingrese el nuevo mes de vencimiento:  "))
        dV = int(input("Ingrese el dia de vencimiento: "))
        nueva_FechaV = datetime(yV,mV,dV).strftime("%y %m %d")
        nuevo_estado = input("Ingrese el nuevo estado de la tarea de la tarea prioritaria: ")
        nuevo_porc = int(input("Ingrese el nuevo porcentaje de la tarea de la tarea prioritaria %: "))
        while aux:
            if aux.id == id:
                aux.id = nuevo_id
                aux.nombre = nuevo_nom
                aux.empresa = nuevo_empresa
                aux.cliente = nuevo_cliente
                aux.descrip = nueva_descri
                aux.fechaI = nueva_FechaI
                aux.fechaV = nueva_FechaV
                aux.estado = nuevo_estado
                aux.porce = nuevo_porc
                return True
            aux = aux.siguiente
        return False
    #Funcion que muestra las tareas prioritarias  
    def mostrar_tareaPri(self):
        aux = self.cima
        while aux:
            if len(aux.subtareas) == 0:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce)
            else:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce,aux.subtareas)
            aux = aux.siguiente
class CTareas:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    #Funcion que agrega una tarea
    def agregar_tarea_a_la_Cola(self,tarea):
        nuevoNodo = tarea
        if not self.cabeza:
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            self.cola.siguiente = nuevoNodo
            self.cola = nuevoNodo
    
    #Funcion que busca una tarea segun su id
    def Buscar_tarea_en_la_cola(self,fechaV):
        aux = self.cabeza
        while aux:
            if aux.fechaV == fechaV:
                return True
            aux = aux.siguiente
        return False
    #Funcion que elimina un elemento de la cola
    def Eliminar_tarea_en_la_cola(self):
        if not self.cabeza:
            return None
        eliminar = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return eliminar
    #Funcion que modifica una tarea segun su fecha de vencimiento
    def Modifica_tarea_en_la_cola(self,id):
        aux = self.cabeza
        nuevo_id = int(input("Ingrese el nuevo id de la tarea : "))
        nuevo_nom = input("Ingrese el nuevo nombre de la tarea : ")
        nuevo_empresa = input("Ingrese la nueva empresa de la tarea : ")
        nuevo_cliente = input("Ingrese el nuevo cliente de la tarea : ")
        nueva_descri = input("Ingrese la nueva descripcion de la tarea : ")
        yI = int(input("Ingrese el nuevo año de inicio: "))
        mI = int(input("Ingrese el nuevo mes de inicio:  "))
        dI = int(input("Ingrese el dia de inicio: "))
        nueva_FechaI = datetime(yI,mI,dI).strftime("%y %m %d")
        yV = int(input("Ingrese el nuevo año de vencimiento: "))
        mV = int(input("Ingrese el nuevo mes de vencimiento:  "))
        dV = int(input("Ingrese el dia de vencimiento: "))
        nueva_FechaV = datetime(yV,mV,dV).strftime("%y %m %d")
        nuevo_estado = input("Ingrese el nuevo estado de la tarea de la tarea : ")
        nuevo_porc = int(input("Ingrese el nuevo porcentaje de la tarea de la tarea  %: "))
        while aux:
            if aux.id== id:
                aux.id = nuevo_id
                aux.nombre = nuevo_nom
                aux.empresa = nuevo_empresa
                aux.cliente = nuevo_cliente
                aux.descrip = nueva_descri
                aux.fechaI = nueva_FechaI
                aux.fechaV = nueva_FechaV
                aux.estado = nuevo_estado
                aux.porce = nuevo_porc
                return True
            aux = aux.siguiente
        return False
    #Funcion que obtiene la posicion de la tarea que esta en la cola
    def Obtener_posi_en_la_cola(self,fechaV):
        aux = self.cabeza
        pos = 0
        term = -1
        while aux:
            if aux.fechaV == fechaV:
                return pos
            aux = aux.siguiente
            pos +=1
        return term
    
    #Funcion que muestra las tareas que se encuentra dentros de la cola
    def mostrar_cola(self):
        aux = self.cabeza
        while aux:
            if len(aux.subtareas) == 0:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce)
            else:
                print(aux.id,aux.nombre,aux.empresa,aux.cliente,
                      aux.descrip,aux.fechaI,aux.fechaV,
                      aux.estado,aux.porce,aux.subtareas)
            aux = aux.siguiente

def crearTarea():
    nuevo_id = int(input("Ingrese el id"))
    nuevo_nom = input("Ingrese el nombre: ")
    nuevo_empresa = input("Ingrese la empresa: ")
    nuevo_cliente = input("Ingrese el cliente: ")
    nueva_descri = input("Ingrese la descripcion: ")
    yI = int(input("Ingrese el  año de inicio: "))
    mI = int(input("Ingrese el  mes de inicio:  "))
    dI = int(input("Ingrese el dia de inicio: "))
    nueva_FechaI = datetime(yI,mI,dI).strftime("%y %m %d")
    yV = int(input("Ingrese el  año de vencimiento: "))
    mV = int(input("Ingrese el  mes de vencimiento:  "))
    dV = int(input("Ingrese el dia de vencimiento: "))
    nueva_FechaV = datetime(yV,mV,dV).strftime("%y %m %d")
    nuevo_estado = input("Ingrese el  estado de la tarea: ")
    nuevo_porc = int(input("Ingrese el  porcentaje de la tarea %: "))
    return NodoTarea(nuevo_id,nuevo_nom,nuevo_empresa,nuevo_cliente,nueva_descri,nueva_FechaI,nueva_FechaV,nuevo_estado,nuevo_porc)
#Funcion que elige que metodo quiere utilizar para organizar las tareas
def organizacionTareas():
    #tarea1 = NodoTarea(1,"Tarea1","Empresa1","Cliente1","Descripcion1",datetime(2016,12,2).strftime("%y %m %d")
    #,datetime(2025,7,12).strftime("%y %m %d"),"En progreso",65)
    tarea1 = crearTarea()
    print("Desea agregar una subtarea a la tarea1? (S/N)")
    agreSub = input(" : ")
    if (agreSub.upper() == "S"):
        tarea1.agregar_subTareas()
    else:
        print()
    print("Desea Eliminar una subTarea (S/N)")
    elimSub = input(" : ")
    if (elimSub.upper() == "S"):
        tarea1.eliminar_Subtareas()
    else:
        print()
    tarea2 = NodoTarea(2,"Tarea2","Empresa2","Cliente2","Descripcion2",datetime(2022,4,12).strftime("%y %m %d")
    ,datetime(2024,9,30).strftime("%y %m %d"),"Pendiente",15)

    print("Desea agregar una subtarea a la tarea2? (S/N)")
    agreSub = input(" : ")
    if (agreSub.upper() == "S"):
        tarea2.agregar_subTareas()
    else:
        print()
    print("Desea Eliminar una subTarea (S/N)")
    elimSub = input(" : ")
    if (elimSub.upper() == "S"):
        tarea2.eliminar_Subtareas()
    else:
        print()

    tarea3 = NodoTarea(3,"Tarea3","Empresa3","Cliente3","Descripcion3",datetime(2012,3,6).strftime("%y %m %d")
    ,datetime(2024,8,12).strftime("%y %m %d"),"Completada",45)

    print("Desea agregar una subtarea a la tarea3? (S/N)")
    agreSub = input(" : ")
    if (agreSub.upper() == "S"):
        tarea3.agregar_subTareas()
    else:
        print()
    print("Desea Eliminar una subTarea (S/N)")
    elimSub = input(" : ")
    if (elimSub.upper() == "S"):
        tarea3.eliminar_Subtareas()
    else:
        print()

    print("Hola como quieres organizar las tareas del proyecto: ")
    print("1.Lista entrelazadas")
    print("2.Pila")
    print("3.Cola")
    opc = int(input("Ingrese una opcion: "))
    if (opc == 1):
        organL = LTareas()
        agregar = input("Quiere agregar tareas? (S/N) ")
        if (agregar == "S"):
            print("Que tarea quiere agregar al inicio de la lista: 1.Tarea1, 2.Tarea2, 3.Tarea3: ")
            opc1 = int(input(" : "))
            if (opc1 == 1):
                organL.agregar_en_el_Inicio(tarea1)
                organL.agregar_tarea(tarea2)
                organL.agregar_tarea(tarea3)
            elif(opc1 == 2):
                organL.agregar_en_el_Inicio(tarea2)
                organL.agregar_tarea(tarea1)
                organL.agregar_tarea(tarea3)
            else:
                organL.agregar_en_el_Inicio(tarea3)
                organL.agregar_tarea(tarea2)
                organL.agregar_tarea(tarea3)
        else:
            print("No se agrego nada a la lista!!")
        print("Desea eliminar una tarea: (S/N):")
        opc2 = input(" : ")
        if (opc2.upper() == "S"):
            print("Ingrese el id de la tarea que quiere eliminar")
            id = int(input(":"))
            if (id == 1):
                organL.eliminar_tarea(1)
            elif(id == 2):
                organL.eliminar_tarea(2)
            else:
                organL.eliminar_tarea(3)
        else:
            print("No se elimino nada de la lista")
        print("Desea modificar una tarea: (S/N):")
        opc3 = input(" : ")
        if (opc3.upper() == "S"):
            print("Ingrese el id de la tarea que quiere modificar ")
            id = int(input(" : "))
            if (id == 1):
                organL.modificar_tarea(1)
            elif(id == 2):
                organL.modificar_tarea(2)
            else:
                organL.modificar_tarea(3)
        else:
            print("No se elimino nada de la lista")
        
        print("Quiere hacer algo mas? (S/N)")
        opc4 = input(" : ")
        if (opc4.upper() == "N"):
            organL.mostrar_tarea()
        else:
            print("Quiere buscar un elemento? (S/N)")
            opc5 = input(" : ")
            if (opc5.upper() == "S"):
                nom = input("Ingrese el nombre de la tarea: ")
                result = organL.Buscar_tarea(nom)
                print("Existen la tarea:", result)
            else:
                organL.mostrar_tarea()
    elif (opc == 2):
        organP = PTareas()
        agregar = input("Quiere agregar tareas prioritaria (S/N): ")
        if (agregar.upper() == "S"):
            if(tarea2.porce < tarea1.porce and tarea1.porce < tarea3.porce):
                organP.agregar_TareaPrior(tarea3)
                organP.agregar_TareaPrior(tarea1)
                organP.agregar_TareaPrior(tarea2)
            elif(tarea1.porce < tarea2.porce and tarea2.porce < tarea3.porce):
                organP.agregar_TareaPrior(tarea3)
                organP.agregar_TareaPrior(tarea2)
                organP.agregar_TareaPrior(tarea1)
            elif(tarea3.porce < tarea1.porce and tarea1.porce < tarea2.porce):
                organP.agregar_TareaPrior(tarea2)
                organP.agregar_TareaPrior(tarea1)
                organP.agregar_TareaPrior(tarea3)
            else:
                print("Esta mal organizado")
        print("Desea Eliminar una tarea prioritaria? (S/N)")
        eliminar = input(" : ")
        if (eliminar.upper() == "S"):
            eliminado = organP.eliminar_tareaPrior()
        else:
            print("No se elimino tarea prioritaria")
        print("Desea Modificar una tarea prioritaria? (S/N)")
        modificar = input(" : ")
        if (modificar.upper() == "S"):
            print("Ingrese el id de la tarea prioritaria que quiere modificar")
            id = int(input(" : "))
            if (id == 1):
                organP.modificar_tarea(1)
                if(tarea1.porce < tarea2.porce and tarea2.porce < tarea3.porce):
                    organP.agregar_TareaPrior(tarea3)
                    organP.agregar_TareaPrior(tarea2)
                    organP.agregar_TareaPrior(tarea1)
            elif(id == 2):
                organP.modificar_tarea(2)
                if(tarea2.porce < tarea1.porce and tarea1.porce < tarea3.porce):
                    organP.agregar_TareaPrior(tarea3)
                    organP.agregar_TareaPrior(tarea1)
                    organP.agregar_TareaPrior(tarea2)
            else:
                organP.modificar_tarea(3)
                if(tarea3.porce < tarea2.porce and tarea2.porce < tarea1.porce):
                    organP.agregar_TareaPrior(tarea1)
                    organP.agregar_TareaPrior(tarea2)
                    organP.agregar_TareaPrior(tarea3)
        else:
            print("No se modifico ninguna tarea prioritaria")
        
        print("Quiere hacer algo mas: (S/N)")
        mostrar = input(" : ")
        if(mostrar.upper() == "N"):
            organP.mostrar_tareaPri()
        else:
            print("Quiere buscar un elemento? (S/N)")
            opc5 = input(" : ")
            if (opc5.upper() == "S"):
                porc = int(input("Ingrese el porcentaje que tiene la tarea prioritaria: "))
                result = organP.Buscar_tarea_Prioritaria(porc)
                print("Existen la tarea:", result)
            else:
                organP.mostrar_tareaPri()
    elif(opc == 3):
        organC = CTareas()
        agregar = input("Quiere agregar tareas? (S/N): ")
        if (agregar.upper() == "S"):
            fechaV1 = time.strptime(tarea1.fechaV,"%y %m %d")
            fechaV2 = time.strptime(tarea2.fechaV,"%y %m %d")
            fechaV3 = time.strptime(tarea3.fechaV,"%y %m %d")
            if(fechaV2 < fechaV1 and fechaV1 < fechaV3):
                organC.agregar_tarea_a_la_Cola(tarea2)
                organC.agregar_tarea_a_la_Cola(tarea1)
                organC.agregar_tarea_a_la_Cola(tarea3)
            elif(fechaV1 < fechaV2 and fechaV2 < fechaV3):
                organC.agregar_tarea_a_la_Cola(tarea1)
                organC.agregar_tarea_a_la_Cola(tarea2)
                organC.agregar_tarea_a_la_Cola(tarea3)
            elif(fechaV3 < fechaV2 and fechaV2 < fechaV1):
                organC.agregar_tarea_a_la_Cola(tarea3)
                organC.agregar_tarea_a_la_Cola(tarea2)
                organC.agregar_tarea_a_la_Cola(tarea1)
        else:
            print("Cola vacia o no se agrego nada")
        print("Desea eliminar una tarea? (S/N)")
        eliminar = input(":")
        if(eliminar.upper() == "S"):
            eliminado = organC.Eliminar_tarea_en_la_cola()
        else:
            print("No se elimino nada ninguna tarea")
        print("Desea modificar una tarea")
        modificar = input(" : ")
        if(modificar.upper() == "S"):
            id = int(input(" : "))
            fechaV1 = time.strptime(tarea1.fechaV,"%y %m %d")
            fechaV2 = time.strptime(tarea2.fechaV,"%y %m %d")
            fechaV3 = time.strptime(tarea3.fechaV,"%y %m %d")
            if (id == 1):
                organC.Modifica_tarea_en_la_cola(1)
                if(fechaV1 < fechaV2 and fechaV2 < fechaV3):
                    organC.agregar_tarea_a_la_Cola(tarea3)
                    organC.agregar_tarea_a_la_Cola(tarea2)
                    organC.agregar_tarea_a_la_Cola(tarea1)
            elif(id == 2):
                organC.Modifica_tarea_en_la_cola(2)
                if(fechaV2 < fechaV1 and fechaV1 < fechaV3):
                    organC.agregar_tarea_a_la_Cola(tarea3)
                    organC.agregar_tarea_a_la_Cola(tarea1)
                    organC.agregar_tarea_a_la_Cola(tarea2)
            else:
                organC.Modifica_tarea_en_la_cola(3)
                if(fechaV3 < fechaV2 and fechaV2 < fechaV1):
                    organC.agregar_tarea_a_la_Cola(tarea1)
                    organC.agregar_tarea_a_la_Cola(tarea2)
                    organC.agregar_tarea_a_la_Cola(tarea3)
        else:
            print("No se modifico ninguna tarea")

        print("Quiere hacer algo mas: (S/N)")
        mostrar = input(" : ")
        if(mostrar.upper() == "N"):
            organC.mostrar_cola()
        else:
            print("Quiere buscar un elemento? (S/N)")
            opc5 = input(" : ")
            if (opc5.upper() == "S"):
                fechaV = int(input("Ingrese el porcentaje que tiene la tarea prioritaria: "))
                result = organP.Buscar_tarea_Prioritaria(porc)
                print("Existen la tarea:", result)
            else:
                organC.mostrar_cola()

#ver = organizacionTareas()