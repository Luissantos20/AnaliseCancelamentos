import pandas as pd
import plotly.express as px

def carregar_dados():
    """Carrega e prepara os dados iniciais"""
    print("Passo 1: Importando a base de dados...")
    tabela = pd.read_csv("cancelamentos_sample.csv")
    return tabela

def limpar_dados(tabela):
    """Realiza a limpeza dos dados"""
    print("\nPasso 2: Limpando a base de dados...")
    
    # Removendo coluna não utilizada
    tabela = tabela.drop(columns="CustomerID")
    
    # Removendo valores vazios
    tabela = tabela.dropna()
    
    return tabela

def analise_inicial(tabela):
    """Realiza análise inicial dos cancelamentos"""
    print("\nPasso 3: Análise inicial dos cancelamentos")
    display(tabela.info())
    display(tabela["cancelou"].value_counts(normalize=True))

def analise_causas(tabela):
    """Analisa as causas dos cancelamentos"""
    print("\nPasso 4: Analisando causas dos cancelamentos")
    
    # Gera gráficos para todas as colunas
    for coluna in tabela.columns:
        grafico = px.histogram(tabela, x=coluna, color="cancelou", 
                              title=f"Cancelamentos por {coluna}",
                              labels={coluna: coluna.replace("_", " ").title()})
        grafico.show()

def aplicar_filtros(tabela):
    """Aplica filtros para reduzir cancelamentos"""
    print("\nPasso 5: Aplicando filtros para redução de cancelamentos")
    
    # Filtros identificados
    filtros = [
        tabela["ligacoes_callcenter"] <= 4,
        tabela["dias_atraso"] <= 20,
        tabela["duracao_contrato"] != "Monthly"
    ]
    
    for filtro in filtros:
        tabela = tabela[filtro]
    
    return tabela

def main():
    # Fluxo principal de análise
    dados = carregar_dados()
    dados_limpos = limpar_dados(dados)
    analise_inicial(dados_limpos)
    analise_causas(dados_limpos)
    
    # Análise após aplicação de filtros
    dados_filtrados = aplicar_filtros(dados_limpos)
    print("\nResultado após aplicação dos filtros:")
    display(dados_filtrados["cancelou"].value_counts(normalize=True))

if __name__ == "__main__":
    main()