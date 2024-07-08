import csv
from datetime import datetime

class EmpresaCliente:
    def __init__(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto
        self.proyectos = []

class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_fin):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class GestorEmpresas:
    def __init__(self, archivo_csv):
        self.empresas = []
        self.cargar_datos(archivo_csv)

    def cargar_datos(self, archivo_csv):
        with open(archivo_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la fila de encabezados
            for row in reader:
                id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto = row
                fecha_creacion = datetime.strptime(fecha_creacion, '%Y-%m-%d')
                empresa = EmpresaCliente(id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto)
                self.empresas.append(empresa)

    def crear_empresa(self, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        id = len(self.empresas) + 1
        empresa = EmpresaCliente(id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto)
        self.empresas.append(empresa)
        self.guardar_datos()

    def listar_empresas(self):
        for empresa in self.empresas:
            print(f"ID: {empresa.id}, Nombre: {empresa.nombre}, Descripcion: {empresa.descripcion}")

    def modificar_empresa(self, id, nombre=None, descripcion=None, fecha_creacion=None, direccion=None, telefono=None, correo=None, gerente=None, equipo_contacto=None):
        for empresa in self.empresas:
            if empresa.id == id:
                if nombre:
                    empresa.nombre = nombre
                if descripcion:
                    empresa.descripcion = descripcion
                if fecha_creacion:
                    empresa.fecha_creacion = fecha_creacion
                if direccion:
                    empresa.direccion = direccion
                if telefono:
                    empresa.telefono = telefono
                if correo:
                    empresa.correo = correo
                if gerente:
                    empresa.gerente = gerente
                if equipo_contacto:
                    empresa.equipo_contacto = equipo_contacto
                self.guardar_datos()
                return
        print("Empresa no encontrada")

    def consultar_empresa(self, id):
        for empresa in self.empresas:
            if empresa.id == id:
                print(f"ID: {empresa.id}, Nombre: {empresa.nombre}, Descripcion: {empresa.descripcion}")
                return
        print("Empresa no encontrada")

    def eliminar_empresa(self, id):
        for empresa in self.empresas:
            if empresa.id == id:
                self.empresas.remove(empresa)
                self.guardar_datos()
                return
        print("Empresa no encontrada")

    def guardar_datos(self):
        with open('empresas.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nombre", "descripcion", "fecha_creacion", "direccion", "telefono", "correo", "gerente", "equipo_contacto"])
            for empresa in self.empresas:
                writer.writerow([empresa.id, empresa.nombre, empresa.descripcion, empresa.fecha_creacion.strftime('%Y-%m-%d'), empresa.direccion, empresa.telefono, empresa.correo, empresa.gerente, empresa.equipo_contacto])

    def gestionar_proyectos(self, id_empresa):
        for empresa in self.empresas:
            if empresa.id == id_empresa:
                while True:
                    print("1. Crear proyecto")
                    print("2. Listar proyectos")
                    print("3. Modificar proyecto")
                    print("4. Eliminar proyecto")
                    print("5. Volver")
                    opcion = input("Seleccione una opción: ")
                    if opcion == "1":
                        nombre = input("Ingrese el nombre del proyecto: ")
                        descripcion = input("Ingrese la descripción del proyecto: ")
                        fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
                        fecha_fin = input("Ingrese la fecha de fin del proyecto (YYYY-MM-DD): ")
                        proyecto = Proyecto(len(empresa.proyectos) + 1, nombre, descripcion, datetime.strptime(fecha_inicio, '%Y-%m-%d'), datetime.strptime(fecha_fin, '%Y-%m-%d'))
                        empresa.proyectos.append(proyecto)
                    elif opcion == "2":
                        for proyecto in empresa.proyectos:
                            print(f"ID: {proyecto.id}, Nombre: {proyecto.nombre}, Descripcion: {proyecto.descripcion}")
                    elif opcion == "3":
                        id_proyecto = int(input("Ingrese el ID del proyecto a modificar: "))
                        for proyecto in empresa.proyectos:
                            if proyecto.id == id_proyecto:
                                nombre = input("Ingrese el nuevo nombre del proyecto: ")
                                descripcion = input("Ingrese la nueva descripción del proyecto: ")
                                fecha_inicio = input("Ingrese la nueva fecha de inicio del proyecto (YYYY-MM-DD): ")
                                fecha_fin = input("Ingrese la nueva fecha de fin del proyecto (YYYY-MM-DD): ")
                                proyecto.nombre = nombre
                                proyecto.descripcion = descripcion
                                proyecto.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
                                proyecto.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
                                break
                    elif opcion == "4":
                        id_proyecto = int(input("Ingrese el ID del proyecto a eliminar: "))
                        for proyecto in empresa.proyectos:
                            if proyecto.id == id_proyecto:
                                empresa.proyectos.remove(proyecto)
                                break
                    elif opcion == "5":
                        break
                return
        print("Empresa no encontrada")

gestor = GestorEmpresas("empresas.csv")

while True:
    print("1. Crear empresa")
    print("2. Listar empresas")
    print("3. Modificar empresa")
    print("4. Consultar empresa")
    print("5. Eliminar empresa")
    print("6. Gestionar proyectos")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre de la empresa: ")
        descripcion = input("Ingrese la descripción de la empresa: ")
        fecha_creacion = input("Ingrese la fecha de creación de la empresa (YYYY-MM-DD): ")
        direccion = input("Ingrese la dirección de la empresa: ")
        telefono = input("Ingrese el teléfono de la empresa: ")
        correo = input("Ingrese el correo electrónico de la empresa: ")
        gerente = input("Ingrese el nombre del gerente de la empresa: ")
        equipo_contacto = input("Ingrese el nombre del equipo de contacto de la empresa: ")
        gestor.crear_empresa(nombre, descripcion, datetime.strptime(fecha_creacion, '%Y-%m-%d'), direccion, telefono, correo, gerente, equipo_contacto)
    elif opcion == "2":
        gestor.listar_empresas()
    elif opcion == "3":
        id = int(input("Ingrese el ID de la empresa a modificar: "))
        nombre = input("Ingrese el nuevo nombre de la empresa: ")
        descripcion = input("Ingrese la nueva descripción de la empresa: ")
        fecha_creacion = input("Ingrese la nueva fecha de creación de la empresa (YYYY-MM-DD): ")
        direccion = input("Ingrese la nueva dirección de la empresa: ")
        telefono = input("Ingrese el nuevo teléfono de la empresa: ")
        correo = input("Ingrese el nuevo correo electrónico de la empresa: ")
        gerente = input("Ingrese el nuevo nombre del gerente de la empresa: ")
        equipo_contacto = input("Ingrese el nuevo nombre del equipo de contacto de la empresa: ")
        gestor.modificar_empresa(id, nombre, descripcion, datetime.strptime(fecha_creacion, '%Y-%m-%d'), direccion, telefono, correo, gerente, equipo_contacto)
    elif opcion == "4":
        id = int(input("Ingrese el ID de la empresa a consultar: "))
        gestor.consultar_empresa(id)
    elif opcion == "5":
        id = int(input("Ingrese el ID de la empresa a eliminar: "))
        gestor.eliminar_empresa(id)
    elif opcion == "6":
        id = int(input("Ingrese el ID de la empresa para gestionar proyectos: "))
        gestor.gestionar_proyectos(id)
    elif opcion == "7":
        break