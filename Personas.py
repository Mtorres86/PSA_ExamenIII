import csv

class Persona:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.salario = float(salario)
        self.deducciones = float(deducciones)
        self.genero = genero
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class RegistroPersonas:
    def __init__(self):
        self.personas = []

    def cargar_datos_desde_csv(self, archivo):
        with open(archivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # saltar encabezados
            for row in reader:
                persona = Persona(*row)
                self.personas.append(persona)

    def persona_mayor_edad(self):
        return max(self.personas, key=lambda x: x.edad)

    def persona_menor_edad(self):
        return min(self.personas, key=lambda x: x.edad)

    def contar_genero(self):
        hombres = sum(1 for persona in self.personas if persona.genero.lower() == 'masculino')
        mujeres = len(self.personas) - hombres
        return hombres, mujeres

    def promedio_salario(self):
        total_salarios = sum(persona.salario for persona in self.personas)
        return total_salarios / len(self.personas)

    def persona_mas_deducciones(self):
        return max(self.personas, key=lambda x: x.deducciones)

    def persona_mayor_salario(self):
        return max(self.personas, key=lambda x: x.salario)


registro = RegistroPersonas()
registro.cargar_datos_desde_csv('datos.csv')


print("Persona con mayor edad:", registro.persona_mayor_edad())
print("Persona con menor edad:", registro.persona_menor_edad())
hombres, mujeres = registro.contar_genero()
print("Cantidad de Hombres:", hombres)
print("Cantidad de Mujeres:", mujeres)
print("Promedio de salario:", registro.promedio_salario())
print("Persona con más deducciones:", registro.persona_mas_deducciones())
print("Persona que gana más:", registro.persona_mayor_salario())
