import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Primer Programa Ciencia de Datos
"""

 
def main():
    st.title('Analisis de Cienda de datos')
    
    # Pedir datos al usuario
    user_input = st.text_input('Ingrese su edad:')
    
    # Mostrar los datos ingresados
    if user_input:
        st.write(f'Su edad es: {user_input}')
    
if __name__ == '__main__':
    main()
