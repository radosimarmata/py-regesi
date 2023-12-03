import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file Excel
file_path = 'C:/project/python/regesi/sample.xlsx'
data = pd.read_excel(file_path)

# Scatter plot 'Sales' vs 'Radio'
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(data['radio'], data['sales'], alpha=0.7)
plt.title('Sales vs Radio')
plt.xlabel('radio')
plt.ylabel('sales')

# Scatter plot 'Sales' vs 'Newspaper'
plt.subplot(1, 2, 2)
plt.scatter(data['newspaper'], data['sales'], alpha=0.7)
plt.title('Sales vs Newspaper')
plt.xlabel('newspaper')
plt.ylabel('sales')

plt.tight_layout()
plt.show()
