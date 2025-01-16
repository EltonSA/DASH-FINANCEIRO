import pandas as pd
import streamlit as st
import plotly.express as px
import requests

# Função para carregar os dados do CSV
def carregar_dados(arquivo_csv):
    dados = pd.read_csv(arquivo_csv, sep=',')
    dados['Data'] = pd.to_datetime(dados['Data'], format='%d/%m/%Y')
    dados['Valor'] = pd.to_numeric(dados['Valor'], errors='coerce')
    return dados

# Função para gerar resposta da IA com base em uma pergunta
def perguntar_ia(dados, pergunta, api_key):
    # Transformar os dados em um formato legível para a IA
    dados_formatados = dados.to_dict(orient='records')

    # Prompt para a IA
    prompt = f"""
    Você é uma IA financeira que responde perguntas sobre movimentações financeiras de um usuário.
    Aqui estão os dados financeiros:
    {dados_formatados}

    Pergunta do usuário:
    {pergunta}

    Responda de forma clara e objetiva.
    """

    # Configuração para chamada da API
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": "Você é uma IA financeira que ajuda pessoas a entender suas movimentações financeiras."
            },
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Verifica erros na requisição
        resposta = response.json()
        resposta_ia = resposta['choices'][0]['message']['content']
        return resposta_ia
    except requests.exceptions.RequestException as e:
        return f"Erro ao se conectar à API da OpenAI: {e}"
    except (KeyError, IndexError):
        return "Erro ao processar a resposta da API da OpenAI."

# Função principal do app
def main():
    st.set_page_config(page_title="Dashboard Financeiro com IA", layout="wide")
    st.title("💬 Dashboard Financeiro com Chat IA")

    # Barra lateral para upload do arquivo
    st.sidebar.header("📂 Upload de Dados")
    arquivo_csv = st.sidebar.file_uploader("Carregue sua planilha CSV", type=["csv"])

    # Configuração da API da OpenAI
    st.sidebar.header("🔑 Configuração da OpenAI")
    api_key = st.sidebar.text_input("Insira sua chave API da OpenAI", type="password")

    if arquivo_csv is not None:
        dados = carregar_dados(arquivo_csv)

        # Mostra os dados brutos
        with st.expander("🔍 Visualizar Dados Carregados"):
            st.dataframe(dados)

        # Resumos financeiros
        entradas = dados[dados['Valor'] > 0]['Valor'].sum()
        saidas = dados[dados['Valor'] < 0]['Valor'].sum()
        saldo = entradas + saidas

        # Mostrando resumos em cartões
        st.subheader("📊 Resumo Financeiro")
        col1, col2, col3 = st.columns(3)
        col1.metric("💰 Entradas", f"R$ {entradas:,.2f}")
        col2.metric("💸 Saídas", f"R$ {abs(saidas):,.2f}")
        col3.metric("📈 Saldo", f"R$ {saldo:,.2f}")

        # Gráfico de movimentações ao longo do tempo
        st.subheader("📅 Movimentações ao Longo do Tempo")
        grafico_mov = dados.groupby(dados['Data'].dt.date)['Valor'].sum().reset_index()
        grafico_mov.columns = ['Data', 'Valor']
        fig = px.line(
            grafico_mov, 
            x="Data", 
            y="Valor", 
            title="Movimentações Diárias", 
            labels={"Data": "Data", "Valor": "Valor (R$)"},
            markers=True
        )
        fig.update_traces(line_color="green", line_width=3)
        st.plotly_chart(fig, use_container_width=True)

        # Gráfico de barras para entradas e saídas
        st.subheader("📊 Entradas vs. Saídas")
        resumo_categoria = pd.DataFrame({
            "Categoria": ["Entradas", "Saídas"],
            "Valor": [entradas, abs(saidas)]
        })
        fig_bar = px.bar(
            resumo_categoria,
            x="Categoria",
            y="Valor",
            text="Valor",
            color="Categoria",
            title="Resumo de Entradas e Saídas",
            color_discrete_map={"Entradas": "green", "Saídas": "red"}
        )
        fig_bar.update_traces(texttemplate="R$ %{text:,.2f}", textposition="outside")
        st.plotly_chart(fig_bar, use_container_width=True)

        # Seção de chat com a IA
        st.subheader("🤖 Converse com a IA sobre suas finanças")

        if api_key:
            # Histórico de conversa
            if "historico" not in st.session_state:
                st.session_state.historico = []

            # Caixa de texto para perguntas
            st.markdown("---")
            pergunta = st.text_input("Digite sua pergunta para a IA:")

            if st.button("Enviar"):
                if pergunta.strip():
                    with st.spinner("A IA está processando sua pergunta..."):
                        resposta = perguntar_ia(dados, pergunta, api_key)
                        st.session_state.historico.append((pergunta, resposta))

            # Exibir o histórico de perguntas e respostas
            if st.session_state.historico:
                st.markdown("### Histórico de Conversas")
                for pergunta, resposta in st.session_state.historico:
                    st.markdown(f"**Você:** {pergunta}")
                    st.markdown(f"**IA:** {resposta}")
        else:
            st.warning("Insira sua chave da API OpenAI na barra lateral para ativar o chat.")

    else:
        st.info("Por favor, carregue um arquivo CSV para visualizar o dashboard.")

# Executa o app
if __name__ == "__main__":
    main()
