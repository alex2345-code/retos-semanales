import sys


def limpiar_valor(valor):
    """
    Quita espacios y elimina caracteres inválidos.
    Solo permite dígitos, punto decimal y signo negativo.
    """
    valor = valor.strip()
    caracteres_validos = '0123456789.-'
    resultado = ''
    for char in valor:
        if char in caracteres_validos:
            resultado += char
    return resultado


def convertir_a_entero(texto):
    """Convierte texto limpio a entero, truncando decimales."""
    if not texto:
        return 0
    try:
        numero = float(texto)
        return int(numero)   # int() trunca hacia cero (no redondea)
    except ValueError:
        return 0


def procesar_linea(linea):
    """
    Procesa una línea completa y devuelve la suma.
    """
    linea = linea.strip()

    # Regla 1: línea vacía → 0
    if not linea:
        return 0

    valores = linea.split(',')

    total = 0
    for valor in valores:
        valor_limpio = limpiar_valor(valor)
        total += convertir_a_entero(valor_limpio)

    return total


def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)






if __name__ == "__main__":
    main()