print ('Hello Word')
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

# Solicitamos los datos al usuario
print("--- Calculadora de Divisas Interactiva ---")
try:
    mi_presupuesto = float(input("Ingresa tu presupuesto en moneda local: "))
    mi_tasa = float(input("Ingresa la tasa de cambio (¿Cuánto vale 1 unidad extranjera?): "))

    # Realizamos la conversión
    resultado = exchange_money(mi_presupuesto, mi_tasa)

    print(f"\nResultado: Con {mi_presupuesto} unidades originales, obtendrás {resultado:.2f} en la moneda local del país.")
except ValueError:
    print("Error: Por favor, ingresa solo números (usa punto para decimales).")