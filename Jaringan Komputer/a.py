import numpy as np
import pandas as pd

np.random.seed(42)  # Untuk reproduktibilitas

# Tentukan jumlah baris dan kolom
num_rows = 106
num_columns = 25

# Hasilkan data acak
data = np.random.rand(num_rows, num_columns)

# Buat DataFrame dengan data yang dihasilkan
columns = [f'Column_{i+1}' for i in range(num_columns)]
df = pd.DataFrame(data, columns=columns)

# Simpan DataFrame ke file Excel
excel_file_path = 'synthetic_data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Data telah disimpan dalam file Excel: {excel_file_path}")
