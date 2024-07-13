import streamlit as st
from st_aggrid import AgGrid

if 'dados' not in st.session_state:
    st.error("Os dados não forma carregados")
else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']
    dados_filtrados = dados.head(top_n)
    AgGrid(dados_filtrados, fit_columns_on_grid_load=True)
    