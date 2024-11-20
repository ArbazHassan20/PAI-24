import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns

df = pd.read_csv('digits.csv')
pixels = df.drop(columns='number_label')
single_row = pixels.iloc[0]
single_row_array = single_row.to_numpy()
reshaped_array = single_row_array.reshape(8, 8)

plt.imshow(reshaped_array, cmap='gray')
plt.show()

scaler = StandardScaler()
scaled_pixels = scaler.fit_transform(pixels)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_pixels)

explained_variance = pca.explained_variance_ratio_
print(explained_variance)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=df['number_label'], palette='Set1')
plt.show()
 