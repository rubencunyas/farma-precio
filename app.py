import streamlit as st
import pandas as pd

st.set_page_config(page_title="💊 FarmaPrecio - Compara Precios", page_icon="💊")

st.title("💊 FarmaPrecio")
st.write("Compara precios de medicamentos en farmacias Peruvianas")

# Barra lateral
st.sidebar.header("Opciones")
st.sidebar.write("Versión: MVP 1.0")

# Buscador
busqueda = st.text_input("🔍 Busca un medicamento:", placeholder="Ej: Panadol, Apronax, Redoxon...")

# Base de datos de prueba más completa
productos_db = [
    {"producto": "Panadol 500mg", "farmacia": "Inkafarma", "precio": 12.90},
    {"producto": "Panadol 500mg", "farmacia": "Mifarma", "precio": 11.50},
    {"producto": "Panadol 500mg", "farmacia": "Boticas Perú", "precio": 10.90},
    {"producto": "Panadol 500mg", "farmacia": "Farmacia del Pueblo", "precio": 11.20},
    
    {"producto": "Apronax 550mg", "farmacia": "Inkafarma", "precio": 18.50},
    {"producto": "Apronax 550mg", "farmacia": "Mifarma", "precio": 17.90},
    {"producto": "Apronax 550mg", "farmacia": "Boticas Perú", "precio": 16.50},
    {"producto": "Apronax 550mg", "farmacia": "Farmacia del Pueblo", "precio": 17.00},
    
    {"producto": "Redoxon Vit C", "farmacia": "Inkafarma", "precio": 15.90},
    {"producto": "Redoxon Vit C", "farmacia": "Mifarma", "precio": 14.50},
    {"producto": "Redoxon Vit C", "farmacia": "Boticas Perú", "precio": 13.90},
    {"producto": "Redoxon Vit C", "farmacia": "Farmacia del Pueblo", "precio": 14.20},
    
    {"producto": "Betaloc 100mg", "farmacia": "Inkafarma", "precio": 32.00},
    {"producto": "Betaloc 100mg", "farmacia": "Mifarma", "precio": 30.50},
    {"producto": "Betaloc 100mg", "farmacia": "Boticas Perú", "precio": 29.90},
    {"producto": "Betaloc 100mg", "farmacia": "Farmacia del Pueblo", "precio": 31.00},
]

if busqueda:
    # Filtrar productos que contengan el texto buscado
    resultados = [p for p in productos_db if busqueda.lower() in p["producto"].lower()]
    
    if resultados:
        df = pd.DataFrame(resultados)
        df = df.sort_values("precio")
        
        # Encontrar el precio mínimo
        precio_min = df["precio"].min()
        
        st.subheader(f"📋 Resultados para: {busqueda}")
        st.dataframe(df, hide_index=True, use_container_width=True)
        
        # Resaltar el mejor precio
        mejor = df.iloc[0]
        st.markdown(f"""
        <div style="background-color: #d4edda; padding: 15px; border-radius: 10px; text-align: center;">
            <h2 style="margin: 0; color: #155724;">💰 Mejor Precio: S/ {mejor['precio']}</h2>
            <p style="margin: 5px 0 0 0; color: #155724;">en {mejor['farmacia']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Diferencia de precio
        precio_max = df["precio"].max()
        ahorro = precio_max - precio_min
        if ahorro > 0:
            st.info(f"Puedes ahorrar hasta S/ {ahorro:.2f} comparando precios")
    else:
        st.warning("No se encontraron productos. Prueba con otro nombre.")
else:
    st.info("💡 Escribe un medicamento para comenzar a comparar precios")
    st.markdown("---")
    st.markdown("### 🏥 Farmacias disponibles:")
    st.write("- Inkafarma")
    st.write("- Mifarma")
    st.write("- Boticas Perú")
    st.write("- Farmacia del Pueblo")