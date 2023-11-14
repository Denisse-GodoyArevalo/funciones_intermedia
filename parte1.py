#1 Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

estudiantes[0]['last_name']= 'Bryan'
print(estudiantes)

directorio_deportes['fútbol'][directorio_deportes['fútbol'].index('Messi')] = 'Andres'
print(directorio_deportes)

z[0]['y']=30
print(z)