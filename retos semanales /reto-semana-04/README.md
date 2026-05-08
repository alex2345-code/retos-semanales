# Sistema de Inventario Modular

## Descripcion
Sistema que genera reportes de productos que necesitan reorden. 
Lee un archivo de inventario en CSV, filtra los productos con stock por debajo del mínimo, y genera un reporte de compras con la cantidad de unidades faltantes y el valor del inventario.

## Estructura del Proyecto
```
reto-semana-04/
├── main.py                    # Punto de entrada
├── README.md                  # Documentacion
├── .gitignore                 # Archivos a ignorar
├── models/                    # Clases de dominio
│   ├── __init__.py
│   └── producto.py            # Clase Producto
├── utils/                     # Utilidades
│   ├── __init__.py
│   ├── io.py                  # Funciones de lectura/escritura
│   └── validators.py          # Funciones de validacion
├── data/                      # Datos de entrada
│   └── inventario.csv         # Datos iniciales
└── outputs/                   # Resultados
    └── reporte_inventario.csv # Reporte de salida
```

## Como Ejecutar
```bash
python main.py
```

## Entrada
El archivo `data/inventario.csv` contiene los datos actuales del inventario.
Las columnas esperadas son:
- `sku`: Identificador unico del producto
- `nombre`: Nombre del producto
- `categoria`: Categoria del producto
- `precio`: Precio unitario (número decimal)
- `stock`: Cantidad actual en inventario (número entero)
- `stock_minimo`: Nivel minimo antes de reordenar (número entero)

El sistema ignora silenciosamente cualquier fila que contenga datos inválidos (como letras en campos numéricos).

## Salida
El archivo `outputs/reporte_inventario.csv` contiene los productos que requieren reorden (`stock < stock_minimo`).
Se genera con las siguientes columnas:
- `sku`
- `nombre`
- `categoria`
- `stock_actual`
- `stock_minimo`
- `unidades_faltantes` (calculado como `stock_minimo - stock_actual`)
- `valor_inventario` (calculado como `precio * stock_actual`)

Los resultados se ordenan de forma descendente según la cantidad de unidades faltantes.

## Autor
Alexis Pineda
