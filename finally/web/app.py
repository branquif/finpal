import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="FinAlly - Gestão Financeira Familiar",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("FinAlly - Gestão Financeira Familiar")

# Sidebar
st.sidebar.title("Menu")
page = st.sidebar.selectbox(
    "Navegação",
    ["Dashboard", "Contas", "Transações", "Orçamentos", "Investimentos", "Relatórios"]
)

# Conteúdo principal
if page == "Dashboard":
    st.header("Dashboard")
    st.write("Bem-vindo ao FinAlly! Aqui você terá uma visão geral da sua situação financeira.")
elif page == "Contas":
    st.header("Contas")
    st.write("Gerencie suas contas bancárias, cartões de crédito e investimentos.")
# ... outras páginas

# Rodapé
st.markdown("---")
st.markdown("FinAlly - v0.1.0")
