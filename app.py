import streamlit as st 

st.header('Lanzar una moneda')

#st.write('Esta aplicación aún no es funcional. En construcción.')
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.tk.Button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    
st.write('Esta aplicación aún no es funcional. En construcción.')