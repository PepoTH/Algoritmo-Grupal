class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def modify(self, old_data, new_data):
        node_to_modify = self.find(old_data)
        if node_to_modify:
            node_to_modify.data = new_data
            return True
        else:
            return False

    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def consult(self, key):
        node = self.find(key)
        if node:
            return node.data
        else:
            return None

# Ejemplo de uso:
linked_list = LinkedList()
linked_list.add("primer")
linked_list.add("segundo")
linked_list.add("tercero")

print("Lista original:", linked_list.list())

# Modificar un elemento
linked_list.modify("segundo", "modificado")
print("Lista después de modificar 'segundo' por 'modificado':", linked_list.list())

# Consultar un elemento
print("Consulta del elemento 'modificado':", linked_list.consult("modificado"))

# Eliminar un elemento
linked_list.delete("modificado")
print("Lista después de eliminar 'modificado':", linked_list.list())