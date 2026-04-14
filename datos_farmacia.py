productos_ficticios = [
    {"producto": "Panadol 500mg", "farmacia": "Inkafarma", "precio": 12.90},
    {"producto": "Panadol 500mg", "farmacia": "Boticas Perú", "precio": 11.50},
    {"producto": "Panadol 500mg", "farmacia": "Mifarma", "precio": 13.20},
    {"producto": "Panadol 500mg", "farmacia": "Farmacia del Pueblo", "precio": 10.90},
]

for p in productos_ficticios:
    print(f"{p['producto']} en {p['farmacia']}: S/ {p['precio']}")