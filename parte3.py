#3 Obtener valores de una lista de diccionarios
def  iterateDictionary2(name,some_list):
    for dictionary in some_list:
        if name in dictionary:
            print(dictionary[name])
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]            
name ='first_name'
iterateDictionary2(name, estudiantes)
print("--------------")
def  iterateDictionary2(apellido,some_list):
    for dictionary in some_list:
        if apellido in dictionary:
            print(dictionary[apellido])
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]            
apellido= 'last_name'
iterateDictionary2(apellido, estudiantes)
