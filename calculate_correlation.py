import pandas as pd
import scipy.stats

# Membaca data dari file Excel
file_path = 'C:/project/python/regesi/sample.xlsx'
data = pd.read_excel(file_path)

# Misalkan radio_values dan newspaper_values adalah array NumPy yang berisi data masing-masing variabel
radio_values = data['radio'].values
newspaper_values = data['newspaper'].values

# Hitung korelasi Pearson
correlation, p_value = scipy.stats.pearsonr(radio_values, newspaper_values)

# Tampilkan hasil
print(f'Korelasi Pearson antara radio dan newspaper: {correlation:.4f}')
print(f'P-value: {p_value:.4f}')
