# Función con parámetros y retorno de valor
def calcular_total_compra(precio_unitario, cantidad):
    subtotal = precio_unitario * cantidad
    
    # Aplica un 10% de descuento si la compra supera $50
    if subtotal > 50:
        total = subtotal * 0.90
    else:
        total = subtotal
        
    return total  # Uso de la palabra clave return

# Programa principal
print("=== CALCULADORA DE PRECIO TOTAL ===")

# Entrada de datos
precio = float(input("Ingrese el precio del producto: $"))
cantidad = int(input("Ingrese la cantidad comprada: "))

# Llamada a la función
total_a_pagar = calcular_total_compra(precio, cantidad)

# Mostrar el resultado en pantalla
print(f"El total a pagar es: ${total_a_pagar:.2f}")