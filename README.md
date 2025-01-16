# 💬 Dashboard Financeiro com IA
![Imagem do projeto](https://i.postimg.cc/9XDfN2F3/dash.png)

Bem-vindo ao **Dashboard Financeiro com IA**, uma aplicação poderosa desenvolvida para visualizar movimentações financeiras e integrar com a API da OpenAI, permitindo análises e sugestões inteligentes sobre seus dados financeiros. 🚀

## 📌 Funcionalidades

- **Carregamento de Dados:** Faça o upload de um arquivo CSV contendo suas movimentações financeiras.
- **Análise Resumida:** Visualize entradas, saídas e saldo total de forma clara e objetiva.
- **Gráficos Interativos:** Explore gráficos para acompanhar movimentações ao longo do tempo.
- **Chat com IA:** Interaja com uma IA treinada para analisar suas movimentações e responder perguntas financeiras.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/):** Linguagem de programação base do projeto.
- **[Streamlit](https://streamlit.io/):** Framework para criação de aplicações web interativas.
- **[Pandas](https://pandas.pydata.org/):** Manipulação e análise de dados financeiros.
- **[Plotly](https://plotly.com/python/):** Criação de gráficos interativos.
- **[OpenAI API](https://openai.com/):** Integração com GPT-4 para respostas inteligentes.

---

## ⚙️ Configuração e Execução

### Pré-requisitos

Certifique-se de ter instalado:

- Python 3.8 ou superior
- Uma chave válida para a API da OpenAI

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/EltonSA/DASH-FINANCEIRO.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/MacOS
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   streamlit run dash.py
   ```

---

## 📂 Estrutura do Projeto

```plaintext
.
├── dash.py               # Código principal do aplicativo
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
└── exemplos/
    └── exemplo.csv       # Arquivo exemplo para teste
```

---

## 🧑‍💻 Uso da Aplicação

1. Faça o upload de um arquivo CSV contendo as seguintes colunas:
   - **Data**: Formato `DD/MM/YYYY`
   - **Valor**: Valores numéricos (positivos para entradas, negativos para saídas)
   - **Identificador**: Identificação única da transação
   - **Descrição**: Detalhes da transação

2. Insira sua chave da API da OpenAI na barra lateral.

3. Utilize a seção de chat para fazer perguntas sobre suas movimentações, como:
   - "Qual foi minha maior saída em janeiro?"
   - "Qual o saldo acumulado até agora?"

---

## 📊 Exemplos de Análise Visual

### Resumo Financeiro

![Resumo Financeiro](https://prnt.sc/kEcmIb8I5qNF)

### Gráfico de Movimentações

![Gráfico de Movimentações](https://prnt.sc/LxaT3kXj5RBB)

---

## 🤝 Contribuição

Sinta-se à vontade para contribuir! Abra uma issue ou envie um pull request com melhorias ou novas funcionalidades.

---

## 📝 Licença

Este projeto está licenciado sob a [Elton Santos]. Sinta-se à vontade para utilizá-lo e adaptá-lo conforme necessário.

---

## 🌟 Agradecimentos

Agradecimentos especiais a todas as ferramentas e comunidades que tornaram este projeto possível! 💜

