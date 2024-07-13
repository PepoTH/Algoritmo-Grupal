import csv

class Tarea:
    def __init__(self, id, nombre, descripcion, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, tarea):
        if not self.head:
            self.head = tarea
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = tarea

    def to_list(self):
        tarea_list = []
        current = self.head
        while current:
            tarea_list.append(current)
            current = current.next
        return tarea_list

class Sprint:
    def __init__(self, id, nombre, fecha_inicio, fecha_fin, estado, objetivos, equipo):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.objetivos = objetivos
        self.equipo = equipo
        self.tareas = LinkedList()

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        return self.tareas.to_list()

class AVLNode:
    def __init__(self, sprint):
        self.sprint = sprint
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, sprint):
        if not self.root:
            self.root = AVLNode(sprint)
        else:
            self._insert(self.root, sprint)

    def _insert(self, node, sprint):
        if sprint.id < node.sprint.id:
            if node.left:
                self._insert(node.left, sprint)
            else:
                node.left = AVLNode(sprint)
        else:
            if node.right:
                self._insert(node.right, sprint)
            else:
                node.right = AVLNode(sprint)

    def show_sprints_at_level(self, level):
        result = []
        self._show_sprints_at_level(self.root, level, result)
        return result

    def _show_sprints_at_level(self, node, level, result):
        if node:
            if level == 0:
                result.append(node.sprint)
            else:
                self._show_sprints_at_level(node.left, level - 1, result)
                self._show_sprints_at_level(node.right, level - 1, result)

    def show_subtareas(self, tarea_id):
        result = []
        self._show_subtareas(self.root, tarea_id, result)
        return result

    def _show_subtareas(self, node, tarea_id, result):
        if node:
            for tarea in node.sprint.tareas.to_list():
                if tarea.id == tarea_id:
                    result.append(tarea)
                    for subtarea in tarea.subtareas:
                        result.append(subtarea)
                    return
            self._show_subtareas(node.left, tarea_id, result)
            self._show_subtareas(node.right, tarea_id, result)

def load_data(file_path):
    avl_tree = AVLTree()
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sprint = Sprint(int(row['id']), row['nombre'], row['fecha_inicio'], row['fecha_fin'], row['estado'], row['objetivos'], row['equipo'])
            avl_tree.insert(sprint)
    return avl_tree

def save_data(avl_tree, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'objetivos', 'equipo'])
        for sprint in avl_tree.show_sprints_at_level(0):
            writer.writerow([sprint.id, sprint.nombre, sprint.fecha_inicio, sprint.fecha_fin, sprint.estado, sprint.objetivos, sprint.equipo])

def buscar_sprint(avl_tree, sprint_id):
    current = avl_tree.root
    while current:
        if current.sprint.id == sprint_id:
            return current.sprint
        elif sprint_id < current.sprint.id:
            current = current.left
        else:
            current = current.right
    return None

# Carga de datos
avl_tree = load_data('data.csv')

# Agregar tarea a un sprint
sprint_id = 1
tarea_id = 2
sprint = buscar_sprint(avl_tree, sprint_id)
if sprint:
    tarea = Tarea(tarea_id, 'Tarea 2', 'Descripción de la tarea 2', 'pendiente')
    sprint.agregar_tarea(tarea)
else:
    print("Sprint no encontrado")

# Mostrar tareas de un sprint
sprint_id = 1
sprint = buscar_sprint(avl_tree, sprint_id)
if sprint:
    tareas = sprint.mostrar_tareas()
    for tarea in tareas:
        print(f"Tarea {tarea.id}: {tarea.nombre} - {tarea.descripcion} - {tarea.estado}")
else:
    print("Sprint no encontrado")

# Guardar datos
save_data(avl_tree, 'data.csv')