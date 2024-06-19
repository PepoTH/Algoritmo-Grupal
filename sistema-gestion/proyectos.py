from datetime import datetime
from tareas import *
import json

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
        self.Tareas = [] #Variable que contendrá un dato de tipo 'Tareas'

    def crearTarea(self,id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc):
        self.Tareas.append(NodoTarea(id,nombre,empresa,cliente,descripcion,fechaI,fechaV,estadoAc,porc))

    def mostrar(self):
        print("Id: {}\nNombre: {}\nDescripcion: {}\nFecha de inicio: {}\nFecha de vencimiento: {}\nEstado: {}\nEquipo: {}\nGerente: {}\nEquipo: {}".format(self.id,self.nombre,self.descripcion,self.fechaInicio,self.fechaVencimiento,self.estado,self.empresa,self.gerente,self.equipo))

#Clase para los nodos de la lista entrelazada
class NodoProyectos:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.siguiente = None

#Clase de la lista entrelazada
class Proyectos: 
    def __init__(self):
        self.cabeza = None
    
    def agregarProyecto(self,proyecto): #Funcion que agrega un proyecto a la lista
        NodoNuevo = NodoProyectos(proyecto)
        NodoNuevo.siguiente = self.cabeza
        self.cabeza = NodoNuevo

    def buscarProyecto(self,nombre): #Función que busca un proyecto por su nombre
        nodoaux = self.cabeza
        while nodoaux:
            if nodoaux.proyecto.nombre == nombre:
                return nodoaux
            nodoaux = nodoaux.siguiente
        return None
    
    def borrarProyectoJSON(self):
        nombre = input("Ingrese el nombre del proyecto a borrar: ")
        with open('datos.json', 'r') as file:
            data = json.load(file)
        for i, proyecto in enumerate(data['Proyectos']):
            if proyecto['Nombre'] == nombre:
                del data['Proyectos'][i]
                with open('datos.json', 'w') as file:
                    json.dump(data, file, indent=4)
                print("Proyecto eliminado con éxito")
                return
        print("Proyecto no encontrado")
    
    def consultarProyectoJSON(self):
        nombre = input("Ingrese el nombre del proyecto a consultar: ")
        with open('datos.json', 'r') as file:
            data = json.load(file)
        for proyecto in data['Proyectos']:
            if proyecto['Nombre'] == nombre:
                print("Id: {}\nNombre: {}\nDescripcion: {}\nFecha de inicio: {}\nFecha de vencimiento: {}\nEstado: {}\nEquipo: {}\nGerente: {}\nEmpresa: {}".format(
                    proyecto['ID'], proyecto['Nombre'], proyecto['Descripcion'], proyecto['Fecha de Inicio'], proyecto['Fecha de Vencimiento'], proyecto['Estado'], proyecto['Equipo'], proyecto['Gerente'], proyecto['Empresa']
                ))
                return
        print("Proyecto no encontrado")
    
    
    def crearProyecto(self): #Función que crea un proyecto
        id = int(input("Ingrese la ID del nuevo proyecto: "))
        nombre = input("Ingrese el nombre del proyecto: ")
        descripcion = input("Ingrese la descripcion del proyecto: ")
        fechaInicio = input("Ingrese la fecha en la que inicia el proyecto: ")
        fechaVencimiento = input("Ingrese la fecha en la que finaliza el proyecto: ")
        estado = input("Ingrese el estado actual del proyecto: ")
        empresa = input("Ingrese la empresa que ocupa el proyecto: ")
        gerente = input("Ingrese el gerente que gestiona el proyecto: ")
        equipo = input("Ingrese el equipo encargado del proyecto: ")

        tareas1 = input("Desea agregar tareas?(s/n): ")
        agregartareas = []

        if(tareas1=='s'):
            cantidad = int(input('Cuantas Tareas?: '))
            
            for i in range(0,cantidad):
                agregartareas.append(crearTarea())
            pass
        else:
            agregartareas = []
        #Vinculacion con Tareas y  Subtareas

        with open('datos.json', 'r') as file:
            data = json.load(file)

        data['Proyectos'].append({
        'ID': id,
        'Nombre': nombre,
        'Descripcion': descripcion,
        'Fecha de Inicio': fechaInicio,
        'Fecha de Vencimiento': fechaVencimiento,
        'Estado': estado,
        'Empresa': empresa,
        'Gerente': gerente,
        'Equipo': equipo ,
        'tareas': [{
            'ID':'',
            'Nombre': '',
            'Cliente': '',
            'Descripcion': '',
            'Fecha de Inicio': '',
            'Fecha de Vencimiento': '',
            'Estado': '',
            'Empresa': '',
            'Porcentaje': ''  
        }]
        })  

        index = 0
        for i in range(0,len(data['Proyectos']) - 1):
            if(data['Proyectos'][i]['Nombre'] == nombre):
                index = i
                break

        print('\n\n', data['Proyectos'][index]['tareas'], '\n\n')


        for j in range(0,len(agregartareas)):
            tarea_id = data['Proyectos'][index]['tareas'].id
            tarea_name = data['Proyectos'][index]['tareas'].nombre
            tarea_empresa = data['Proyectos'][index]['tareas'].empresa
            tarea_cliente = data['Proyectos'][index]['tareas'].cliente
            tarea_descripcion = data['Proyectos'][index]['tareas'].descripcion
            tarea_fechaI = data['Proyectos'][index]['tareas'].fechaI
            tarea_fechaV = data['Proyectos'][index]['tareas'].fechaV
            tarea_estado = data['Proyectos'][index]['tareas'].estado
            tarea_porce = data['Proyectos'][index]['tareas'].porce

            data['Proyectos'][index]['tareas'].append({
                'ID':tarea_id,
                'Nombre': tarea_name,
                'Cliente': tarea_cliente,
                'Descripcion': tarea_descripcion,
                'Fecha de Inicio': tarea_fechaI,
                'Fecha de Vencimiento': tarea_fechaV,
                'Estado': tarea_estado,
                'Empresa': tarea_empresa,
                'Porcentaje': tarea_porce
            })
              

        with open('datos.json','w') as file:
            json.dump(data,file,indent=4)

        p = Proyecto(id,nombre,descripcion,fechaInicio,fechaVencimiento,estado,empresa,gerente,equipo)
        self.agregarProyecto(p)
    
    def modificarProyecto(self): #Función que modifica un proyecto
        nombre_viejo = str(input('Ingrese el nombre del proyecto a cambiar: '))

        with open('datos.json','r') as archivo:
            data = json.load(archivo)

        names = []
        for elemento in data['Proyectos']:
            names.append(elemento['Nombre'])

        if not nombre_viejo in names:
            return print('Proyecto no Encontrado')
        
        #nodo = self.buscarProyecto(nombre)
        id = input("Ingrese el nuevo ID del proyecto: ")
        nombre = input("Ingrese el nuevo nombre del proyecto: ")
        descripcion = input("Ingrese la nueva descripción del proyecto: ")
        fechaInicio = input("Ingrese la nueva fecha de inicio: ")
        fechaVencimiento = input("Ingrese la nueva fecha de vencimiento: ")
        estado = input("Ingrese el nuevo estado del proyecto: ")
        empresa = input("Ingrese la nueva empresa del proyecto: ")
        gerente = input("Ingrese el nuevo gerente del proyecto: ")
        equipo = input("Ingrese el nuevo equipo del proyecto: ")

        for elemento in data['Proyectos']:
            if(elemento['Nombre'] == nombre_viejo):
                elemento.update({'ID': id})
                elemento.update({'Nombre': nombre})
                elemento.update({'Descripcion': descripcion})
                elemento.update({'Fecha de Inicio': fechaInicio})
                elemento.update({'Fecha de Vencimiento': fechaVencimiento})
                elemento.update({'Estado': estado})
                elemento.update({'Empresa': empresa})
                elemento.update({'Gerente': gerente})
                elemento.update({'Equipo': equipo})

        with open('datos.json','w') as file:
            json.dump(data,file,indent=4)
    
    def listarProyectos(self): #Función que lista todos los proyectos
        lista = []
        nodo = self.cabeza
        while nodo:
            lista.append(nodo.proyecto)
            nodo = nodo.siguiente
        return lista

    def borrarProyecto(self): #Función que borra un proyecto
        nombre = input("Ingrese el nombre del proyecto a borrar: ")
        nodo = self.cabeza
        prev = None
        while nodo:
            if nodo.proyecto.nombre == nombre:
                if prev:
                    prev.siguiente = nodo.siguiente
                else:
                    self.cabeza = nodo.siguiente
                return True
            prev = nodo
            nodo = nodo.siguiente
        return False
    
    def consultarProyecto(self): #Función que consulta un proyecto
        nombre = input("Ingrese el nombre del proyecto a consultar: ")
        nodo = self.buscarProyecto(nombre)
        if nodo: nodo.proyecto.mostrar()

#Prueba
"""
lista = Proyectos()
p1 = Proyecto("1","alfa","Proyecto 1",datetime.now(),datetime.now(),"Completada","UJAP","Santana","JAC")
lista.agregarProyecto(p1)
p2 = Proyecto("2","beta","Proyecto 2",datetime.now(),datetime.now(),"Completada","UJAP","Cesar","JAC")
lista.agregarProyecto(p2)
print(lista.listarProyectos())
lista.modificarProyecto()
print(lista.listarProyectos())
lista.crearProyecto()
print(lista.listarProyectos())
lista.borrarProyecto()
print(lista.listarProyectos())
lista.consultarProyecto()
"""