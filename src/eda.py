import seaborn as sns
import matplotlib.pyplot as plt

def plotar_distribuicao_churn(df):
    sns.countplot(data=df, x='Churn')
    plt.title("Distribuição Churn (Evasão de Clientes)")
    plt.show()

def plotar_correlacao(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.show()
