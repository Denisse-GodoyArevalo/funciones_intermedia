#2 iterar a traves de una lista de diccionarios 
def  iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key}: {value}")

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(estudiantes) 