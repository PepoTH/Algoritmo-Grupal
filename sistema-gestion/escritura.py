import json

id = 'hola'

data = {}
data['Proyectos'] = []
data['Proyectos'].append({
'ID':id
})

with open('datos.json','w') as file:
    json.dump(data,file)