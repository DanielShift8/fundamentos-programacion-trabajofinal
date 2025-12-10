productos = [
    {"nombre": "Arroz", "cantidad": 8},
    {"nombre": "Azúcar", "cantidad": 3},
    {"nombre": "Aceite", "cantidad": 12},
    {"nombre": "Fideos", "cantidad": 2}
]

umbral = 5
alertas = []

for p in productos:
    if p["cantidad"] < umbral:
        alertas.append(p)

print("Productos con bajo stock:")
for a in alertas:
    print(f"{a['nombre']} → Cantidad: {a['cantidad']}")
