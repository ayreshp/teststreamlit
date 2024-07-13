import streamlit as st
import plotly.express as px


st.header("Maiores valores")

if 'dados' not in st.session_state:
    st.error("Os dados não forma carregados")
else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']

    col1, col2, col3 = st.columns(3)

    with col1:
        Mempenho = dados.nlargest(top_n, 'VALOREMPENHO')
        fig = px.bar(Mempenho, x='MUNICIPIO', y='VALOREMPENHO',
                     title='Maiores Empenhos')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        Mpibs = dados.nlargest(top_n, 'PIB')
        fig2 = px.pie(Mpibs, values='PIB', names='MUNICIPIO',
                     title='Maiores pib')
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        Mprop = dados.nlargest(top_n, 'PROPOCAO')
        fig3 = px.bar(Mempenho, x='MUNICIPIO', y='PROPOCAO',
                     title='Maiores gastos em proporção ao PIB')
        st.plotly_chart(fig3, use_container_width=True)
