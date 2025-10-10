import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from ch05.common_function import is_windows_platform, get_font_name

# 한글 폰트 깨짐 처리
rc('font', family = get_font_name())
plt.rcParams['axes.unicode_minus'] = False

jumsu1_data = [3.5, 4.1, 4.2, 4.5]
jumsu2_data = [3.65, 4.12, 4.23, 4.5]
index_data = [2024, 2025, 2026, 2027]

df = pd.DataFrame(
    {
        '홍길동' : jumsu1_data,
        '이순신' : jumsu2_data,
    }
    , index = index_data)   # 인덱스 없어도 에러 안 남, 인덱스 지정하고 싶을 때 - -

df.plot.line()
plt.show()