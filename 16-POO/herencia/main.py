import clases

persona = clases.Persona()
persona.setNombre('Mateo')
persona.setApellidos('Monsalve')
persona.setAltura('180cm')
persona.setEdad('22 años')

print(f'la persona es {persona.getNombre()} {persona.getApellidos()}')
print(persona.hablar())
print('---------------------------------------------')

informatico = clases.Informatico()
informatico.setNombre('Sebas')
informatico.setApellidos('Velez')
informatico.setEdad('23')

print(f'El informatico es {informatico.getNombre()} {informatico.getApellidos()}')
print(informatico.getLenguajes())
print(informatico.caminar())

print('---------------------------------------------')