import pandas as pd
import matplotlib.pyplot as plt

file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

ds_data = df_raw.groupby(['Country']).size()

print('-' * 100)
print(ds_data)

# print('-' * 100)
# ds_data = ds_data.nlargest(20)
# print(type(ds_data))
#
# ds_data.plot.pie(figsize = (10, 10))    # 인치 단위
# plt.tight_layout()
# plt.show()

print('-' * 100)
ds_data.nlargest(20).plot.pie(figsize = (10, 10))
plt.tight_layout()
plt.show()