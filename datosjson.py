import json

def modificar_json(nombre_archivo, clave, valor):
   
    with open(nombre_archivo, 'r') as file:
        data = json.load(file)

    # Buscamos el key y lo modificamos (en este caso usaremos la key de "CLUBS")
    if clave in data:
        if clave == 'name':
            # Aqui modifcamos el nom,mbre con el nuevo valor
            data[clave] = valor
        elif clave == 'clubs':
            # Varificamos que exista 
            nuevo_club = True
            for club in data[clave]:
                if club['name'] == valor:
                    nuevo_club = False
                    break
            # Si no existe entonces lo agregos
            if nuevo_club:
                nuevo_club = {'name': valor, 'period': '2024-present'}
                data[clave].append(nuevo_club)
        else:
            # Reemplazar el valor existente con el nuevo valor
            data[clave] = valor

    # Guardar el JSON modificado en el archivo
    with open(nombre_archivo, 'w') as file:
        json.dump(data, file, indent=4)

# Modificar el archivo JSON
# Veremos que se agregara un nuevo club, originalmente hay 2 aqui agregamos 1 tercero. 
modificar_json('datos.json', 'name', 'Andres Iniesta Perez')
modificar_json('datos.json', 'clubs', 'New Club')

print("Archivo modificado exitosamente.")
