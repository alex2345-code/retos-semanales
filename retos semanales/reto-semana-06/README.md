
## Descripción del Proyecto

Este script en Python funciona como un **validador automático** para una empresa de logística. Procesa códigos de entrada estándar (`stdin`), detecta su naturaleza mediante expresiones regulares y aplica reglas de negocio estrictas para determinar si son válidos. 

El resultado se exporta a la salida estándar (`stdout`) en formato **CSV**.

Se validan cuatro tipos principales de códigos:
* **Producto** (Ej. `TEC-0001-MX`)
* **Envío** (Ej. `ENV-2024-03-15-001234`)
* **Empleado** (Ej. `EMP-VEN-1234`)
* **Factura** (Ej. `FAC-A-123456`)

> **Nota:** Cualquier código con una estructura no reconocida se clasifica automáticamente como `desconocido` e `INVALIDO`.

---

## Requisitos

* **Python 3.x**
* No se requieren librerías de terceros. El código utiliza exclusivamente los módulos de la biblioteca estándar `sys` y `re`.

---

##  Cómo ejecutar y probar

El script lee desde la entrada estándar y escribe en la salida estándar, ignorando las líneas en blanco.

### 1. Preparar los datos de prueba
Asegúrate de tener un archivo de texto con los códigos a evaluar, por ejemplo, `tests/codigos.txt`, con un código por línea.

### 2. Ejecutar el validador

**En Linux / Mac:**
```bash
python main.py < tests/codigos.txt > resultados.csv