import pandas as pd
import statsmodels.api as sm

# Membaca data dari file Excel
file_path = 'C:/project/python/regesi/sample.xlsx'
data = pd.read_excel(file_path)

# Menentukan variabel independen (X) dan dependen (y)
X = data[['radio', 'newspaper']]
y = data['sales']

# Menambahkan konstanta untuk model regresi linier
X = sm.add_constant(X)

# Membuat model regresi
model = sm.OLS(y, X).fit()

# Menampilkan hasil regresi
print(model.summary())