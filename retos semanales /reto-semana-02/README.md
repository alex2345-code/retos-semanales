# Conversor de Temperaturas

Script de Python que lee un CSV desde stdin con temperaturas de ciudades, las convierte a Celsius y las clasifica.

## Como usarlo

```bash
python main.py < datos.csv
```

## Formato de entrada

El CSV debe tener encabezado y 3 columnas: ciudad, temperatura y unidad (C o F).

```
ciudad,temperatura,unidad
Monterrey,95,F
Ciudad de Mexico,18,C
```

## Formato de salida

```
ciudad,temperatura_celsius,clasificacion
Monterrey,35.0,Calido
Ciudad de Mexico,18.0,Templado
```

## Clasificaciones

- Menos de 0 grados: Congelante
- 0 a 15 grados: Frio
- 16 a 25 grados: Templado
- 26 a 35 grados: Calido
- Mas de 35 grados: Extremo

## Notas

- Si una linea tiene formato invalido o la unidad no es C o F, se ignora.
- Requiere Python 3.