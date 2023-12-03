import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data dari file Excel
file_path = 'C:/project/python/regesi/sample.xlsx'
data = pd.read_excel(file_path)

# Scatter plot 'Sales' vs 'Radio' dengan garis regresi
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.regplot(x='radio', y='sales', data=data, scatter_kws={'alpha':0.7})
plt.title('Sales vs Radio')
plt.xlabel('radio')
plt.ylabel('sales')

# Scatter plot 'Sales' vs 'Newspaper' dengan garis regresi
plt.subplot(1, 2, 2)
sns.regplot(x='newspaper', y='sales', data=data, scatter_kws={'alpha':0.7})
plt.title('Sales vs Newspaper')
plt.xlabel('newspaper')
plt.ylabel('sales')

plt.tight_layout()
plt.show()
