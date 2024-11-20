import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('digits.csv')
X = df.drop(columns='number_label')
y = df['number_label']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(X_scaled)

sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=y, palette='Set1')
plt.show()
