def guardar_record(ruta_archivo: str, datos_del_juego: dict):
    '''
    Recibe la ruta de un archivo y un diccionario con información del juego.
    Lee los registros existentes y los actualiza según los datos del juego.
    '''
    registros = leer_registros(ruta_archivo)

    usuario_encontrado = False
    for usuario in registros:
        if usuario["Nombre"] == datos_del_juego["Nombre"]:
            usuario["Partidas ganadas"] = int(usuario["Partidas ganadas"]) + int(datos_del_juego["Partidas ganadas"])
            usuario["Partidas perdidas"] = int(usuario["Partidas perdidas"]) + int(datos_del_juego["Partidas perdidas"])
            usuario["Partidas empatadas"] = int(usuario["Partidas empatadas"]) + int(datos_del_juego["Partidas empatadas"])
            usuario_encontrado = True
            break

    if usuario_encontrado == False:
        registros.append(datos_del_juego)

    ruta = f"archivos/{ruta_archivo}"
    with open(ruta, "w", encoding="utf-8") as archivo:
        for fila in registros:
            linea = (
                f"{fila['Nombre']}, "
                f"{fila['Partidas ganadas']}, "
                f"{fila['Partidas perdidas']}, "
                f"{fila['Partidas empatadas']}\n"
            )
            archivo.write(linea)



def leer_registros(ruta_archivo: str) -> list:
    '''
    Recibe una ruta de archivo
    Lee los registros desde el archivo
    Devuelve como una lista de diccionarios.
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

