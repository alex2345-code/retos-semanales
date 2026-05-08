import sys
def main():
    #diccionario para agrupar por producto
    productos = {}

    primera_linea = True
    #leer todas las lineas 
    for linea in sys.stdin:
        linea = linea.strip()

        #saltar encabezado 
        if primera_linea:
            primera_linea = False
            continue

        #saltar lineas vacias 
        if not linea: 
            continue

        #parsear linea 
        partes = linea.split(',')
        if len(partes) != 4:
            continue #ignorar lineas invalidas 

        fecha = partes[0]
        producto = partes [1]

        #convertir cantidad y precio (con manejo de errores)
        try: 
            cantidad = int(partes[2])
            precio = float(partes[3])
        except ValueError:
            continue # ignorar si no son numeros validos

        #crear entrada si no existe 
        if producto not in productos:
            productos[producto] = {
                "unidades" = 0,
                "ingreso": 0.0
            }
#acumular
productos[producto]["unidades"] += cantidad
productos[producto]["ingreso"] += cantidad * precio 

#calcular precio promedio 
for prod in productos:
    unidades = productos[prod]["unidades"]
    ingreso = productos[prod]["ingreso"]
    productos[prod]["promedio"] = ingreso / unidades if unidades > 0 else 0

#ordenar por ingreso deescendente 
productos_ordenados = sorted(
    productos.items(),
    key=lambda x: x[1]["ingreso"],
    reverse=True
)
    
    


