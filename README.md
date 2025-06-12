# 📉 Análise de Cancelamentos de Clientes

Este projeto realiza uma análise exploratória de dados com foco em entender e reduzir os cancelamentos de clientes em uma base de dados fictícia. O objetivo é identificar padrões e aplicar filtros que ajudem a diminuir a taxa de cancelamento de contratos.

---

## 🧪 Funcionalidades do Projeto

- 📥 **Carregamento de dados**: leitura de um arquivo CSV com informações de clientes.
- 🧹 **Limpeza de dados**: remoção de colunas desnecessárias e tratamento de valores ausentes.
- 📊 **Análise inicial**: visualização da proporção de cancelamentos e estrutura da base.
- 🔍 **Análise das causas**: gráficos interativos para entender os fatores relacionados ao cancelamento.
- 🚫 **Aplicação de filtros**: identificação de critérios para redução de cancelamentos.

---

## 📁 Estrutura do Código

O código está dividido em funções principais:

- `carregar_dados(caminho_arquivo)`: Lê e retorna a base de dados.
- `limpar_dados(tabela)`: Remove colunas e dados ausentes.
- `analise_inicial(tabela)`: Mostra informações gerais e proporção de cancelamentos.
- `analise_causas(tabela)`: Gera gráficos por coluna para investigar causas dos cancelamentos.
- `aplicar_filtros(tabela)`: Aplica filtros baseados nos dados analisados e compara os resultados.

---

## 📈 Resultado Obtido

Após a análise e aplicação de filtros baseados nos dados:

- **Total de registros após os filtros**: `26.267`
- **Proporção de cancelamentos após filtro**:  
  - Não cancelaram: `81,65%`  
  - Cancelaram: `18,35%`
- **Comparativo com dados originais**:
  - Taxa de cancelamento original: `56,79%`
  - Taxa de cancelamento com filtros: `18,35%`
  - **Redução de cancelamentos**: `67,68%`

---

## 🧰 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- Jupyter Notebook (ou qualquer ambiente que suporte `IPython.display`)

---

## 📂 Como usar

1. Instale as dependências:
    pip install pandas plotly
    Execute o script (preferencialmente em um notebook):

2. Ajuste o caminho do arquivo CSV:
    caminho = "cancelamentos_sample.csv"
    Rode o fluxo principal para ver os resultados passo a passo.

📌 Observações
    Certifique-se de que o arquivo cancelamentos_sample.csv esteja na mesma pasta do script ou informe o caminho correto.




