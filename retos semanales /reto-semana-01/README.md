# Reto Semana 1: Calculadora de Sumas

## Descripción

Programa que lee líneas desde stdin, donde cada línea contiene valores separados por comas, y calcula la suma de los valores en cada línea.

El programa maneja datos "sucios" del mundo real:
- Líneas vacías
- Números decimales (truncados, no redondeados)
- Caracteres inválidos mezclados (ej: `1a2`, `$100`)
- Espacios extra alrededor de los valores

## Requisitos

- Python 3.x
- No requiere librerías externas

## Uso

### Desde un archivo
```bash
python3 main.py < entrada.txt
```

### Guardar la salida
```bash
python3 main.py < entrada.txt > salida.txt
```

### Entrada manual
```bash
python3 main.py
# Escribe líneas manualmente
# Presiona Ctrl+D para terminar
```

## Ejemplo

**Entrada:**
```
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15  
```

**Salida:**
```
6
10
0
6
19
8
30
```

## Reglas de procesamiento

| Caso | Entrada | Salida | Explicación |
|------|---------|--------|-------------|
| Línea vacía | `` | `0` | Sin valores |
| Un elemento | `3.9` | `3` | Se trunca, no redondea |
| Múltiples | `1,2,3` | `6` | Suma normal |
| Decimales | `1.9,2.1` | `3` | `1+2=3` (truncados) |
| Caracteres basura | `1a2,3b` | `15` | `12+3=15` |
| Espacios | ` 5 , 10 ` | `15` | Se ignoran espacios |
| Negativos | `-5,10,3` | `8` | `-5+10+3` |

## Autor

Ortiz Pineda Alexis Imanol
Instituto Politécnico Nacional
