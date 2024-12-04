def guardar_record(ruta_archivo: str, datos_del_juego: dict) -> bool:
    '''
    Guarda los datos del jugador en el archivo
    Si el jugador ya existe, actualiza sus datos sumando los nuevos valores si no, lo agrega sin borrar los registros anteriores
    '''
    registros = leer_registros(ruta_archivo)
    ruta = f"E:/UTN PYGAME/archivos/{ruta_archivo}"
    encontrado = False

    print(f"Datos del juego a guardar: {datos_del_juego}")

    for usuario in registros:
        if datos_del_juego["Nombre"] == usuario["Nombre"]: 
            
            usuario["Partidas ganadas"] += datos_del_juego["Partidas ganadas"]
            usuario["Partidas perdidas"] += datos_del_juego["Partidas perdidas"]
            usuario["Partidas empatadas"] += datos_del_juego["Partidas empatadas"]
            
            encontrado = True
            break

    if encontrado == False:
        print(f"Agregando un nuevo registro para {datos_del_juego['Nombre']}")  
        registros.append(datos_del_juego)

    
    with open(ruta, "w", encoding="utf-8") as archivo:
        for fila in registros:
            print(f"Escribiendo en archivo: {fila}")  
            linea = (
                f"Nombre: {fila['Nombre']}, "
                f"Partidas ganadas: {fila['Partidas ganadas']}, " 
                f"Partidas perdidas: {fila['Partidas perdidas']}, " 
                f"Partidas empatadas: {fila['Partidas empatadas']}\n"
            )
            archivo.write(linea)
    return True


def leer_registros(ruta_archivo: str) -> list:
    '''
    Recibe una ruta de archivo
    Lee los registros desde el archivo
    Devuelve una lista de diccionarios.
    '''
    ruta = f"E:/UTN PYGAME/archivos/{ruta_archivo}"
    lista_retorno = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            valores = linea.strip().split(",")
            if len(valores) == 4:
                diccionario = {
                    "Nombre": valores[0],
                    "Partidas ganadas": valores[1],
                    "Partidas perdidas": valores[2],
                    "Partidas empatadas": valores[3],
                }
                lista_retorno.append(diccionario)
    
    return lista_retorno

