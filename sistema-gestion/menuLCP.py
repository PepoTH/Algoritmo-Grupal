import principal as main
main = main.modificar()


class Menu:
    def __init__(self):
        self.opciones = []
        self.titulo = ""
        self.menu = ""
        self.opcion = 0
        self.salir = False
        self.opcion = 0

    def Mostrar_Menu(self):
        main.ordenar_tareas_pila()
        main.ordenar_tareas_colas()
        while True:
            print("********************************************************************")
            print("     ------------Bienvenido al sistema administrativo-----------    ")
            print("********************************************************************")
            print("")
            print("¿Qué desea hacer?")
            print("1. Crear Proyecto")
            print("2. Modificar Proyecto")
            print("3. Consultar Proyecto")
            print("4. Eliminar Proyecto")
            print("5. Listar Proyectos")
            print("6. Agregar Tarea")
            print("7. Tareas")
            print("8. Reporte")
            print("9. Salir")
            print("")
            print("-----------------------------------------------")
            print("")
            opcion = int(input("Ingrese la opción deseada (1-9): "))
            def Comprobacion(self, opcion):
                while True:
                    try:
                        if 1 <= opcion <= 9:
                            return opcion
                        else:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input("Ingrese la opción deseada (1-9): "))
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                        opcion = int(input("Ingrese la opción deseada (1-9): "))
            self.opcion = Comprobacion(self, opcion)
                
            if self.opcion == 1: #Crear Proyecto
                print("")
                print("Creacion de Proyecto \n")
                print("")                
                main.Agregar_Proyectos()
                
            elif self.opcion == 2: #Modificar Proyecto
                print("")
                print("Modificar Proyecto")
                
            elif self.opcion == 3: #Consultar Proyecto
                print("")
                print("Consultar Proyecto")
                
            elif self.opcion == 4: #Eliminar Proyecto
                print("")
                print("Eliminar Proyectos")
                print("")
                print("¿Qué proyecto desea eliminar?\n")
                main.Imprimir_Proyectos()
                print("")
                
                        
                main.Eliminar_Proyectos()
                print("Proyecto eliminado con éxito")
                print("")
                main.Imprimir_Proyectos()
                
                
                
            elif self.opcion == 5: #Listar Proyectos
                print("")
                print("Listar Proyectos")
                print("")
                print("¿Qué desea hacer?")
                print("1. Listar todos los proyectos")
                print("2. Listar por fecha mayor a, los proyectos")
                print("3. Consultar Proyecto por id")
                print("4. consultar por empresa")
                print("5. Listar Proyectos menor a una fecha")
                print("6. listar proyectos en un rango de fechas")
                print("7. listar proyectos por estado")
                opcion_5 = input("")
                while True:
                    if opcion_5 == "1":
                        main.Imprimir_Proyectos()
                        break
                    elif opcion_5 == "2":
                        main.filtrar_proyectos_por_fecha_mayor()
                        break
                    elif opcion_5 == "3":
                        main.filtrar_proyecto_por_id()
                        break
                    elif opcion_5 == "4":
                        main.filtrar_proyecto_por_empresa()
                        break
                    elif opcion_5 == "5":
                        main.filtrar_proyectos_por_fecha_menor()
                        break
                    elif opcion_5 == "6":
                        main.filtrar_proyectos_por_fecha_rango()
                        break
                    elif opcion_5 == "7":
                        main.filtrar_proyecto_por_estado()
                        break
                    else:
                        print("Elegir una opcion correcta")
                    
            elif self.opcion == 6: #Agregar Tarea
                print("")
                print("¿En que proyecto de desea agregar las tareas?\n")
                print("Nombre de los proyectos: \n")
                cont = main.Imprimir_Proyectos()
                print("")
                opcion = int(input("Ingrese la opción deseada (1-9): "))
                while True:
                    try:
                        if 1 <= opcion <= 9:
                            break
                        else:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input("Ingrese la opción deseada (1-9): "))
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                        opcion = int(input("Ingrese la opción deseada (1-9): "))
                
                #f opcion = :
                    
            elif self.opcion == 7:
                print("")
                print("Estas en el menu de Tareas\n")
                print("¿Qué desea hacer?\n")
                print("1. Agregar Tareas al inicio")
                print("2. Agregar Tareas al final")
                print("3. Modificar Tarea")
                print("4. Eliminar Tarea")
                print("5. Listar Tareas")
                print("")
                opcion = int(input("Ingrese la opción deseada (1-5): "))
                
                while True:
                    try:
                        if 1 <= opcion <= 5:
                            break
                        else:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input("Ingrese la opción deseada (1-5): "))
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                        opcion = int(input("Ingrese la opción deseada (1-5): "))
                if opcion == 1:
                    print("Agregar Tareas al inicio")
                    print("")
                    print("¿En que proyecto de desea agregar las tareas?\n")
                    print("Nombre de los proyectos: \n")
                    cont = main.Imprimir_Proyectos()
                    cont = cont[-1]
                    print("")
                    opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                    while True:
                        try:
                            if 1 <= opcion <= 9:
                                break
                            else:
                                print("Opción inválida, intente de nuevo")
                                opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                        except ValueError:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                    
                    main.agregar_pila()
                    main.recorre_pila()
                
                elif opcion == 2:
                    print("Agregar Tareas al final")
                    print("")
                    print("¿En que proyecto de desea agregar las tareas?\n")
                    print("Nombre de los proyectos: \n")
                    cont = main.Imprimir_Proyectos()
                    cont = cont[-1]
                    print("")
                    opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                    while True:
                        try:
                            if 1 <= opcion <= 9:
                                break
                            else:
                                print("Opción inválida, intente de nuevo")
                                opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                        except ValueError:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                    
                    main.agregar_cola()
                    main.recorre_cola()
                    
                elif opcion == 3:
                    print("Modificar Tarea")
                    print("")
                    print("¿En que proyecto de desea modificar las tareas?\n")
                    print("Nombre de los proyectos: \n")
                    cont = main.Imprimir_Proyectos()
                    cont = cont[-1]
                    print("")
                    opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                    while True:
                        try:
                            if 1 <= opcion <= 9:
                                break
                            else:
                                print("Opción inválida, intente de nuevo")
                                opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                        except ValueError:
                            print("Opción inválida, intente de nuevo")
                            opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                    #main.Modificar_Tarea()
                    
                elif opcion == 4:
                    print("Eliminar Tarea")
                    print("")
                    i = input("¿En que proyecto de desea eliminar las tareas en la pila(p) o en la cola (c)?: \n")
                    
                    while True:
                        if i.lower() == "p":
                           main.eliminar_pila()
                           main.recorre_pila()
                           break
                        elif i.lower() == "c":
                            main.eliminar_cola()
                            main.recorre_cola()
                            break
                        else:
                            print("Coloque el dato correcto")
                            
                    
                elif opcion == 5:
                    print("Listar Tareas")
                    print("")
                    print("")
                    print("¿Qué desea hacer?")
                    print("1. Listar todos las tareas")
                    print("2. Listar por fecha mayor a, las tareas")
                    print("5. Listar menor a una fecha")
                    print("6. listar en un rango de fechas")
                    print("7. listar por estado")
                    print("8. Listar por proyecto")
                    opcion_7 = input("")
                    while True:
                        if opcion_7 == "1":
                            main.Imprimir_Tareas()
                            break
                        if opcion_7 == "2":
                            main.filtrar_tareas_por_fecha_mayor()
                            break
                        if opcion_7 == "5":
                            main.filtrar_proyectos_por_fecha_menor()
                            break
                        elif opcion_7 == "7":
                            main.filtrar_tareas_por_estado()
                            break
                        elif opcion_7 == "6":
                            main.filtrar_tareas_por_fecha_rango()
                            break
                        elif opcion_7 == "8":
                            print("¿En que proyecto de desea listar las tareas?\n")
                            print("Nombre de los proyectos: \n")
                            cont = main.Imprimir_Proyectos()
                            cont = cont[-1]
                            print("")
                            opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                            while True:
                                try:
                                    if 1 <= opcion <= 9:
                                        break
                                    else:
                                        print("Opción inválida, intente de nuevo")
                                        opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                                except ValueError:
                                    print("Opción inválida, intente de nuevo")
                                    opcion = int(input(f"Ingrese la opción deseada (1-{cont}): "))
                            main.Imprimir_Tareas()
                            break
                        else:
                            print("elige una opcion valida")
                        
                
                
                
                
                
            elif self.opcion == 8:
                print("")
                print("Reportes\n")
                print("¿Qué desea hacer?\n")
                print("1. Consulta de Tareas por Estado:")
                print("2. Filtrado por Fecha")
                print("3. Filtrado de Proyectos")
                print("4. Listar sub tareas\n")
                while True:
                    try:
                        opcion = int(input("Ingrese la opción deseada (1-4): "))
                        if 1 <= opcion <= 4:
                            break
                        else:
                            print("Opción inválida, intente de nuevo")
                    except ValueError:
                        print("Opción inválida, intente de nuevo")
                
                
                
                
            elif self.opcion == 9:
                print("")
                print("Desea guardar los cambios realizados?")
                print("1. Si")
                print("2. No")
                guardar = input("Ingrese la opción deseada (1-2): ")
                if guardar == "1":
                    print("Guardando cambios...")
                    break
                elif guardar == "2":
                    print("Saliendo sin guardar cambios...")
                    break
                
        
        
menu = Menu()
menu.Mostrar_Menu()