#Iterar a través de un diccionarios con valores de lista
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{key} tiene {len(value)} elemento(s): \n{value}")
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)