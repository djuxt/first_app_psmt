import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Primer Programa Ciencia de Datos
"""

 
def main():
    st.title('Mi Aplicación Básica en Streamlit')
    
    # Pedir datos al usuario
    user_input = st.text_input('Ingresa algún dato:')
    
    # Mostrar los datos ingresados
    if user_input:
        st.write(f'Has ingresado: {user_input}')
    
if __name__ == '__main__':
    main()
