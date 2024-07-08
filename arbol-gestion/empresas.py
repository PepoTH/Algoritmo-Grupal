import csv
from datetime import datetime
import proyectos as pro

class Empresa:
    def __init__(self,id,nombre,descripcion,fechaC,
                 direccion,telefono,correo,gerente,equipo_Contacto,proyecto = []):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaCreacion = fechaC
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipoC = equipo_Contacto
        self.proyectos = proyecto
    
class GestorEmpresa:
    def __init__(self,archivo):
        self.empresas = []
        self.cargar_datos(archivo)
    #Funcion que carga los datos en un archivo csv
    def cargar_datos(self,archivo):
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            for arc in reader:
                id,nombre,descripcion,fechaC,direccion,telefono,correo,gerente,equipo_contacto,proyecto = arc
                empresa = Empresa(id,nombre,descripcion,fechaC,direccion,telefono,
                                  correo,gerente,equipo_contacto,proyecto)
                self.empresas.append(empresa)
    
    #Funcion que crea una empresa de un cliente
    def crear_empresa(self, nombre, descripcion, fechaC, direccion, telefono, correo, gerente, equipo_contacto,proyecto):
        if len(self.empresas) >= 0:
            id = len(self.empresas) + 1
            lista = pro.GestorProyecto().crear_proyecto(proyecto)
            empresa = Empresa(id,nombre,descripcion,fechaC,direccion,telefono,
                                      correo,gerente,equipo_contacto,lista)
            self.empresas.append(empresa)
            self.guardar_datos()
            return
        else:
            print("No se han podido crear la empresa")
    
    #Funcion que consulta la empresa del cliente segun su id
    def consultar_empresa(self,id):
        for empresa in self.empresas:
            if empresa.id == id:
                print(f"ID de la empresa: {empresa.id}, Nombre de la empresa: {empresa.nombre}, Descripcion de la empresa: {empresa.descripcion}")
    
    #Funcion que lista la empresa del cliente
    def listar_empresa(self):
        for empresa in self.empresas:
            print(f"ID de la empresa: {empresa.id}, Nombre de la empresa: {empresa.nombre}, Descripcion de la empresa: {empresa.descripcion}")
    
    #Funcion que elimina una empresa segun su Id
    def eliminar_empresa(self,id):
        for empresa in self.empresas:
            if empresa.id == id:
                self.empresas.remove(empresa)
                self.guardar_datos()
                return
        print("No se han encontrado la empresa")
    
    #Funcion que modifica una empresa cliente segun su id
    def modificar_empresa(self,id,nombre,descripcion,fechaC,
                 direccion,telefono,correo,gerente,equipo_Contacto):
        for empresa in self.empresas:
            if empresa.id == id:
                if nombre:
                    empresa.nombre = nombre
                if descripcion:
                    empresa.descripcion = descripcion
                if fechaC:
                    empresa.fechaCreacion = fechaC
                if direccion:
                    empresa.direccion = direccion
                if telefono:
                    empresa.telefono = telefono
                if correo:
                    empresa.correo = correo
                if gerente:
                    empresa.gerente = gerente
                if equipo_Contacto:
                    empresa.equipoC = equipo_Contacto
                self.guardar_datos()
                return
        print("No se encontro la empresa")
    
    #Funcion que guarda la informacion de las empresas en el archivo.csv
    def guardar_datos(self):
        with open('Datos.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Id", "Nombre", "Descripción", "Fecha de creación", "Dirección", "Telefono", "correo", "gerente", "equipo_contacto", "Proyectos"])
            for empresa in self.empresas:
                writer.writerow([empresa.id, empresa.nombre, empresa.descripcion, empresa.fechaCreacion, 
                                 empresa.direccion, empresa.telefono, empresa.correo, empresa.gerente, empresa.equipoC, 
                                 empresa.proyectos])


def menu_empresa():
    
    em = GestorEmpresa('Datos.csv')

    while True:
        print("1. Crear empresa")
        print("2.Consultar empresa")
        print("3.Listar empresa")
        print("4.Eliminar Empresa")
        opc = int(input("Ingrese una opción: "))

        if(opc == 1):
            nombre = input("Ingrese el nombre de la empresa: ")
            descripcion = input("Ingrese uan descripcion a la empresa: ")
            fecha = input("Ingrese la fecha de creación de la empresa en el formato (YYYY-MM-DD): ")
            dire = input("Ingrese la direccion de la empresa: ")
            tlf = input("Ingrese el numero de telefono de la empresa: ")
            correo = input("Ingrese el correo de la empresa: ")
            gerente = input("Ingrese el nombre del gerente de la empresa")
            equipo = input("Ingrese el equpio encargado de la empresa")
            lista = []
            em.crear_empresa(nombre,descripcion,datetime.strptime(fecha,'%Y-%m-%d'),dire,tlf,correo,gerente,equipo,lista)

menu = menu_empresa()