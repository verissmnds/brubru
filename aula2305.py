import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste ECMI 2')

st.write("Tabela")

dataframe = pd.DataFrame({
    'Nome': ['Lavinia', 'Bruna', 'Anna B', 'Nataly', 'Anna L'],
    'Salário': [978, 18300, 2400, 4576, 1350]
})
dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = pd.DataFrame(
    np.random.randon(20, 3)
    columns=['a', 'b', 'c', 'd', 'e'])
    
    
