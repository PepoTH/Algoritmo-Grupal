import json

class Tarea:
    def __init__(self, id, nombre, cliente_empresa, descripcion, fecha_inicio, fecha_vencimiento, estado, porcentaje):
        self.id = id
        self.nombre = nombre
        self.cliente_empresa = cliente_empresa
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.porcentaje = porcentaje
        self.subtareas = []
        self.nivel = 0

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

    def __str__(self):
        return f"Tarea {self.id}: {self.nombre} ({self.estado})"

class ArbolDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea, padre=None, nivel=0):
        tarea.nivel = nivel
        self.tareas.append(tarea)
        if padre:
            padre.agregar_subtarea(tarea)

    def obtener_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
        return None

    def listar_tareas_en_nivel(self, nivel):
        tareas_en_nivel = []
        for tarea in self.tareas:
            if tarea.nivel == nivel:
                tareas_en_nivel.append(tarea)
        return tareas_en_nivel

    def mostrar_subtareas(self, tarea):
        print(f"Subtareas de {tarea.nombre}:")
        for subtarea in tarea.subtareas:
            print(f"  {subtarea.nombre}")

    def serializar_a_json(self):
        arbol_de_tareas_json = {"tareas": []}
        for tarea in self.tareas:
            tarea_json = {
                "id": tarea.id,
                "nombre": tarea.nombre,
                "cliente_empresa": tarea.cliente_empresa,
                "descripcion": tarea.descripcion,
                "fecha_inicio": tarea.fecha_inicio,
                "fecha_vencimiento": tarea.fecha_vencimiento,
                "estado": tarea.estado,
                "porcentaje": tarea.porcentaje,
                "subtareas": []
            }
            for subtarea in tarea.subtareas:
                tarea_json["subtareas"].append(subtarea.id)
            arbol_de_tareas_json["tareas"].append(tarea_json)
        return json.dumps(arbol_de_tareas_json)

    def cargar_desde_json(self, cadena_json):
        arbol_de_tareas_json = json.loads(cadena_json)
        for tarea_json in arbol_de_tareas_json["tareas"]:
            tarea = Tarea(
                tarea_json["id"],
                tarea_json["nombre"],
                tarea_json["cliente_empresa"],
                tarea_json["descripcion"],
                tarea_json["fecha_inicio"],
                tarea_json["fecha_vencimiento"],
                tarea_json["estado"],
                tarea_json["porcentaje"]
            )
            for subtarea_id in tarea_json["subtareas"]:
                subtarea = self.obtener_tarea(subtarea_id)
                if subtarea:
                    tarea.agregar_subtarea(subtarea)
            self.agregar_tarea(tarea)

# Ejemplo de uso
arbol_de_tareas = ArbolDeTareas()

tarea1 = Tarea(1, "Tarea 1", "Cliente 1", "Descripción 1", "2022-01-01", "2022-01-31", "En progreso", 50)
tarea2 = Tarea(2, "Tarea 2", "Cliente 2", "Descripción 2", "2022-02-01", "2022-02-28", "Nueva", 0)
tarea3 = Tarea(3, "Tarea 3", "Cliente 1", "Descripción 3","2022-03-01", "2022-03-31", "Hecha", 100)

arbol_de_tareas.agregar_tarea(tarea1)  # nivel 0
arbol_de_tareas.agregar_tarea(tarea2, tarea1, 1)  # nivel 1, padre es tarea1
arbol_de_tareas.agregar_tarea(tarea3, tarea2, 2)  # nivel 2, padre es tarea2


arbol_de_tareas.mostrar_subtareas(tarea1)  # Subtareas de Tarea 1: Tarea 2
arbol_de_tareas.mostrar_subtareas(tarea2)  # Subtareas de Tarea 2: Tarea 3

cadena_json = arbol_de_tareas.serializar_a_json()
arbol_de_tareas.cargar_desde_json(cadena_json)