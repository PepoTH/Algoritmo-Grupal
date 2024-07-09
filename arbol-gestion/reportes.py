from empresas import *

class Reportes:
    def __init__(self, gestor_empresa):
        self.gestor_empresa = gestor_empresa

    def reporte_tareas_criticas(self):
        # Implementar lógica para identificar tareas críticas
        pass

    def reporte_sprites_proyecto(self, proyecto_id, nivel_arbol):
        # Implementar lógica para listar sprites de un proyecto específico
        pass

    def reporte_tareas_empleado(self, cedula_empleado):
        # Implementar lógica para listar tareas asignadas a un empleado
        pass

    def mostrar_reportes(self):
        while True:
            print("1. Reporte de tareas críticas")
            print("2. Reporte de sprites de un proyecto")
            print("3. Reporte de tareas asignadas a un empleado")
            print("4. Regresar al menú principal")
            opc = int(input("Ingrese una opción: "))

            if opc == 1:
                self.reporte_tareas_criticas()
            elif opc == 2:
                proyecto_id = int(input("Ingrese el ID del proyecto: "))
                nivel_arbol = int(input("Ingrese el nivel del árbol: "))
                self.reporte_sprites_proyecto(proyecto_id, nivel_arbol)
            elif opc == 3:
                cedula_empleado = input("Ingrese la cédula del empleado: ")
                self.reporte_tareas_empleado(cedula_empleado)
            elif opc == 4:
                break
            else:
                print("Opción inválida")

def menu_reportes(gestor_empresa):

    #pasarle el em del menu de empresa
    reportes = Reportes(gestor_empresa)
    reportes.mostrar_reportes()

#menu = menu_empresa()
em = GestorEmpresa()
reportes = menu_reportes(em)