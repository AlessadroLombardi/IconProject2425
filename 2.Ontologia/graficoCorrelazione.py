"""
@author: Gruppo NARDULLI-LOMBARDI

"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Caricamento dei dati
dataset = pd.read_csv("2.Ontologia/Cancer_Data.csv")

# Selezione delle colonne numeriche per la matrice di correlazione
# Escludiamo colonne non numeriche come 'id' e 'diagnosis'
numerical_columns = dataset.select_dtypes(include=['float64', 'int64']).columns.tolist()

# Creazione della matrice di correlazione
corr_matrix = dataset[numerical_columns].corr()

# Creazione della heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=False, cmap="coolwarm", cbar=True)
plt.title("Heat Map of Cancer Dataset Correlations")
plt.show()
