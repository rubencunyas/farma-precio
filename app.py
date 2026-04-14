import streamlit as st
import pandas as pd

st.set_page_config(page_title="FarmaPrecio", page_icon="💊")

st.title("💊 Compara Precios de Farmacias")
st.write("Encuentra el mejor precio para tus medicamentos")

busqueda = st.text_input("🔍 Busca un medicamento:", placeholder="Ej: Panadol")

if busqueda:
    productos_ficticios = [
        {"producto": "Panadol 500mg", "farmacia": "Inkafarma", "precio": 12.90},
        {"producto": "Panadol 500mg", "farmacia": "Boticas Perú", "precio": 11.50},
        {"producto": "Panadol 500mg", "farmacia": "Mifarma", "precio": 13.20},
        {"producto": "Panadol 500mg", "farmacia": "Farmacia del Pueblo", "precio": 10.90},
    ]
    
    df = pd.DataFrame(productos_ficticios)
    df = df.sort_values("precio")
    
    st.subheader("Resultados:")
    st.dataframe(df, hide_index=True)
    
    st.success(f"💰 El precio más bajo es: S/ {df.iloc[0]['precio']} en {df.iloc[0]['farmacia']}")
else:
    st.info("Escribe un medicamento para comenzar a comparar")